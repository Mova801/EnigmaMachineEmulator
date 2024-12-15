from typing import Any

from core import constants, exceptions
from core.plugboard import Plugboard
from core.reflector import Reflector
from core.rotor import Rotor, RotorFlags
from models import reflectors_models
from models import rotors_models


class EnigmaMachine:
    """
    An Enigma machine is composed by three main components:

    - a plugboard
    - a rotors system (consisting of multiple rotors attached together)
    - a reflector

    Rotors are passed as (right rotor, center rotor, left rotor) and so any type of configuration that requires settings
    for multiple rotors.
    """
    _plugboard: Plugboard
    _rotors: tuple[Rotor, ...]
    _reflector: Reflector

    def __init__(self, **kwargs: Any) -> None:
        # rotors init
        rotors: tuple[Rotor, ...] = kwargs.get('rotors', tuple())
        rot_models: tuple[rotors_models.RotorProperties] = kwargs.get('rotors_models', tuple())
        if len(rotors) == 0 or len(rotors) != constants.ROTOR_NUMBER:
            raise exceptions.MissingRotorsException()
        elif len(rotors) != 0:
            self._rotors = tuple(reversed(rotors))
        elif len(rot_models) == 0 or len(rot_models) != constants.ROTOR_NUMBER:
            raise exceptions.MissingRotorsPropertiesException()
        else:
            self._rotors = tuple([Rotor(prop) for prop in reversed(rot_models)])
        for i in range(constants.ROTOR_NUMBER - 1):
            rotor = self._rotors[i]
            next_rotor = self._rotors[i + 1]
            rotor.attach_rotor(next_rotor)
        # reflector init
        reflector_model: reflectors_models.ReflectorProperties = kwargs.get('reflectors_model',
                                                                            reflectors_models.ReflectorBProperties)
        # if reflector_model is None:
        #     self._reflector = Reflector()
        # else:
        self._reflector = Reflector(reflector_model)
        self._plugboard = Plugboard()

    def set_plugboard(self, pairs: list[str]) -> None:
        """
        Set the plugboard pairs of the Enigma Machine.
        :param pairs: pairs of letters to scramble
        :return: None
        """
        self._plugboard.set_plugboard(pairs)

    def set_rotors(self, rotors: list[Rotor]) -> None:
        """
        Set the rotors of the Enigma Machine. The rotors are handled to be:

        - rotors[0]: right rotor
        - rotors[1]: middle rotor
        - rotors[2]: left rotor
        :param rotors: rotors to set for the Enigma Machine
        :return: None
        """
        if len(rotors) != constants.ROTOR_NUMBER:
            raise exceptions.InvalidRotorsNumberException(
                f"Number of rotors must be {constants.ROTOR_NUMBER}, not",
                len(rotors)
            )
        self._rotors = tuple(*reversed(rotors))

    def set_rotors_position(self, positions: tuple[str, ...]) -> None:
        """
        Set the starting positions of the rotors of the Enigma Machine.
        :param positions: starting positions to set in the rotors
        :return: None
        """
        if len(positions) != constants.ROTOR_NUMBER:
            raise ValueError(
                f"The number of offsets must be equal to rotors number {constants.ROTOR_NUMBER}, not {len(positions)}")
        [self._rotors[i].set_starting_position(pos) for i, pos in enumerate(reversed(positions))]

    def set_alphabet_ring_position(self, offsets: tuple[int, ...]) -> None:
        """
        Set the alphabet ring position for each rotor of the Enigma Machine.
        :param offsets: offsets to set in the rotors
        :return: None
        """
        if len(offsets) != constants.ROTOR_NUMBER:
            raise ValueError(
                f"The number of offsets must be equal to rotors number {constants.ROTOR_NUMBER}, not {len(offsets)}")
        [self._rotors[i].set_alphabet_ring_position(offset) for i, offset in enumerate(reversed(offsets))]

    def set_reflector(self, model: reflectors_models.ReflectorProperties) -> None:
        """
        Set a reflector of the given model in Enigma Machine settings.
        :param model: reflector model to use
        :return: None
        """
        if not isinstance(model, reflectors_models.ReflectorProperties):
            self._reflector = Reflector(model)

    def process_text(self, text: str) -> str:
        """
        Processes a text string with the current Enigma Machine settings and returns the encrypted text.
        :param text: text to process
        :return: encrypted text
        """
        # check if all rotors are attached
        for i in range(constants.ROTOR_NUMBER - 1):
            rotor = self._rotors[i]
            if not rotor.get_flag(RotorFlags.RA) and len(self._rotors) > 1:
                raise exceptions.InvalidRotorsNumberException()

        text = text.upper()
        final_text: str = ""
        # for each letter in the text
        for letter in text:
            if letter not in constants.ALPHABET:
                final_text += letter
                continue
            transformed1: str = self._plugboard.exchange(letter)
            self._rotors[0].rotate()
            for rotor in reversed(self._rotors):
                transformed1 = rotor.swap_letter(transformed1)
            transformed2: str = self._reflector.reflect(transformed1)
            for rotor in self._rotors:
                transformed2 = rotor.reverse_swap_letter(transformed2)
            final_text += self._plugboard.exchange(transformed2)
        return final_text
