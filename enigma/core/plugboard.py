from enigma.core import constants


class Plugboard:
    """
    One of the components of the Enigma Machine. Consists of a table in which specific outgoing letters can be set as a
    result of specific incoming letters.
    E.g:
        T -> Plugboard -> J
    """
    _input: str
    _output: str

    def __init__(self, pairs: list[str] = None) -> None:
        self._input = ""
        self._output = ""
        if pairs is not None:
            self.set_plugboard(pairs)

    def set_plugboard(self, pairs: list[str]) -> None:
        """
        Set the correspondence between letters of the alphabet.
        :param pairs: list of pairs to set. Only pairs of letters that belong to the 26-letters alphabet are allowed
        :return: None
        """
        pairs_cpy: list[str] = pairs.copy()
        for pair in pairs_cpy:
            pair = pair.upper()
            # checks for invalid pair: length different from 2
            if len(pair) != 2:
                raise ValueError(f"Invalid pair '{pair}'. Pairs must contain exactly two letters.")
            # checks for invalid pair: contains characters other than letters
            if pair[0] not in constants.ALPHABET or pair[1] not in constants.ALPHABET:
                raise ValueError(f"Invalid pair '{pair}'. Pairs can contain only letters.")
            pair = pair.upper()
            # checks for invalid pair: letter already registered in the reflector
            # noinspection DuplicatedCode
            if pair[0] in self._input or pair[1] in self._input or pair[0] in self._output or pair[1] in self._output:
                raise ValueError(f"Invalid pair '{pair}'."
                                 f" Pairs cannot contain duplicates. A letter must appear only once per configuration.")
            self._input += pair
            self._output += pair[1] + pair[0]

    def exchange(self, letter: str) -> str:
        """
        Reflect the incoming letter using the correspondence.
        If the letter is not registered than is returned unaltered.
        :param letter: letter to reflect. Only letters that belong to the 26-letters alphabet are allowed
        :return: reflected letter
        """
        letter = letter.upper()
        if letter not in constants.ALPHABET:
            raise ValueError(
                f"Invalid letter '{letter}'. Only letter that belong to the 26-letters alphabet are allowed")
        letter_index: int = self._input.find(letter)
        if letter_index == -1:
            return letter
        return self._output[letter_index]

    def clear(self) -> None:
        """
        Clears the plugboard settings.
        :return: None
        """
        self._input = ""
        self._output = ""
