import pytest

from enigma.core.plugboard import Plugboard


def test_set_plugboard_default() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX', 'BY', 'CZ']
    pb.set_plugboard(swaps)
    assert (
            pb._input.find('A') != -1
            and pb._output.find('A') != -1
            and pb._input.find('X') != -1
            and pb._output.find('X') != -1
    )


def test_set_plugboard_pair_with_two_letters_in_first_position_associated_with_one_letter() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX', 'AX', 'CZ']
    with pytest.raises(ValueError):
        pb.set_plugboard(swaps)


def test_set_plugboard_pair_with_one_letter_associated_with_two_letters_in_last_position() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX', 'BX', 'CZ']
    with pytest.raises(ValueError):
        pb.set_plugboard(swaps)


def test_set_plugboard_pair_with_lowercase_letter_in_first_position() -> None:
    pb = Plugboard()
    swaps: list[str] = ['aX', 'CY']
    pb.set_plugboard(swaps)
    assert (pb._input.find('A') != -1 and pb._output.find('A') != -1)


def test_set_plugboard_pair_with_lowercase_letter_in_last_position() -> None:
    pb = Plugboard()
    swaps: list[str] = ['Ax', 'CY']
    pb.set_plugboard(swaps)
    assert (pb._input.find('X') != -1 and pb._output.find('X') != -1)


def test_set_plugboard_pair_with_length_greater_than_two() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX', 'CBY']
    with pytest.raises(ValueError):
        pb.set_plugboard(swaps)


def test_set_plugboard_pair_with_length_lower_than_two() -> None:
    pb = Plugboard()
    swaps: list[str] = ['A', 'CZ']
    with pytest.raises(ValueError):
        pb.set_plugboard(swaps)


def test_set_plugboard_pair_with_first_character_not_in_alphabet() -> None:
    pb = Plugboard()
    swaps: list[str] = ['0X', 'CY']
    with pytest.raises(ValueError):
        pb.set_plugboard(swaps)


def test_set_plugboard_pair_with_last_character_not_in_alphabet() -> None:
    pb = Plugboard()
    swaps: list[str] = ['A0', 'CY']
    with pytest.raises(ValueError):
        pb.set_plugboard(swaps)


def test_exchange_default() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX']
    pb.set_plugboard(swaps)
    assert pb.exchange('A') == 'X'


def test_exchange_arg1_not_in_alphabet() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX']
    pb.set_plugboard(swaps)
    with pytest.raises(ValueError):
        pb.exchange('0')


def test_exchange_lowercase_arg1() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX']
    pb.set_plugboard(swaps)
    assert pb.exchange('a') == 'X'


def test_clear() -> None:
    pb = Plugboard()
    swaps: list[str] = ['AX', 'BY', 'CZ']
    pb.set_plugboard(swaps)
    pb.clear()
    assert pb._input == pb._output == ""
