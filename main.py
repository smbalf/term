from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import socket
import os


os.system('cls')

# Define host and port for the server
HOST = '127.0.0.1'
PORT = 65430

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

    console = Console()

    # Create a panel with the login and register options
    panel = Panel("[bold]Choose an option:[/]\n[1] Login\n[2] Register", title="Login/Register")

    while True:
        console.print(panel)

        # Get user input for login or register
        choice = Prompt.ask("Enter option number")

        if choice == "1":
            # Get user input for username and password
            username = Prompt.ask("Enter username")
            password = Prompt.ask("Enter password")

            # Send the choice and user input to the server
            message = f"login {username} {password}"
            print(f"Sending message to server: {message}")  # debugging statement
            s.sendall(message.encode())

            # Wait for response from server
            data = s.recv(1024)

            # Print the response from server
            console.print(data.decode())

            # If the response is "Login successful!", exit the loop and close the connection
            if data.decode() == "Login successful!":
                break
        elif choice == "2":
            # Get user input for username and password
            username = Prompt.ask("Enter username")
            password = Prompt.ask("Enter password")

            # Send the choice and user input to the server
            message = f"register {username} {password}"
            print(f"Sending message to server: {message}")  # debugging statement
            s.sendall(message.encode())

            # Wait for response from server
            data = s.recv(1024)

            try:
                # Try to decode the response
                response = data.decode()

                # If the response is "Closing connection", exit the loop and close the connection
                if response == "Closing connection":
                    break

                # Print the response from server
                console.print(response)

            except:
                # If there was an error decoding the response, print a user-friendly error message
                console.print("There was an error registering the account. Please try again with a different username.")

        else:
            console.print("Invalid choice. Please choose either 1 or 2.")

    # Close the connection
    s.close()
