import pytest

from enigma.core.reflector import Reflector
from enigma.core.rotor import Rotor
from enigma.models.rotors_models import (
    RotorIProperties, RotorIIProperties, RotorIIIProperties
)
from enigma.models.reflectors_models import ReflectorBProperties


def setup_rotors(rotors: list[Rotor], offsets: list[int], positions: list[str]) -> None:
    # setting rotors starting position
    [rt.set_starting_position(positions[i]) for i, rt in enumerate(rotors)]
    # setting rotors alphabet ring position
    [rt.set_alphabet_ring_position(offsets[i]) for i, rt in enumerate(rotors)]


def test_rotor_swap_with_rotation() -> None:
    rt = Rotor(RotorIProperties)
    rt.set_starting_position('Z')
    rt.set_alphabet_ring_position(1)
    rt.rotate()

    p1: str = rt.swap_letter('A')

    rt2 = Rotor(RotorIProperties)
    rt2.set_starting_position('Z')
    rt2.set_alphabet_ring_position(1)
    rt2.rotate()

    p2: str = rt2.reverse_swap_letter(p1)

    assert (
            p1 == 'M' and
            rt._position == 1 and
            p2 == 'A' and
            rt2._position == 1
    )


#
#
# def test_set_alphabet_ring_position_default() -> None:
#     r1: Rotor = Rotor(RotorIProperties)
#     r1.set_alphabet_ring_position(15)
#     letter: str = 'A'
#     assert r1.swap(letter) == 'H'
#
#
# def test_set_alphabet_ring_position_arg1_below_lower_limit() -> None:
#     r1: Rotor = Rotor(RotorIProperties)
#     with pytest.raises(ValueError):
#         r1.set_alphabet_ring_position(const.ROTOR_MIN_OFFSET - 1)
#
#
# def test_set_alphabet_ring_position_arg1_above_upper_limit() -> None:
#     r1: Rotor = Rotor(RotorIProperties)
#     with pytest.raises(ValueError):
#         r1.set_alphabet_ring_position(const.ROTOR_MAX_OFFSET + 1)
#
#
# def test_set_starting_position_default() -> None:
#     r1: Rotor = Rotor(RotorIProperties)
#     r1.set_starting_position('Z')
#     assert r1.swap('A') == 'J'


def test_one_rotor_encryption_and_decryption_with_rotation() -> None:
    r1: Rotor = Rotor()
    ref: Reflector = Reflector(ReflectorBProperties)

    r1.set_starting_position('B')
    r1.set_alphabet_ring_position(1)
    r1.rotate()

    # encryption
    enc_letter: str = 'A'
    p1: str = r1.swap_letter(enc_letter)
    p2: str = ref.reflect(p1)
    p3: str = r1.reverse_swap_letter(p2)

    # decryption
    dec_letter: str = p3
    p4: str = r1.swap_letter(dec_letter)
    p5: str = ref.reflect(p4)
    p6: str = r1.reverse_swap_letter(p5)

    assert p6 == enc_letter


# noinspection DuplicatedCode
def test_three_rotor_first_half_cycle_without_rotation_with_offset() -> None:
    r1: Rotor = Rotor(RotorIProperties)
    r2: Rotor = Rotor(RotorIIProperties)
    r3: Rotor = Rotor(RotorIIIProperties)
    rotors = [r1, r2, r3]
    sp: list[str] = ['A', 'A', 'A']
    setup_rotors(rotors, [1, 1, 1], sp)
    # test start
    letter: str = 'A'
    p1: str = r1.swap_letter(letter)
    p2: str = r2.swap_letter(p1)
    p3: str = r3.swap_letter(p2)
    assert p3 == 'Y'


# noinspection DuplicatedCode
def test_three_rotor_first_half_cycle_with_rotation() -> None:
    r1: Rotor = Rotor(RotorIProperties)
    r2: Rotor = Rotor(RotorIIProperties)
    r3: Rotor = Rotor(RotorIIIProperties)
    rotors = [r1, r2, r3]
    sp: list[str] = ['Z', 'A', 'A']
    setup_rotors(rotors, [1, 1, 1], sp)
    # attaching rotors
    r1.attach_rotor(r2)
    r2.attach_rotor(r3)
    # test start
    letter: str = 'A'
    r1.rotate()
    p1: str = r1.swap_letter(letter)
    p2: str = r2.swap_letter(p1)
    p3: str = r3.swap_letter(p2)
    assert p3 == 'Y'


# noinspection DuplicatedCode
# def test_three_rotor_second_half_cycle_without_rotation() -> None:
#     r1: Rotor = Rotor(RotorIProperties)
#     r2: Rotor = Rotor(RotorIIProperties)
#     r3: Rotor = Rotor(RotorIIIProperties)
#     rotors = [r1, r2, r3]
#     sp: list[str] = ['B', 'A', 'A']
#     setup_rotors(rotors, [0, 0, 0], sp)
#     # test start
#     letter: str = 'K'
#     p3: str = r3.reverse_swap(letter)
#     p2: str = r2.reverse_swap(p3)
#     p1: str = r1.reverse_swap(p2)
#     assert p1 == 'Q'


# noinspection DuplicatedCode
# def test_three_rotor_second_half_cycle_with_rotation() -> None:
#     r1: Rotor = Rotor(RotorIProperties)
#     r2: Rotor = Rotor(RotorIIProperties)
#     r3: Rotor = Rotor(RotorIIIProperties)
#     rotors = [r1, r2, r3]
#     sp: list[str] = ['B', 'A', 'A']
#     setup_rotors(rotors, [0, 0, 0], sp)
#     # attaching rotors
#     r1.attach_rotor(r2)
#     r2.attach_rotor(r3)
#     # test start
#     letter: str = 'K'
#     r1.rotate()
#     p3: str = r3.reverse_swap(letter)
#     p2: str = r2.reverse_swap(p3)
#     p1: str = r1.reverse_swap(p2)
#     assert p1 == 'P'

def test_swap_no_position_no_offset() -> None:
    rt: Rotor = Rotor(RotorIProperties)
    rt._position = 0
    rt._offset = 0
    letter: str = 'G'
    p1: str = rt.swap_letter(letter)
    assert p1 == 'D'


def test_swap_default() -> None:
    rt: Rotor = Rotor(RotorIProperties)
    letter: str = 'G'
    p1: str = rt.swap_letter(letter)
    assert p1 == 'V'


# def test_swap_arg1_not_in_alphabet() -> None:
#     rt = Rotor(RotorIProperties)
#     letter: str = '*'
#     with pytest.raises(ValueError):
#         rt.swap_letter(letter)


def test_reverse_swap_default() -> None:
    rt = Rotor(RotorIProperties)
    letter: str = 'A'
    p1: str = rt.reverse_swap_letter(letter)
    assert p1 == 'S'


def test_reverse_swap_no_position_no_offset() -> None:
    rt = Rotor(RotorIProperties)
    rt._position = 0
    rt._offset = 0
    letter: str = 'A'
    p1: str = rt.reverse_swap_letter(letter)
    assert p1 == 'U'


def test_reverse_swap_arg1_not_in_alphabet() -> None:
    r1 = Rotor(RotorIProperties)
    letter: str = '*'
    with pytest.raises(ValueError):
        r1.reverse_swap_letter(letter)
