# import pytest
#
# from enigma.core.plugboard import Plugboard
#
#
# def test_exchange_default() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a']
#     lout: list[str] = ['x']
#     pb.set_swap(lin, lout)
#     assert pb.exchange(lin[0]) == lout[0]
#
#
# def test_exchange_arg1_invalid() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a']
#     lout: list[str] = ['x']
#     pb.set_swap(lin, lout)
#     assert pb.exchange('0') == '0'
#
#
# def test_exchange() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'b', 'c']
#     lout: list[str] = ['x', 'y', 'z']
#     pb.set_swap(lin, lout)
#     assert pb.exchange(lin[0]) == lout[0]
#
#
# def test_set_swap_default() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'b', 'c']
#     lout: list[str] = ['x', 'y', 'z']
#     pb.set_swap(lin, lout)
#     assert pb.get_swap_dict().get('a') == 'x'
#
#
# def test_set_swap_two_elem_of_arg1_associated_with_one_elem_of_arg2() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'b', 'c']
#     lout: list[str] = ['x', 'x', 'z']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_set_swap_one_elem_of_arg1_associated_with_two_elem_of_arg2() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'a', 'c']
#     lout: list[str] = ['x', 'y', 'z']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_set_swap_arg1_uppercase_letter() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['A', 'c']
#     lout: list[str] = ['x', 'y']
#     pb.set_swap(lin, lout)
#     # with pytest.raises(ValueError):
#     ret = pb.get_swap_dict().get('a') == 'x'
#
#
# def test_set_swap_arg2_uppercase_letter() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'c']
#     lout: list[str] = ['X', 'y']
#     pb.set_swap(lin, lout)
#     # with pytest.raises(ValueError):
#     ret = pb.get_swap_dict().get('a') == 'X'
#
#
# def test_set_swap_arg1_element_with_len_greater_than_1() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'cb']
#     lout: list[str] = ['x', 'y']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_set_swap_arg2_element_with_len_greater_than_1() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'c']
#     lout: list[str] = ['x', 'yz']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_set_swap_arg1_arg2_list_with_different_length() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'c']
#     lout: list[str] = ['x']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_set_swap_arg1_invalid() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['0', 'c']
#     lout: list[str] = ['x', 'y']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_set_swap_arg2_invalid() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'c']
#     lout: list[str] = ['0', 'y']
#     with pytest.raises(ValueError):
#         pb.set_swap(lin, lout)
#
#
# def test_clear() -> None:
#     pb = Plugboard()
#     lin: list[str] = ['a', 'b', 'c']
#     lout: list[str] = ['x', 'y', 'z']
#     pb.set_swap(lin, lout)
#     pb.clear()
#     assert pb.get_swap_dict() == {}
