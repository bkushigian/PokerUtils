from random import randint
from time import sleep
import pyfiglet
import typer
from rich.console import Console
from rich.style import Style

console = Console()

COLORS = [
    Style(color="white"),
    Style(color="red"),
    Style(color="yellow"),
    Style(color="green"),
    Style(color="cyan"),
    Style(color="blue"),
    Style(color="magenta"),
]

def rngs_cmd(
    min_val: int = typer.Option(1, "--min", "-m", help="Minimum value"),
    max_val: int = typer.Option(100, "--max", "-M", help="Maximum value"),
    interval: float = typer.Option(3.0, "--interval", "-i", help="Seconds between numbers"),
    num_colors: int = typer.Option(5, "--colors", "-c", help="Number of colors to use"),
    font: str = typer.Option("doh", "--font", "-f", help="Figlet font to use"),
    history: bool = typer.Option(False, help="Keep history of generated numbers"),
) -> None:
    """Generate continuous random numbers with visual display."""
    try:
        num_colors = min(max(1, num_colors), len(COLORS))
        
        while True:
            num = randint(min_val, max_val)
            color_idx = int(num_colors * (num - min_val) / (max_val - min_val))
            style = COLORS[color_idx]
            
            fig_text = pyfiglet.figlet_format(f"{num:02}", font=font).strip()
            
            if not history:
                console.clear()
            
            console.print(fig_text, style=style)
            sleep(interval)
            
    except KeyboardInterrupt:
        console.print("\nStopped by user") 