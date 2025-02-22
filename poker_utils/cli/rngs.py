from argparse import ArgumentParser
from random import randint
from time import sleep
import pyfiglet
from .base import Command, CommandResult


class RngsCommand(Command):
    name = "rngs"
    help = "Generate continuous random numbers with visual display"

    COLORS = [
        "\033[97m",  # white
        "\033[91m",  # red
        "\033[93m",  # yellow
        "\033[32m",  # green
        "\033[96m",  # cyan
        "\033[94m",  # blue
        "\033[95m",  # magenta
    ]

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
        parser.add_argument(
            "--interval",
            "-i",
            type=float,
            default=3.0,
            help="Seconds between numbers (default: 3.0)"
        )
        parser.add_argument(
            "--colors",
            "-c",
            type=int,
            default=5,
            help="Number of colors to use (default: 5)"
        )
        parser.add_argument(
            "--font",
            "-f",
            default="doh",
            help="Figlet font to use (default: doh)"
        )
        parser.add_argument(
            "--mouse",
            action="store_true",
            help="Generate numbers on mouse click"
        )
        parser.add_argument(
            "--history",
            action="store_true",
            help="Keep history of generated numbers"
        )

    @classmethod
    def execute(cls, args) -> CommandResult:
        try:
            if args.mouse:
                return cls._run_mouse_mode(args)
            else:
                return cls._run_continuous_mode(args)
        except KeyboardInterrupt:
            return CommandResult(message="\nStopped by user")

    @classmethod
    def _run_continuous_mode(cls, args):
        num_colors = min(max(1, args.colors), len(cls.COLORS))
        last_lines = 0
        
        while True:
            num = randint(args.min, args.max)
            color_idx = int(num_colors * (num - args.min) / (args.max - args.min))
            color = cls.COLORS[color_idx]
            
            fig_text = pyfiglet.figlet_format(f"{num:02}", font=args.font).strip()
            
            if last_lines and not args.history:
                print("\033[F" * last_lines, end="")
            
            output = f"\n{color}{fig_text}\033[0m"
            print(output, end="", flush=True)
            last_lines = output.count("\n") + 1
            
            sleep(args.interval)

    @classmethod
    def _run_mouse_mode(cls, args):
        try:
            import mouse
        except ImportError:
            return CommandResult(
                error="Mouse mode requires the 'mouse' package. Install with: pip install mouse"
            )

        color_idx = 0
        num_colors = min(max(1, args.colors), len(cls.COLORS))

        def on_click(x, y, button, pressed):
            nonlocal color_idx
            if pressed:
                num = randint(args.min, args.max)
                color = cls.COLORS[color_idx]
                print(f"\n{color}{num}\033[0m", end="", flush=True)
                color_idx = (color_idx + 1) % num_colors
            return True

        with mouse.Listener(on_click=on_click) as listener:
            print("Click anywhere to generate numbers (Ctrl+C to exit)")
            listener.join() 