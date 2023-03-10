
import os
import time
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel


console = Console()

game_world = {
    "Genoa": {"Marseille": 4, "Roma": 4, "Palma": 7, "Cagliari": 7},
    "Cagliari": {"Genoa": 7, "Tunis": 1, "Rome": 3},
    "Marseille": {"Genoa": 4, "Palma": 4, "Valencia": 6},
    "Valencia": {"Marseille": 6, "Algiers": 3, "Palma": 1, "Sevilla": 8},
    "Palma": {"Valencia": 1, "Algiers": 1, "Marseille": 4},
    "Sevilla": {"Valencia": 8, "Algiers": 8},
    "Algiers": {"Valencia": 3, "Palma": 1,"Tunis": 3, "Sevilla": 8},
    "Tunis": {"Algiers": 3, "Siracusa": 2, "Malta": 1, "Cagliari": 1},
    "Siracusa": {"Tunis": 2, "Roma": 5, "Malta": 1},
    "Malta": {"Siracusa": 1, "Tunis": 1},
    "Roma": {"Genoa": 4, "Siracusa": 5, "Cagliari": 3},
}

current_location = "Genoa"

def display_nearest_ports():
    nearest_ports = get_nearest_ports()
    panel = Panel.fit(
        f"Where to captain?\n\n"
        + "\n".join(
            f"[{i+1}] {port} - sailing days: {nearest_ports[port]}" for i, port in enumerate(nearest_ports)
        ),
        title=f"{current_location}",
        border_style="yellow",
    )
    console.print(panel)
        
def get_nearest_ports():
    distances = game_world[current_location]
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    nearest_ports = {port: distance for port, distance in sorted_distances}
    return nearest_ports

def choose_port():
    display_nearest_ports()
    selection = int(input("> "))
    nearest_ports = get_nearest_ports()
    next_port = list(nearest_ports.keys())[selection-1]
    sailing_days = nearest_ports[next_port]
    return next_port, sailing_days

while True:
    os.system('cls')
    next_port, sailing_days = choose_port()

    with Progress() as progress:
        task = progress.add_task(f"Sailing from {current_location} to {next_port}", total=sailing_days)
        while not progress.finished:
            progress.update(task, advance=0.2)
            time.sleep(0.3)

    current_location = next_port

