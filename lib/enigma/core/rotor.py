import enum
from typing import Self

from ..models import rotors_models as models
import constants


class RotorFlags(enum.IntEnum):
    """Flags used by rotor."""
    RO = 0
    "RO: rotor offset adjusted (1 if regulated, 0 use default setting)"
    RP = 1
    "RP: rotor starting position adjusted (1 if regulated, 0 use default setting)"
    RA = 2
    "RA: rotor attached (1 if have a rotor attached to it, 0 not attached)"
    TF = 3
    "TF: turnover flag (1 if active, 0 if not)"


class Rotor:
    """
    One of the components of the Enigma Machine.
    """
    _model: str
    "Rotor model. Each model is characterized by a specific scrambling of letters."
    _alphabet: str
    "26-letters alphabet."
    _rotor_alphabet: str
    "Rotor alphabet. Rotor scrambling of letters."
    _turnover_position: int
    "Rotation position of the attached rotor."
    _offset: int
    "Rotor static letters offset."
    _position: int
    "Rotor dynamic offset."
    _next_attached_rotor: Self
    "Attached rotor. When the turnover position of the first rotor is reached, this rotor rotate."
    _flags: list[bool]
    """
    Rotor flags:

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
        self._offset = constants.ROTOR_MIN_OFFSET  # 1
        self._position = constants.ROTOR_MIN_POSITION  # A
        self._flags = [
            False,  # RO
            False,  # RP
            False,  # RA
            self._turnover_position == self._position  # TF
        ]

    def get_flag(self, flag: RotorFlags) -> bool:
        """
        Returns the value of a specific rotor flag.
        :param flag: flag of which to return the value
        :return: required flag value
        """
        return self._flags[flag]

    def attach_rotor(self, rotor: Self) -> None:
        """
        Attaches a rotor to the current rotor.
        :param rotor: rotor to attach
        :return: None
        """
        if self == rotor:
            raise ValueError("Cannot attach a rotor to itself.")
        self._next_attached_rotor = rotor
        self._flags[RotorFlags.RA] = True

    def check_turnover(self) -> bool:
        """
        Update the turnover-flag of the rotor and returns its value.
        :return: TF value
        """
        self._flags[RotorFlags.TF] = self._turnover_position == self._position
        return self._flags[RotorFlags.TF]

    def rotate(self) -> None:
        """
        Rotates the rotor. If the turnover kicks-in the attached rotor also rotated, if any.
        :return: None
        """
        self._position += 1
        if self._position > constants.ROTOR_MAX_POSITION:
            self._position = constants.ROTOR_MIN_POSITION
        if self._position < constants.ROTOR_MIN_POSITION:
            self._position = constants.ROTOR_MAX_POSITION
        if self.check_turnover() and self._flags[RotorFlags.RA]:
            self._next_attached_rotor.rotate()

    def set_alphabet_ring_position(self, offset: int) -> None:
        """
        Sets the position of the alphabet ring position on the rotor. Describes the static offset of each letter of the
        alphabet in relation to the rotor alphabet.
        :param offset: static offset value
        :return: None
        """
        if offset > constants.ROTOR_MAX_OFFSET or offset < constants.ROTOR_MIN_OFFSET:
            raise ValueError(f"Offset must be between {constants.ROTOR_MIN_OFFSET} and {constants.ROTOR_MAX_OFFSET}")
        self._offset = offset
        self._flags[RotorFlags.RO] = True

    def set_starting_position(self, position: str) -> None:
        """
        Sets the starting position of the rotor. Describes the dynamic offset of each letter of the
        alphabet in relation to the rotor alphabet. This offset updates with each rotation, so that if the same letter
        is pressed multiple times (e.g., twice) the rotor will output a different letter.
        :param position: starting position of the rotor
        :return: None
        """
        pos_index: int = constants.ALPHABET.find(position) + 1
        if pos_index > constants.ROTOR_MAX_POSITION or pos_index < constants.ROTOR_MIN_POSITION:
            raise ValueError(
                f"Position must be between {constants.ROTOR_MIN_POSITION}"
                f" and {constants.ROTOR_MAX_POSITION}, received {pos_index}")
        self._position = pos_index
        self._flags[RotorFlags.RP] = True

    def swap_letter(self, letter: str) -> str:
        """
        Swaps a letter from the 26-letters alphabet into the rotor alphabet.
        :param letter: letter to swap. Only letters that belong to the 26-letters alphabet are allowed
        :return: swapped letter
        """
        alphabet_len: int = len(self._alphabet)
        rotor_alphabet_len: int = len(self._rotor_alphabet)
        letter = letter.upper()
        letter_index: int = self._alphabet.find(letter) + self._position
        rotated_letter: str = self._alphabet[letter_index % len(self._alphabet)]
        rotated_letter_index: int = self._alphabet.find(rotated_letter)
        if rotated_letter_index == -1:
            raise ValueError(
                f"Invalid letter {letter}. Only letters that belong to the 26-letters alphabet are allowed.")
        swapped_letter_index: int = rotated_letter_index % alphabet_len
        return self._rotor_alphabet[(swapped_letter_index + self._offset) % rotor_alphabet_len]

    def reverse_swap_letter(self, letter) -> str:
        """
        Reverses the swap of a letter from rotor alphabet into the 26-letters alphabet.
        :param letter: letter to reverse. Only letters that belong to the 26-letters alphabet are allowed
        :return: reversed letter
        """
        alphabet_len: int = len(self._alphabet)
        rotor_alphabet_len: int = len(self._rotor_alphabet)
        letter = letter.upper()
        letter_index: int = self._rotor_alphabet.find(letter)
        if letter_index == -1:
            raise ValueError(
                f"Invalid letter {letter}. Only letters that belong to the 26-letters alphabet are allowed.")
        swapped_letter_index: int = letter_index % alphabet_len
        rev_letter: str = self._alphabet[(swapped_letter_index - self._offset) % rotor_alphabet_len]
        letter_index: int = self._alphabet.find(rev_letter) - self._position
        return self._alphabet[letter_index % len(self._alphabet)]
