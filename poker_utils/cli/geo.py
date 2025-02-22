import typer
from rich.console import Console
from rich.table import Table

console = Console()

def geo_cmd(
    pot: float = typer.Argument(..., help="Initial pot size"),
    stack: float = typer.Argument(..., help="Remaining stack size"),
    streets: int = typer.Argument(..., help="Number of streets (2 or 3)", min=2, max=3),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed calculations"),
) -> None:
    """Calculate geometric betting sizes."""
    e = 0.5 * (((pot + 2 * stack) / pot) ** (1 / streets) - 1)
    
    table = Table(title="Geometric Betting Calculation")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="green")
    
    table.add_row("Geometric ratio", f"{e:.3f}")
    table.add_row("First bet", f"{e * pot:.2f}")
    
    if verbose:
        p = pot
        s = stack
        console.print("\nDetailed progression:")
        
        progress = Table(show_header=True)
        progress.add_column("Street")
        progress.add_column("Bet", justify="right")
        progress.add_column("Pot", justify="right")
        progress.add_column("Stack", justify="right")
        
        progress.add_row(
            "Initial",
            "-",
            f"{p:.2f}",
            f"{s:.2f}",
        )
        
        for i in range(streets):
            b = e * p
            p += 2 * b
            s -= b
            progress.add_row(
                str(i + 1),
                f"{b:.2f}",
                f"{p:.2f}",
                f"{s:.2f}",
            )
        
        console.print(table)
        console.print(progress)
    else:
        console.print(table) 