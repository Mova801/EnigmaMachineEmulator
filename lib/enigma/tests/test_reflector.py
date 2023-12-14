import pytest

from ..core.reflector import Reflector
from ..models.reflectors_models import ReflectorBProperties


def test_set_pairs_default() -> None:
    reflector = Reflector()
    reflector.set_pairs(ReflectorBProperties)
    assert (reflector._input.find('a') == reflector._output.find('y') and
            reflector._input.find('y') == reflector._output.find('a') and
            reflector._input.find('b') == reflector._output.find('r') and
            reflector._input.find('r') == reflector._output.find('b')
            )


def test_set_pairs_with_length_other_than_26_letters_alphabet_half() -> None:
    ref: list[str] = ["AY"]
    reflector = Reflector()
    with pytest.raises(ValueError):
        reflector.set_pairs(ref)


def test_set_pairs_with_first_pair_elem_not_in_alphabet() -> None:
    ref = ReflectorBProperties.copy()
    ref[4] = "E0"
    reflector = Reflector()
    with pytest.raises(ValueError):
        reflector.set_pairs(ref)


def test_set_pairs_with_second_pair_elem_not_in_alphabet() -> None:
    ref = ReflectorBProperties.copy()
    ref[4] = "0E"
    reflector = Reflector()
    with pytest.raises(ValueError):
        reflector.set_pairs(ref)


def test_reflect_default() -> None:
    reflector = Reflector()
    reflector.set_pairs(ReflectorBProperties)
    assert reflector.reflect('a') == 'Y'


def test_reflect_arg1_uppercase() -> None:
    reflector = Reflector()
    reflector.set_pairs(ReflectorBProperties)
    assert reflector.reflect('A') == 'Y'


def test_reflect_arg1_not_in_registered_pairs() -> None:
    reflector = Reflector()
    reflector.set_pairs(ReflectorBProperties)
    with pytest.raises(ValueError):
        reflector.reflect('0')
