
import os
import socket
import logging
import sqlite3

from register import register_user
from login import login_user

HOST = "localhost"
PORT = 8000

os.system('cls')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    s.listen()
    logging.info(f"Server is listening on {HOST}:{PORT}")
    print(f"Server is listening on {HOST}:{PORT}")

    conn_db = sqlite3.connect('database.db')
    conn_db.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT NOT NULL,
                  password TEXT NOT NULL);''')

    while True:
        conn_socket, addr = s.accept()
        with conn_socket:
            logging.info(f"Connected by {addr}")
            print(f"Connected by {addr}")

            while True:
                try:
                    # Receive data from the client
                    data = conn_socket.recv(2048)

                    if not data:
                        break
                    # Convert the data to a string and split it into parts
                    message = data.decode().strip()
                    parts = message.split()

                    logging.info(f"Received message from client: {message}")
                    print(f"Received message from client: {message}")

                    username = parts[1].lower()
                    password = parts[2]


                    if parts[0] == "register":
                        response = register_user(conn_db, username, password)
                        conn_socket.sendall(response.encode())

                    elif parts[0] == "login":
                        response = login_user(conn_db, username, password)
                        conn_socket.sendall(response.encode())

                    else:
                        logging.warning(f"Invalid message received from client: {message}")
                        print(f"Invalid message received from client: {message}")
                
                except Exception as e:
                    logging.error(f"Exception: {e}")
                    print(f"Exception: {e}")
                    break

            # Close the connection
            conn_socket.close()
