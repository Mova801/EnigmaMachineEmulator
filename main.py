# Script created by Marte on 09/12/2023
from rich.traceback import install

from src.cmdapplication import CmdApplication

install()  # better looking error print


def main() -> None:
    app = CmdApplication()
    app.run()


if __name__ == '__main__':
    main()
