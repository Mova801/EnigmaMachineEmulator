# Script created by Marte on 09/12/2023
from rich.traceback import install

from src import cmd_emulator

install()  # better looking error print


def main() -> None:
    cmd_emulator.emu()


if __name__ == '__main__':
    main()
