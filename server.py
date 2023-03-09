import socket
import sqlite3
import logging
import os

os.system('cls')
# Initialize logging
logging.basicConfig(filename='server.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Define host and port for the server
HOST = '127.0.0.1'
PORT = 65430

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a specific address and port
    s.bind((HOST, PORT))

    # Listen for incoming connections
    s.listen()

    # Print message to indicate that the server is running
    logging.info(f"Server is listening on {HOST}:{PORT}")
    print(f"Server is listening on {HOST}:{PORT}")

    # Connect to the database
    conn_db = sqlite3.connect('database.db')

    # Create a table if it doesn't exist
    conn_db.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT NOT NULL,
                  password TEXT NOT NULL);''')

    while True:
        # Wait for incoming connection
        conn_socket, addr = s.accept()
        with conn_socket:
            logging.info(f"Connected by {addr}")
            print(f"Connected by {addr}")

            while True:
                try:
                    # Receive data from the client
                    data = conn_socket.recv(1024)

                    if not data:
                        break

                    # Convert the data to a string and split it into parts
                    message = data.decode().strip()
                    parts = message.split()

                    # Log the message received from the client
                    logging.info(f"Received message from client: {message}")
                    print(f"Received message from client: {message}")

                    # Check the message type
                    if parts[0] == "register":
                        # Check if the username already exists in the database
                        username = parts[1]
                        password = parts[2]

                        # Check if the user already exists
                        cursor = conn_db.execute("SELECT * FROM users WHERE username = ?", (username,))
                        row = cursor.fetchone()
                        if row is not None:
                            # User already exists, send a response back to the client
                            response = "Username already in use"
                            conn_socket.sendall(response.encode())
                            continue

                        # If the user doesn't exist, insert a new record into the database
                        conn_db.execute(f"INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                        conn_db.commit()

                        # Log the new user registration
                        logging.info(f"New user registered: {username}")
                        print(f"New user registered: {username}")

                        # Send response back to the client
                        response = "User registered successfully"
                        conn_socket.sendall(response.encode())

                    elif parts[0] == "login":
                        # Check if user exists in the database
                        username = parts[1]
                        password = parts[2]
                        cursor = conn_db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
                        row = cursor.fetchone()

                        if row is not None:
                            # Log successful login attempt
                            logging.info(f"User logged in successfully: {username}")
                            print(f"User logged in successfully: {username}")

                            # Send response back to the client
                            response = "Login successful"
                            conn_socket.sendall(response.encode())
                    else:
                        # Log failed login attempt
                        logging.warning(f"Login failed for user: {username}")
                        print(f"Login failed for user: {username}")

                        # Send response back to the client
                        response = "Login failed"
                        conn_socket.sendall(response.encode())
                
                except Exception as e:
                    logging.error(f"Exception: {e}")
                    print(f"Exception: {e}")
                    break

            # Close the connection
            conn_socket.close()

