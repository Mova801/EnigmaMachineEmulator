from rich.console import Console

from src.states.state import State


class EnigmaScreen(State):
    _console: Console

    def __init__(self, console: Console):
        self._console = console
        self._stack = list()

    def execute(self) -> None:
        """
        Executes status code.
        :return: None
        """
        self._console.print("Hello World! I am a EnigmaMachineEmulator!", style="bold green")
        usr_in: str = self._console.input("""Enter a option:
- ret: return to main screen
""")
        self._console.clear()
        match usr_in:
            case 'ret':
                self._stack.pop()
