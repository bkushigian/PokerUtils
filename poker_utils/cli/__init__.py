"""Command-line interface package for poker utilities."""
import typer
from rich.console import Console

app = typer.Typer(
    help="Poker utilities command line tool",
    no_args_is_help=True,  # Show help when no command is specified
)
console = Console()

# Import commands after creating app to avoid circular imports
from .mdf import mdf
from .geo import e, e2, e3
from .rng import rng
from .rngs import rngs

# Register commands
app.command()(mdf)
app.command()(e)
app.command()(e2)
app.command()(e3)
app.command()(rng)
app.command()(rngs) 