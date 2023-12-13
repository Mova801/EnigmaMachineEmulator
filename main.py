# Script created by Marte on 09/12/2023
from rich.console import Console
from rich.traceback import install

from enigma.core.models.reflectors_models import ReflectorBProperties
from enigma.core.models.rotors_models import RotorIProperties, RotorIIProperties, RotorIIIProperties
from enigma.core.reflector import Reflector
from enigma.core.rotor import Rotor
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
    ref = Reflector(ReflectorBProperties)
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

    # sender1 = Rotor(RotorIProperties)
    # sender2 = Rotor(RotorIProperties)
    # sender3 = Rotor(RotorIProperties)
    # receiver1 = Rotor(RotorIProperties)
    # receiver2 = Rotor(RotorIProperties)
    # receiver3 = Rotor(RotorIProperties)
    #
    # initial_text: str = 'A'
    #
    # sender1.set_alphabet_ring_position(1)
    # sender1.set_starting_position('A')
    # sender2.set_alphabet_ring_position(1)
    # sender2.set_starting_position('A')
    # sender3.set_alphabet_ring_position(1)
    # sender3.set_starting_position('A')
    #
    # receiver1.set_alphabet_ring_position(1)
    # receiver1.set_starting_position('A')
    # receiver2.set_alphabet_ring_position(1)
    # receiver2.set_starting_position('A')
    # receiver3.set_alphabet_ring_position(1)
    # receiver3.set_starting_position('A')
    #
    # sender_out: str = operate([sender1, sender2, sender3], initial_text)
    # receiver_out = operate([receiver1, receiver2, receiver3], sender_out)

    r1 = Rotor(RotorIProperties)
    r2 = Rotor(RotorIIProperties)
    r3 = Rotor(RotorIIIProperties)
    initial_text: str = 'hello'

    arp: tuple[int, int, int] = (1, 1, 1)
    sp: tuple[str, str, str] = ('A', 'A', 'A')

    # Sender Enigma Machine
    sender: EnigmaMachine = EnigmaMachine((r1, r2, r3))  # init
    sender.set_alphabet_ring_position(arp)  # setting alphabet ring pos
    sender.set_rotors_position(sp)  # setting initial rotor pos
    sender_out: str = sender.process_text(initial_text)  # process initial text

    # Receiver Enigma Machine
    receiver: EnigmaMachine = EnigmaMachine((r1, r2, r3))  # init
    receiver.set_alphabet_ring_position(arp)  # setting alphabet ring pos
    receiver.set_rotors_position(sp)  # setting initial rotor pos
    receiver_out: str = sender.process_text(sender_out)  # process encrypted text

    console.print(f"Sender text: {initial_text.upper()}")
    console.print(f"Encrypted text: {sender_out}")
    console.print(f"Decrypted result: {receiver_out} ({receiver_out.upper() == initial_text.upper()})")


if __name__ == '__main__':
    main()
