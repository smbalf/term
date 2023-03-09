from rich.console import Console
import socket
import os
from player_login import login
from player_register import register
from splash_screen import display


os.system('cls')

# Define host and port for the server
HOST = '127.0.0.1'
PORT = 8000

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

    # Display the splash screen and get the user's choice
    choice = display()

    console = Console()

    while True:
        if choice == "1":
            # Call the login function
            result = login(s)
            if result == "Login successful!":
                console.print(result)
                choice = display()
            else:
                # If there was an error logging in, display the error message and show the splash screen again
                console.print(result)
                choice = display()
        elif choice == "2":
            # Call the register function
            result = register(s)
            if result == "Registration successful!":
                # If the registration was successful, show success message and return to splash screen
                console.print(result)
                choice = display()
            else:
                # If there was an error registering, display the error message and show the splash screen again
                console.print(result)
                choice = display()

        # Close the connection
        s.close()
