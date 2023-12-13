# import pytest
#
# import enigma.core.constants as enigma_const
# from enigma.core.rotors_system import RotorsSystem
# from enigma.core.rotor_dep import Rotor
#
#
# def test_set_rotor_default_arg1() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 1, 1)
#     sys.set_rotor(2, 2, 1)
#     sys.set_rotor(3, 3, 1)
#     assert (
#             sys.get_rotor(1).get_shift() == 1 and
#             sys.get_rotor(2).get_shift() == 2 and
#             sys.get_rotor(3).get_shift() == 3
#     )
#
#
# def test_set_rotor_default_arg2() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 0, -1)
#     sys.set_rotor(2, 0, -2)
#     sys.set_rotor(3, 0, -3)
#     assert (
#             sys.get_rotor(1).get_direction() == -1 and
#             sys.get_rotor(2).get_direction() == -1 and
#             sys.get_rotor(3).get_direction() == -1
#     )
#
#
# def test_set_rotor_arg1_lower_than_minimum_rotor_number() -> None:
#     sys = RotorsSystem()
#     with pytest.raises(ValueError):
#         sys.set_rotor(0, 1, 1)
#
#
# def test_set_rotor_arg1_greater_than_maximum_rotor_number() -> None:
#     sys = RotorsSystem()
#     with pytest.raises(ValueError):
#         sys.set_rotor(enigma_const.ROTOR_MAXSHIFT + 1, 1, 1)
#
#
# def test_get_rotor_default_arg1() -> None:
#     r1 = Rotor()
#     r2 = Rotor()
#     r3 = Rotor()
#     sys = RotorsSystem(r1, r2, r3)
#     assert (
#             sys.get_rotor(1) == r1 and
#             sys.get_rotor(2) == r2 and
#             sys.get_rotor(3) == r3
#     )
#
#
# def test_get_rotor_default_arg1_below_minimum_rotor_number() -> None:
#     sys = RotorsSystem()
#     with pytest.raises(ValueError):
#         sys.get_rotor(0)
#
#
# def test_get_rotor_default_arg1_above_maximum_rotor_number() -> None:
#     sys = RotorsSystem()
#     with pytest.raises(ValueError):
#         sys.get_rotor(enigma_const.ROTOR_NUMBER + 1)
#
#
# def test_rotate_rotors_one_cycle_with_rotor_2_and_rotor_3_triggers() -> None:
#     sys = RotorsSystem()
#     sys.set_rotors_direction(1)
#     sys.set_rotor(1, enigma_const.ROTOR_2_SHIFT_TRIGGER - 1, 1)
#     sys.set_rotor(2, enigma_const.ROTOR_3_SHIFT_TRIGGER - 1, 1)
#     sys.set_rotor(3, 0, 1)
#     sys.rotate_rotors()
#     assert (
#             sys.get_rotor(1).get_shift() == 8 and
#             sys.get_rotor(2).get_shift() == 18 and
#             sys.get_rotor(3).get_shift() == 1
#     )
#
#
# def test_rotate_rotors_26_cycles_of_rotor1() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 0, 1)
#     sys.set_rotor(2, 0, 1)
#     sys.set_rotor(3, 0, 1)
#     [sys.rotate_rotors() for _ in range(25)]
#     assert (
#             sys.get_rotor(1).get_shift() == 25 and
#             sys.get_rotor(2).get_shift() == 1 and
#             sys.get_rotor(3).get_shift() == 0
#     )
#
#
# def test_rotate_rotors_18_cycles_of_rotor2() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 0, 1)
#     sys.set_rotor(2, 0, 1)
#     sys.set_rotor(3, 0, 1)
#     [sys.rotate_rotors() for _ in range(25 * 18)]  # cycles 480 times
#     assert (
#             sys.get_rotor(1).get_shift() == 8 and
#             sys.get_rotor(2).get_shift() == 18 and
#             sys.get_rotor(3).get_shift() == 1
#     )
#
#
# def test_rotate_letter_default() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 1, 1)
#     sys.set_rotor(2, 2, 1)
#     sys.set_rotor(3, 3, 1)
#     assert sys.rotate_letter('a') == 'g'
#
#
# def test_rotate_letter_arg1_not_in_ascii() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 1, 1)
#     sys.set_rotor(2, 2, 1)
#     sys.set_rotor(3, 3, 1)
#     with pytest.raises(ValueError):
#         sys.rotate_letter('+')
#
#
# def test_rotate_letter_arg1_length_greater_than_1() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 1, 1)
#     sys.set_rotor(2, 2, 1)
#     sys.set_rotor(3, 3, 1)
#     with pytest.raises(ValueError):
#         sys.rotate_letter('av')
#
#
# def test_rotate_letter_arg2_true() -> None:
#     sys = RotorsSystem()
#     sys.set_rotor(1, 1, 1)
#     sys.set_rotor(2, 2, 1)
#     sys.set_rotor(3, 3, 1)
#     assert sys.rotate_letter('a', True) == 'g'
