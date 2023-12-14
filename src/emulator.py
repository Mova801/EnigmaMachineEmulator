from rich.console import Console

from src.states.main_screen import MainScreen
from src.states.state import State


class EnigmaEmulator:
    """"""
    _status_LIFO_stack: State
    _console: Console
    _running: bool

    def __init__(self) -> None:
        self._console = Console()
        self._status_LIFO_stack = MainScreen(self._console)
        self._running = True

    def run(self) -> None:
        while self._running:
            self._status_LIFO_stack[-1].execute()
