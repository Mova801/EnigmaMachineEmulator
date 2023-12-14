# Script created by Marte on 09/12/2023
from rich.traceback import install

from src.emulator import EnigmaEmulator

install()  # better looking error print


def main() -> None:
    emu = EnigmaEmulator()
    emu.run()


if __name__ == '__main__':
    main()
