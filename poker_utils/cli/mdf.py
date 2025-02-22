from argparse import ArgumentParser
from .base import Command, CommandResult


class MdfCommand(Command):
    name = "mdf"
    help = "Calculate minimum defense frequency"

    @classmethod
    def add_arguments(cls, parser: ArgumentParser) -> None:
        parser.add_argument("pot", type=float, help="Current pot size")
        parser.add_argument("bet", type=float, help="Bet size")
        parser.add_argument(
            "--freq", 
            type=float, 
            help="Actual defense frequency (as percentage)"
        )

    @classmethod
    def execute(cls, args) -> CommandResult:
        mdf_value = args.pot / (args.pot + args.bet)
        result = [f"MDF: {mdf_value * 100:.1f}%"]
        
        if args.freq is not None:
            freq = args.freq / 100.0
            if freq < mdf_value:
                freq_delta = mdf_value - freq
                mistake_size = freq_delta * args.pot
                result.extend([
                    f"Under-defending by {freq_delta * 100:.1f}%",
                    f"Mistake size: {mistake_size:.2f} chips"
                ])
        
        return CommandResult(message="\n".join(result)) 