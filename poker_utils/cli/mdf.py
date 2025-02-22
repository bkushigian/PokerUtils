import typer
from rich.console import Console
from rich.table import Table

console = Console()

def mdf_cmd(
    pot: float = typer.Argument(..., help="Current pot size"),
    bet: float = typer.Argument(..., help="Bet size"),
    freq: float = typer.Option(None, help="Actual defense frequency (as percentage)")
) -> None:
    """Calculate minimum defense frequency."""
    mdf_value = pot / (pot + bet)
    
    table = Table(title="MDF Calculation")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="green")
    
    table.add_row("MDF", f"{mdf_value * 100:.1f}%")
    
    if freq is not None:
        freq = freq / 100.0
        if freq < mdf_value:
            freq_delta = mdf_value - freq
            mistake_size = freq_delta * pot
            table.add_row("Defense Frequency", f"{freq * 100:.1f}%")
            table.add_row("Under-defending by", f"{freq_delta * 100:.1f}%")
            table.add_row("Mistake size", f"{mistake_size:.2f} chips")
    
    console.print(table) 