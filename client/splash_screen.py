from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

def display(s, login_func, register_func):
    console = Console()
    title = Panel("[bold]Merchant's Voyage[/]", style="green")
    panel = Panel("[bold]Choose an option:[/]\n[1] Login\n[2] Register", title="Login/Register")
    console.print(panel)

    choice = Prompt.ask("Enter option number")

    while choice not in ["1", "2"]:
        console.print("Invalid choice. Please choose either 1 or 2.")
        choice = Prompt.ask("Enter option number")

    while True:
        if choice == "1":
            # Call the login function
            result = login_func(s)
            if result == "Login successful!":
                console.print(result)
                break
            else:
                # If there was an error logging in, display the error message and show the splash screen again
                console.print(result)
                choice = display(s, login_func, register_func)
        elif choice == "2":
            # Call the register function
            result = register_func(s)
            if result == "Registration successful!":
                # If the registration was successful, show success message and return to splash screen
                console.print(result)
                break
            else:
                # If there was an error registering, display the error message and show the splash screen again
                console.print(result)
                choice = display(s, login_func, register_func)
    
    return choice
