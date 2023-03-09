from rich.prompt import Prompt

def login(s):
    # Get user input for username and password
    username = Prompt.ask("Enter username")
    password = Prompt.ask("Enter password")

    # Send the choice and user input to the server
    message = f"login {username} {password}"
    print(f"Sending message to server: {message}")  # debugging statement
    s.sendall(message.encode())

    # Wait for response from server
    data = s.recv(2048)

    # Print the response from server
    print(data.decode())

    # If the response is "login successful", return True
    if data.decode() == "Login successful!":
        return True
    else:
        print(data.decode())
        return False
