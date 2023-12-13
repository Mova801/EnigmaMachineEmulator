from enigma.core.dep.rotor_dep import Rotor
import enigma.core.constants as enigma_const


class RotorsSystem:
    __rotors: tuple[Rotor, Rotor, Rotor]

    # __r1_counter: int
    # __r2_counter: int

    def __init__(self, rotor1: Rotor = None, rotor2: Rotor = None, rotor3: Rotor = None) -> None:
        if rotor1 is not None:
            self.__rotors = (rotor1, rotor2, rotor3)
        else:
            self.__rotors = (Rotor(), Rotor(), Rotor())
        # self.__r1_counter = 0
        # self.__r2_counter = 0

    def set_rotors_direction(self, direction: int) -> None:
        [self.__rotors[i].set_direction(direction) for i in range(len(self.__rotors))]

    def set_rotor(self, rotor_number: int, shift: int, direction: int) -> None:
        if rotor_number > enigma_const.ROTOR_NUMBER or rotor_number < 1:
            raise ValueError(f"Invalid rotor number {rotor_number}. Must be between 1 and {enigma_const.ROTOR_NUMBER}")
        rotor_number -= 1
        rotor = self.__rotors[rotor_number]
        rotor.set_shift(shift)
        rotor.set_direction(direction)

    def get_rotor(self, rotor_number: int) -> Rotor:
        if rotor_number > enigma_const.ROTOR_NUMBER or rotor_number < 1:
            raise ValueError(f"Invalid rotor number {rotor_number}. Must be between 1 and {enigma_const.ROTOR_NUMBER}")
        rotor_number -= 1
        return self.__rotors[rotor_number]

    def rotate_rotors(self) -> None:
        self.__rotors[0].inc_shift()
        # self.__r1_counter += 1
        if self.__rotors[0] == enigma_const.ROTOR_2_SHIFT_TRIGGER:
            # self.__r1_counter = 0
            # self.__r2_counter += 1
            self.__rotors[1].inc_shift()
            if self.__rotors[1] == enigma_const.ROTOR_3_SHIFT_TRIGGER:
                # self.__r2_counter = 0
                self.__rotors[2].inc_shift()

    def rotate_letter(self, l0: str, backward_flag: bool = 0) -> str:
        start: int = 2 if backward_flag else 0
        direction: int = -1 if backward_flag else 1
        l1: str = self.__rotors[start + direction].rotate_letter(l0)
        l2: str = self.__rotors[start + direction].rotate_letter(l1)
        return self.__rotors[start + direction].rotate_letter(l2)
