import enum

from typing_extensions import Self

import enigma.core.models.rotors_models as models
from enigma.core import constants


class RotorFlags(enum.IntEnum):
    RO = 0
    RP = 1
    RA = 2
    TF = 3


class Rotor:
    """
    One of the components of the Enigma Machine.
    """
    _model: str
    _alphabet: str
    _rotor_alphabet: str
    _turnover_position: int
    _offset: int
    _position: int
    _next_attached_rotor: Self
    _flags: list[bool]
    """
    Flags:

    - RO: rotor offset adjusted (1 if regulated, 0 default setting)
    - RP: rotor starting position adjusted (1 if regulated, 0 default setting)
    - RA: rotor attached (1 if have a rotor attached to it, 0 not attached)
    - TF: turnover flag (1 if active, 0 if not)
    """

    def __init__(self, properties=models.RotorIProperties) -> None:
        self._model = properties.model
        self._alphabet = constants.ALPHABET
        self._rotor_alphabet = properties.alphabet
        self._turnover_position = properties.turnover
        self._offset = constants.ROTOR_MIN_OFFSET  # 0
        self._position = constants.ROTOR_MIN_POSITION  # A
        self._flags = [
            False,  # RO
            False,  # RP
            False,  # RA
            self._turnover_position == self._position  # TF
        ]

    def get_flag(self, flag: RotorFlags) -> bool:
        return self._flags[flag]

    def attach_rotor(self, rotor: Self) -> None:
        if self == rotor:
            raise ValueError("Cannot attach a rotor to itself.")
        self._next_attached_rotor = rotor
        self._flags[RotorFlags.RA] = True

    def check_turnover(self) -> bool:
        self._flags[RotorFlags.TF] = self._turnover_position == self._position
        return self._flags[RotorFlags.TF]

    def rotate(self) -> None:
        self._position += 1
        if self._position > constants.ROTOR_MAX_POSITION:
            self._position = constants.ROTOR_MIN_POSITION
        if self._position < constants.ROTOR_MIN_POSITION:
            self._position = constants.ROTOR_MAX_POSITION
        if self.check_turnover() and self._flags[RotorFlags.RA]:
            self._next_attached_rotor.rotate()

    def set_alphabet_ring_position(self, offset: int) -> None:
        if offset > constants.ROTOR_MAX_OFFSET or offset < constants.ROTOR_MIN_OFFSET:
            raise ValueError(f"Offset must be between {constants.ROTOR_MIN_OFFSET} and {constants.ROTOR_MAX_OFFSET}")
        self._offset = offset
        self._flags[RotorFlags.RO] = True

    def set_starting_position(self, position: str) -> None:
        pos_index: int = constants.ALPHABET.find(position) + 1
        if pos_index > constants.ROTOR_MAX_POSITION or pos_index < constants.ROTOR_MIN_POSITION:
            raise ValueError(
                f"Position must be between {constants.ROTOR_MIN_POSITION}"
                f" and {constants.ROTOR_MAX_POSITION}, received {pos_index}")
        self._position = pos_index
        self._flags[RotorFlags.RP] = True

    def _swap(self, letter: str, alphabet1: str, alphabet2: str) -> str:
        """
        Swaps a letter from alphabet1 to alphabet2.
        :param letter: letter to swap
        :param alphabet1: given letter alphabet
        :param alphabet2: swapped letter alphabet
        :return: swapped letter
        """
        letter = letter.upper()
        letter_index: int = alphabet1.find(letter)
        if letter_index == -1:
            raise ValueError(
                f"Invalid letter {letter}. Only letters that belong to the 26-letters alphabet are allowed.")
        swapped_letter_index: int = letter_index % len(alphabet1)
        return alphabet2[(swapped_letter_index + self._offset) % len(alphabet2)]

    def swap_letter(self, letter: str) -> str:
        """
        Swaps a letter from the 26-letters alphabet into the rotor alphabet.
        :param letter: letter to swap. Only letters that belong to the 26-letters alphabet are allowed
        :return: swapped letter
        """
        letter_index: int = self._alphabet.find(letter) + self._position
        rotated_letter: str = self._alphabet[letter_index % len(self._alphabet)]
        return self._swap(rotated_letter, self._alphabet, self._rotor_alphabet)

    def _reverse_swap(self, letter: str) -> str:
        """
        Swaps a letter from alphabet1 to alphabet2.
        :param letter: letter to swap
        :return: swapped letter
        """
        alphabet_len: int = len(self._alphabet)
        rotor_alphabet_len: int = len(self._rotor_alphabet)
        letter = letter.upper()
        letter_index: int = self._rotor_alphabet.find(letter)
        if letter_index == -1:
            raise ValueError(
                f"Invalid letter {letter}. Only letters that belong to the 26-letters alphabet are allowed.")
        swapped_letter_index: int = letter_index % alphabet_len
        return self._alphabet[(swapped_letter_index - self._offset) % rotor_alphabet_len]

    def reverse_swap_letter(self, letter) -> str:
        """
        Reverses the swap of a letter from rotor alphabet into the 26-letters alphabet.
        :param letter: letter to reverse. Only letters that belong to the 26-letters alphabet are allowed
        :return: reversed letter
        """
        rev_letter: str = self._reverse_swap(letter)
        letter_index: int = self._alphabet.find(rev_letter) - self._position
        return self._alphabet[letter_index % len(self._alphabet)]
