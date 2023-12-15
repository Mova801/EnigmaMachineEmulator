from rich.console import Console
from rich.prompt import Prompt
from rich.pretty import pprint

from src.states.state import State
from src.states.enigma_config_screen import EnigmaConfigurationScreen
from src.states.enigma_screen import EnigmaScreen
from src.commands.command import Command


class MainScreen(State):
    _console: Console

    def __init__(self, console: Console, prompt: Prompt) -> None:
        self._console = console
        self._prompt = prompt
        self._stack = [self]

    def _handle_user_input(self) -> None:
        """

        :return:
        """
        # User input segment
        usr_in: str = self._prompt.ask(
            "Enter an option",
            show_default=True,
            console=self._console,
            choices=['conf', 'enig', 'ext']
        )
        self._console.clear()
        match usr_in:
            case 'conf':
                self.push(EnigmaConfigurationScreen(self._console, self._prompt))
            case 'enig':
                self.push(EnigmaScreen(self._console, self._prompt))
            case 'ext':
                exit(0)

    def execute(self) -> None:
        """
        Executes status code.
        :return: None
        """
        self._console.print("EnigmaMachineEmulator Main Screen!", style="bold green")
        self._handle_user_input()
