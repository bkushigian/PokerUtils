import typer
from rich.console import Console
from rich.table import Table

console = Console()

def _calculate_geo(pot: float, stack: float, streets: int, verbose: bool) -> tuple[float, Table, Table | None]:
    """Common geometric betting calculation logic."""
    e = 0.5 * (((pot + 2 * stack) / pot) ** (1 / streets) - 1)
    
    table = Table(title=f"{streets}-Street Geometric Betting")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="green")
    
    table.add_row("Geometric ratio", f"{e:.3f}")
    table.add_row("First bet", f"{e * pot:.2f}")
    
    progress = None
    if verbose:
        p = pot
        s = stack
        
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
    
    return e, table, progress

def e(
    pot: float = typer.Argument(..., help="Initial pot size"),
    stack: float = typer.Argument(..., help="Remaining stack size"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed calculations"),
) -> None:
    """Calculate both 2-street and 3-street geometric betting sizes."""
    console.print("\n[bold]2-Street Betting:[/bold]")
    e2, table2, progress2 = _calculate_geo(pot, stack, 2, verbose)
    console.print(table2)
    if progress2:
        console.print(progress2)
    
    console.print("\n[bold]3-Street Betting:[/bold]")
    e3, table3, progress3 = _calculate_geo(pot, stack, 3, verbose)
    console.print(table3)
    if progress3:
        console.print(progress3)

def e2(
    pot: float = typer.Argument(..., help="Initial pot size"),
    stack: float = typer.Argument(..., help="Remaining stack size"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed calculations"),
) -> None:
    """Calculate 2-street geometric betting sizes."""
    _, table, progress = _calculate_geo(pot, stack, 2, verbose)
    console.print(table)
    if progress:
        console.print(progress)

def e3(
    pot: float = typer.Argument(..., help="Initial pot size"),
    stack: float = typer.Argument(..., help="Remaining stack size"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed calculations"),
) -> None:
    """Calculate 3-street geometric betting sizes."""
    _, table, progress = _calculate_geo(pot, stack, 3, verbose)
    console.print(table)
    if progress:
        console.print(progress) 