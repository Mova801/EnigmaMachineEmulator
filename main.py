# Script created by Marte on 09/12/2023
from rich.console import Console
from rich.traceback import install

from enigma.models import rotors_models, reflectors_models
from enigma.core.reflector import Reflector
from enigma.core.rotor import Rotor, RotorFlags
from enigma.enigma import EnigmaMachine

install()  # better looking error print


def single_rotor_permutation(rotor: Rotor, ref: Reflector, letter: str) -> str:
    s1 = rotor.swap_letter(letter)
    s2: str = ref.reflect(s1)
    return rotor.reverse_swap_letter(s2)


def double_rotor_permutation(rotors: list[Rotor], ref: Reflector, letter: str) -> str:
    s1 = rotors[0].swap_letter(letter)
    s2 = rotors[1].swap_letter(s1)
    s3: str = ref.reflect(s2)
    s4: str = rotors[1].reverse_swap_letter(s3)
    return rotors[0].reverse_swap_letter(s4)


def triplet_rotor_permutation(rotors: list[Rotor], ref: Reflector, letter: str) -> str:
    s1 = rotors[0].swap_letter(letter)
    s2 = rotors[1].swap_letter(s1)
    s3 = rotors[2].swap_letter(s2)
    s4: str = ref.reflect(s3)
    s5: str = rotors[2].reverse_swap_letter(s4)
    s6: str = rotors[1].reverse_swap_letter(s5)
    return rotors[0].reverse_swap_letter(s6)


def operate(rotors: list[Rotor], text: str, ) -> str:
    ans: str = ""
    ref = Reflector(reflectors_models.ReflectorBProperties)
    for letter in text:
        rotors[0].rotate()
        res: str
        match len(rotors):
            case 3:
                res = triplet_rotor_permutation(rotors, ref, letter)
            case 2:
                res = double_rotor_permutation(rotors, ref, letter)
            case _:
                res = single_rotor_permutation(rotors[0], ref, letter)
        ans += res
    return ans


def main() -> None:
    console = Console()
    # ...
    console.print('Hello World!', style='bold green')
    input()


if __name__ == '__main__':
    main()
