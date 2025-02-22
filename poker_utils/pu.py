#!/usr/bin/env python3

from argparse import ArgumentParser
from .cli.mdf import MdfCommand
from .cli.geo import GeoCommand
from .cli.rng import RngCommand
from .cli.rngs import RngsCommand


def main():
    commands = [MdfCommand, GeoCommand, RngCommand, RngsCommand]
    
    parser = ArgumentParser(description="Poker utilities command line tool")
    subparsers = parser.add_subparsers(dest="command")
    
    # Register all commands
    for command_class in commands:
        subparser = subparsers.add_parser(command_class.name, help=command_class.help)
        command_class.add_arguments(subparser)
    
    args = parser.parse_args()
    
    # Default to rngs if no command provided
    if args.command is None:
        args.command = "rngs"
        # Set default args for rngs command
        for action in subparsers.choices["rngs"]._actions:
            if not hasattr(args, action.dest):
                setattr(args, action.dest, action.default)
    
    # Find and execute the appropriate command
    for command_class in commands:
        if command_class.name == args.command:
            result = command_class.execute(args)
            if result.error:
                print(f"Error: {result.error}")
                return 1
            print(result.message)
            return 0
    
    print(f"Unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    main()
