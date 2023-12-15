from typing import Callable


class Command:
    """"""
    _short_name: str
    _extended_name: str
    _description: str
    _command: Callable

    def __init__(self, short_name: str, extended_name: str, description: str, function: Callable) -> None:
        self._short_name = short_name.lower().strip()
        self._extended_name = extended_name.lower().strip()
        self._description = description
        self._command = function
