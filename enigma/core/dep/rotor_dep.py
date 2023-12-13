import string

import enigma.core.constants as enigma_const


class Rotor:
    """
    One of the components of the Enigma Machine. Moves a letter by a certain amount. Each time a letter is moved, the
     offset value increases to the maximum, after which it is reset to zero.
    """
    __alphabet: str
    __rotor_alphabet: str
    __rotor_turnover_position: int
    __shift: int

    # __direction: int

    def __init__(self) -> None:
        self.__alphabet = string.ascii_lowercase
        self.__rotor_alphabet = enigma_const.ROTOR_I_ALPHABET

        self.__shift = enigma_const.ROTOR_MIN_OFFSET
        # self.__direction = enigma_const.ROTOR_DEFAULT_DIR

    def set_shift(self, shift: int) -> None:
        """
        Sets a specific offset value, if between the minimum and maximum offset values.
        :param shift: new offset value
        :return: None
        """
        if enigma_const.ROTOR_MIN_OFFSET > shift or shift > enigma_const.ROTOR_MAX_OFFSET:
            raise ValueError(
                f"Invalid shift value: {shift}. "
                f"Must be between {enigma_const.ROTOR_MIN_OFFSET} and {enigma_const.ROTOR_MAX_OFFSET}")
        self.__shift = shift

    def get_shift(self) -> int:
        return self.__shift

    def set_direction(self, direction: int) -> None:
        """
        Sets the direction of the shift.
        :param direction: new shift direction
        :return: None
        """
        if direction >= 0:
            self.__direction = 1
        else:
            self.__direction = -1

    def get_direction(self) -> int:
        return self.__direction

    def inc_shift(self) -> None:
        """
        Increases the offset value by one in the displacement direction. If the maximum value is exceeded, the offset is
        set to the minimum value and vice versa.
        :return: None
        """
        self.__shift += 1 * self.__direction
        if self.__shift > enigma_const.ROTOR_MAX_OFFSET and self.__direction == 1:
            self.__shift = enigma_const.ROTOR_MIN_OFFSET
        elif self.__shift < enigma_const.ROTOR_MIN_OFFSET and self.__direction == -1:
            self.__shift = enigma_const.ROTOR_MAX_OFFSET

    def rotate_letter(self, letter: str) -> str:
        """
        Rotates a letter based on the offset, if valid.
        :param letter: letter to shift
        :return: shifted letter
        """
        letter = letter.lower()
        # checks if letter is in the Rotor alphabet
        letter_index: int = self.__alphabet.find(letter)
        if letter_index == -1:
            raise ValueError(f"Invalid letter {letter}. Only lowercase ascii letters are allowed.")
        return self.__alphabet[letter_index + self.__shift * self.__direction]
