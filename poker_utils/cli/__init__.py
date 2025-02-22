"""Command-line interface package for poker utilities."""
import typer
from rich.console import Console

app = typer.Typer(
    help="Poker utilities command line tool",
    no_args_is_help=False,  # Allow running without subcommand
)
console = Console()

# Import commands after creating app to avoid circular imports
from .mdf import mdf_cmd
from .geo import geo_cmd
from .rng import rng_cmd
from .rngs import rngs_cmd

# Register commands
app.command()(mdf_cmd)
app.command()(geo_cmd)
app.command()(rng_cmd)
app.command()(rngs_cmd)

# Set default command
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Run default command (rngs) if no command specified."""
    if ctx.invoked_subcommand is None:
        # Call rngs_cmd with default values
        rngs_cmd(
            min_val=1,
            max_val=100,
            interval=3.0,
            num_colors=5,
            font="doh",
            history=False
        ) 