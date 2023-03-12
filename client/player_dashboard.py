from rich.console import Console
from rich.panel import Panel

def display_dashboard(player):
    console = Console()

    # Construct the dashboard panel
    panel = Panel(f"[bold]Welcome, {player.username}![/] Location: {player.location}   Gold: {player.gold}   Cargo: {player.cargo}", title="[bold]Merchant's Voyage[/]")

    console.print(panel)
