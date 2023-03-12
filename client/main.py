from rich.console import Console
import socket
import os
from player_login import login
from player_register import register
from splash_screen import splash
from player_dashboard import display_dashboard



os.system('cls')

# Define host and port for the server
HOST = '127.0.0.1'
PORT = 8000

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    console = Console()

    # Display the splash screen and get the user's choice
    choice = splash()

    while True:
        if choice == "1":
            result = login(s)
            if result == "Login successful!":
                pass
                # RUN THE ACTUAL GAME
            else:
                # If there was an error logging in, display the error message and show the splash screen again
                console.print(result)
                choice = splash()
        elif choice == "2":
            result = register(s)
            if result == "Registration successful!":
                pass
                # CODE HERE TO LOG THE NEWLY REGISTERED PLAYER IN
                # RUN THE ACTUAL GAME
            else:
                # If there was an error registering, display the error message and show the splash screen again
                console.print(result)
                choice = splash()
