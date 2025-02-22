from argparse import ArgumentParser
from random import randint
from .base import Command, CommandResult


class RngCommand(Command):
    name = "rng"
    help = "Generate random numbers"

    @classmethod
    def add_arguments(cls, parser: ArgumentParser) -> None:
        parser.add_argument(
            "--min", "-m",
            type=int,
            default=1,
            help="Minimum value (default: 1)"
        )
        parser.add_argument(
            "--max", "-M",
            type=int,
            default=100,
            help="Maximum value (default: 100)"
        )

    @classmethod
    def execute(cls, args) -> CommandResult:
        number = randint(args.min, args.max)
        return CommandResult(message=str(number)) 