# import pytest
#
# from enigma.enigma import EnigmaMachine
# import enigma.core.constants as enigma_consts
#
#
# def test_set_plugboard_default() -> None:
#     enigma = EnigmaMachine()
#     lin: list[str] = ['a', 'b', 'c']
#     lout: list[str] = ['x', 'y', 'z']
#     enigma.set_plugboard(lin, lout)
#     assert (
#             enigma.get_plugboard().exchange('a') == 'x' and
#             enigma.get_plugboard().exchange('b') == 'y' and
#             enigma.get_plugboard().exchange('c') == 'z'
#     )
#
#
# def test_set_rotors_arg1_default() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_rotors([1, 2, 3], 1)
#     assert (
#             enigma.get_rotors_system().get_rotor(1).get_shift() == 1 and
#             enigma.get_rotors_system().get_rotor(2).get_shift() == 2 and
#             enigma.get_rotors_system().get_rotor(3).get_shift() == 3
#     )
#
#
# def test_set_rotors_arg2_default() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_rotors([0, 0, 0], -10)
#     assert (
#             enigma.get_rotors_system().get_rotor(1).get_direction() == -1 and
#             enigma.get_rotors_system().get_rotor(2).get_direction() == -1 and
#             enigma.get_rotors_system().get_rotor(3).get_direction() == -1
#     )
#
#
# def test_set_rotors_arg1_invalid_values() -> None:
#     enigma = EnigmaMachine()
#     with pytest.raises(ValueError):
#         enigma.set_rotors([0, -1, 40], -10)
#
#
# def test_set_reflector_default() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_reflector(10)
#     assert enigma.get_reflector().get_shift() == 10
#
#
# def test_set_reflector_arg1_below_lower_limit() -> None:
#     enigma = EnigmaMachine()
#     with pytest.raises(ValueError):
#         enigma.set_reflector(enigma_consts.ROTOR_MINSHIFT - 1)
#
#
# def test_set_reflector_arg1_above_upper_limit() -> None:
#     enigma = EnigmaMachine()
#     with pytest.raises(ValueError):
#         enigma.set_reflector(enigma_consts.ROTOR_MAXSHIFT + 1)
#
#
# def test_encrypt_without_setting_up_plugboard_reflector_with_0_shift_and_positive_direction() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_rotors([1, 2, 3], 1)
#     enigma.set_reflector(0)
#     assert enigma.encrypt_text('a') == 'm'
#
#
# def test_encrypt_arg1_with_non_ascii_character() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_rotors([1, 2, 3], 1)
#     enigma.set_reflector(0)
#     assert enigma.encrypt_text('hello world!') == 'tqxxa igjdv!'
#
#
# def test_encrypt_uppercase_arg1() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_rotors([1, 2, 3], 1)
#     enigma.set_reflector(0)
#     assert enigma.encrypt_text('A') == enigma.encrypt_text('a')
#
#
# def test_encrypt_without_setting_up_plugboard_reflector_with_0_shift_and_negative_direction() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_rotors([1, 2, 3], -1)
#     enigma.set_reflector(0)
#     assert enigma.encrypt_text('m') == 'a'
#
#
# def test_encrypt_with_reflector_set_to_0_shift_and_positive_direction() -> None:
#     enigma = EnigmaMachine()
#     enigma.set_plugboard(['h', 'e', 'l', 'o', 'w', 'r', 'd'],
#                          ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
#     enigma.set_rotors([0, 0, 0], 1)
#     enigma.set_reflector(0)
#     assert enigma.encrypt_text('hello world') == 'abccg bgfcg'
#
#
# # def test_encrypt_1() -> None:
# #     R_I_shift: int = 9
# #     R_II_shift: int = 20
# #     R_III_shift: int = 15
# #     reflector: str = "QZ"
