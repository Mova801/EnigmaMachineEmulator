from enigma.core import constants
import enigma.core.models.reflectors_models as models


class Reflector:
    _input: str
    _output: str

    def __init__(self, pairs: models.ReflectorProperties = None) -> None:
        self._input = ""
        self._output = ""
        if pairs is not None:
            self.set_pairs(pairs)

    def set_pairs(self, pairs: list[str]) -> None:
        """
        Set the correspondence between each letter of the alphabet.
        :param pairs: list of pairs to set. Only pairs of letters that belong to the 26-letters alphabet are allowed
        :return: None
        """
        pairs_cpy: list[str] = pairs.copy()
        if len(pairs) != constants.ALPHABET_LENGTH // 2:
            raise ValueError(
                f"Reflector needs {constants.ALPHABET_LENGTH // 2} pairs for the set up: {len(pairs)} passed")
        for pair in pairs_cpy:
            # checks for invalid pair: length different from 2
            if len(pair) != 2:
                raise ValueError(f"Invalid pair: {pair}. Pairs must contain exactly two letters.")
            pair = pair.upper()
            # checks for invalid pair: contains characters other than letters
            if pair[0] not in constants.ALPHABET or pair[1] not in constants.ALPHABET:
                raise ValueError(f"Invalid pair: {pair}. Pairs must contain only two letters.")
            # checks for invalid pair: letter already registered in the reflector
            # noinspection DuplicatedCode
            if pair[0] in self._input or pair[1] in self._input or pair[0] in self._output or pair[1] in self._output:
                raise ValueError(f"Pairs cannot contain duplicates. A letter must appear only once per configuration.")
            self._input += pair
            self._output += pair[1] + pair[0]

    def reflect(self, letter: str) -> str:
        """
        Reflect the incoming letter using the correspondence.
        :param letter: letter to reflect. Only letters that belong to the 26-letters alphabet are allowed
        :return: reflected letter
        """
        letter = letter.upper()
        letter_index: int = self._input.find(letter)
        if letter_index == -1:
            raise ValueError(f"Invalid letter {letter}. Only letter that belong to the 26-letters alphabet are allowed")
        return self._output[letter_index]
