from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Optional


@dataclass
class CommandResult:
    """Represents the result of a command execution"""
    message: str
    error: Optional[str] = None


class Command:
    """Base class for all commands"""
    name = ""
    help = ""

    @classmethod
    def add_arguments(cls, parser: ArgumentParser) -> None:
        """Add command-specific arguments to parser"""
        pass

    @classmethod
    def execute(cls, args) -> CommandResult:
        """Execute the command with given arguments"""
        raise NotImplementedError 