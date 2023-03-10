from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def display():
    console = Console()
    panel = Panel("[bold]Choose an option:[/]\n[1] Login\n[2] Register", title="Login/Register")
    console.print(panel)

    choice = Prompt.ask("Enter option number")

    while choice not in ["1", "2"]:
        console.print("Invalid choice. Please choose either 1 or 2.")
        choice = Prompt.ask("Enter option number")

    return choice