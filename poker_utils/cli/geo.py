from argparse import ArgumentParser
from .base import Command, CommandResult


class GeoCommand(Command):
    name = "geo"
    help = "Calculate geometric betting sizes"

    @classmethod
    def add_arguments(cls, parser: ArgumentParser) -> None:
        parser.add_argument("pot", type=float, help="Initial pot size")
        parser.add_argument("stack", type=float, help="Remaining stack size")
        parser.add_argument(
            "streets",
            type=int,
            choices=[2, 3],
            help="Number of streets (2 or 3)"
        )
        parser.add_argument(
            "--verbose", 
            "-v", 
            action="store_true",
            help="Show detailed calculations"
        )

    @classmethod
    def execute(cls, args) -> CommandResult:
        e = 0.5 * (((args.pot + 2 * args.stack) / args.pot) ** (1 / args.streets) - 1)
        result = [f"Geometric ratio: {e:.3f}", f"First bet: {e * args.pot:.2f}"]
        
        if args.verbose:
            p = args.pot
            s = args.stack
            result.append(f"\nDetailed progression:")
            result.append(f"Initial - Pot: {p:.2f}, Stack: {s:.2f}")
            
            for i in range(args.streets):
                b = e * p
                p += 2 * b
                s -= b
                result.append(f"Street {i+1} - Bet: {b:.2f}, Pot: {p:.2f}, Stack: {s:.2f}")
        
        return CommandResult(message="\n".join(result)) 