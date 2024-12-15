from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.pretty import pprint

from src.states.state import State
from src.states.enigma_config_screen import EnigmaConfigurationScreen
from src.states.enigma_screen import EnigmaScreen
from src.commands.command import Command


class MainScreen(State):
    _console: Console
    _prompt: Prompt
    _stack: list[State]
    _commands_short_names: list[str]

    def __init__(self, console: Console, prompt: Prompt) -> None:
        self._console = console
        self._prompt = prompt
        self._stack = [self]
        self._commands_short_names: list[str] = ['conf', 'enig', 'exit']

    def _handle_user_input(self) -> None:
        """

        :return:
        """
        # User input segment
        usr_in: str = self._prompt.ask(
            "Enter an option",
            show_default=True,
            console=self._console,
            choices=self._commands_short_names
        )
        self._console.clear()
        cmd0, cmd1, cmd2 = self._commands_short_names
        match usr_in:
            case str(cmd0):
                self.push(EnigmaConfigurationScreen(self._console, self._prompt))
            case str(cmd1):
                self.push(EnigmaScreen(self._console, self._prompt))
            case cmd2:
                exit(0)

    def execute(self) -> None:
        """
        Executes status code.
        :return: None
        """
        self._console.print(Markdown("# EnigmaMachineEmulator Main Screen!"))
        self._handle_user_input()
