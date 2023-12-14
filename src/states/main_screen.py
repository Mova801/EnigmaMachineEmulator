from rich.console import Console

from src.states.state import State
from src.states.enigma_config_screen import EnigmaConfigurationScreen
from src.states.enigma_screen import EnigmaScreen


class MainScreen(State):
    _console: Console

    def __init__(self, console: Console):
        self._console = console
        self._stack = [self]

    def execute(self) -> None:
        """
        Executes status code.
        :return: None
        """
        self._console.print("EnigmaMachineEmulator Main Screen!", style="bold green")
        usr_in: str = self._console.input("""Enter a option:
- conf: config
- enig: enigma
- ext: exit
""")
        self._console.clear()
        match usr_in:
            case 'conf':
                self.push(EnigmaConfigurationScreen(self._console))
            case 'enig':
                self.push(EnigmaScreen(self._console))
            case 'ext':
                exit(0)
