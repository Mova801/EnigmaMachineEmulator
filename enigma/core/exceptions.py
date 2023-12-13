from typing import Any


class EnigmaMachineEmulatorException(Exception):
    """Base class for exceptions in the EnigmaMachine project."""

    def __init__(self, msg: str = "", val: Any = None, *args) -> None:
        super().__init__(*args)
        self.message = "EnigmaMachineEmulator exception."
        self.value = None
        if msg:
            self.message = msg
        if val is not None:
            self.value = val

    def __str__(self) -> str:
        return self.message + ' ' + self.value


class MissingRotorsException(EnigmaMachineEmulatorException):
    """Exception raised when no rotors are passed in the constructor."""

    def __init__(self, msg: str = "", val: Any = None, *args) -> None:
        super().__init__(*args)
        self.message: str = "rotors absent in constructor."
        self.value = None
        if msg:
            self.message = msg
        if val is not None:
            self.value = val

    def __str__(self) -> str:
        return self.message + ' ' + self.value


class InvalidRotorsNumberException(EnigmaMachineEmulatorException):
    """Exception raised when the number of rotors passed is not correct."""

    def __init__(self, msg: str = "", val: Any = None, *args) -> None:
        super().__init__(*args)
        self.message: str = "invalid rotors number."
        self.value = None
        if msg:
            self.message = msg
        if val is not None:
            self.value = val

    def __str__(self) -> str:
        return self.message + ' ' + self.value


class RotorsNotAttachedException(EnigmaMachineEmulatorException):
    """Exception raised when the number of rotors is greater than one, but they are not correctly attached."""

    def __init__(self, msg: str = "", val: Any = None, *args) -> None:
        super().__init__(*args)
        self.message: str = "rotors not attached."
        self.value = None
        if msg:
            self.message = msg
        if val is not None:
            self.value = val

    def __str__(self) -> str:
        return self.message + ' ' + self.value
