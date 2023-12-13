# import pytest
#
# from enigma.core.rotor_dep import Rotor
# import enigma.core.constants as enigma_const
#
#
# def test_set_shift_default() -> None:
#     rt = Rotor()
#     rt.set_shift(10)
#     assert rt.get_shift() == 10
#
#
# def test_set_shift_arg1_below_minimum_allowed() -> None:
#     rt = Rotor()
#     with pytest.raises(ValueError):
#         rt.set_shift(enigma_const.ROTOR_MINSHIFT - 1)
#
#
# def test_set_shift_arg1_above_maximum_allowed() -> None:
#     rt = Rotor()
#     with pytest.raises(ValueError):
#         rt.set_shift(enigma_const.ROTOR_MAXSHIFT + 1)
#
#
# def test_set_direction_arg1_positive() -> None:
#     rt = Rotor()
#     rt.set_direction(10)
#     assert rt.get_direction() == 1
#
#
# def test_set_direction_arg1_zero() -> None:
#     rt = Rotor()
#     rt.set_direction(0)
#     assert rt.get_direction() == 1
#
#
# def test_set_direction_arg1_negative() -> None:
#     rt = Rotor()
#     rt.set_direction(-4)
#     assert rt.get_direction() == -1
#
#
# def test_inc_shift_with_positive_direction() -> None:
#     init_val: int = 5
#     final_val: int = 6
#     rt = Rotor()
#     rt.set_shift(init_val)
#     rt.set_direction(1)
#     rt.inc_shift()
#     assert rt.get_shift() == final_val
#
#
# def test_inc_shift_when_value_reach_upper_limit_with_positive_direction() -> None:
#     init_val: int = enigma_const.ROTOR_MAXSHIFT
#     final_val: int = enigma_const.ROTOR_MINSHIFT
#     rt = Rotor()
#     rt.set_shift(init_val)
#     rt.set_direction(1)
#     rt.inc_shift()
#     assert rt.get_shift() == final_val
#
#
# def test_inc_shift_with_negative_direction() -> None:
#     init_val: int = 10
#     final_val: int = 9
#     rt = Rotor()
#     rt.set_shift(init_val)
#     rt.set_direction(-1)
#     rt.inc_shift()
#     assert rt.get_shift() == final_val
#
#
# def test_inc_shift_when_value_reach_lower_limit_with_negative_direction() -> None:
#     init_val: int = enigma_const.ROTOR_MINSHIFT
#     final_val: int = enigma_const.ROTOR_MAXSHIFT
#     rt = Rotor()
#     rt.set_shift(init_val)
#     rt.set_direction(-1)
#     rt.inc_shift()
#     assert rt.get_shift() == final_val
#
#
# def test_rotate_letter_with_positive_direction() -> None:
#     rt = Rotor()
#     offset: int = 5
#     rt.set_shift(offset)
#     rt.set_direction(1)
#     assert rt.rotate_letter('l') == 'q'
#
#
# def test_rotate_letter_with_negative_direction() -> None:
#     rt = Rotor()
#     offset: int = 5
#     rt.set_shift(offset)
#     rt.set_direction(-1)
#     assert rt.rotate_letter('l') == 'g'
#
#
# def test_rotate_letter_with_uppercase_arg1_and_positive_direction() -> None:
#     rt = Rotor()
#     offset: int = 5
#     rt.set_shift(offset)
#     rt.set_direction(1)
#     assert rt.rotate_letter('L') == 'q'
#
#
# def test_rotate_letter_with_uppercase_arg1_and_negative_direction() -> None:
#     rt = Rotor()
#     offset: int = 5
#     rt.set_shift(offset)
#     rt.set_direction(-1)
#     assert rt.rotate_letter('L') == 'g'
#
#
# def test_rotate_letter_arg1_not_in_ascii_alphabet() -> None:
#     rt = Rotor()
#     offset: int = 5
#     rt.set_shift(offset)
#     rt.set_direction(1)
#     with pytest.raises(ValueError):
#         rt.rotate_letter('*')
#
#
# def test_rotate_letter_with_arg1_equals_to_z_and_positive_direction() -> None:
#     rt = Rotor()
#     offset: int = 1
#     rt.set_shift(offset)
#     rt.set_direction(1)
#     assert rt.rotate_letter('z') == 'a'
#
#
# def test_rotate_letter_with_arg1_equals_to_a_and_negative_direction() -> None:
#     rt = Rotor()
#     offset: int = 1
#     rt.set_shift(offset)
#     rt.set_direction(-1)
#     assert rt.rotate_letter('a') == 'z'
