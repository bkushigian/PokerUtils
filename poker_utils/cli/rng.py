from random import randint
import typer
from rich.console import Console

console = Console()

def rng_cmd(
    min_val: int = typer.Option(1, "--min", "-m", help="Minimum value"),
    max_val: int = typer.Option(100, "--max", "-M", help="Maximum value"),
) -> None:
    """Generate a random number."""
    number = randint(min_val, max_val)
    console.print(number, style="bold green") 