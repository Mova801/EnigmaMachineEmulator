from rich.console import Console
from rich.prompt import Prompt

from src.states.state import State


class EnigmaScreen(State):
    _console: Console

    def __init__(self, console: Console, prompt: Prompt):
        self._console = console
        self._prompt = prompt
        self._stack = list()

    def execute(self) -> None:
        """
        Executes status code.
        :return: None
        """
        self._console.print("Hello World! I am a EnigmaMachineEmulator!", style="bold green")
        usr_in: str = self._prompt.ask("Enter an option", console=self._console, choices=['ret'])
        self._console.clear()
        match usr_in:
            case 'ret':
                self._stack.pop()
