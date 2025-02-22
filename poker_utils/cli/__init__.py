"""Command-line interface package for poker utilities."""
import typer
from rich.console import Console

app = typer.Typer(
    help="Poker utilities command line tool",
    no_args_is_help=False,  # Allow running without subcommand
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

# Set default command
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Run default command (rngs) if no command specified."""
    if ctx.invoked_subcommand is None:
        rngs(
            min_val=1,
            max_val=100,
            interval=3.0,
            num_colors=5,
            font="doh",
            history=False
        ) 