# ROTORS MODELS
class RotorProperties:
    model: str
    alphabet: str
    turnover: int


class RotorIProperties(RotorProperties):
    model: str = "RI"
    alphabet: str = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    turnover: int = 17  # Q - 18  # R -


class RotorIIProperties(RotorProperties):
    model: str = "RII"
    alphabet: str = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    turnover: int = 5  # E - 6  # F -


class RotorIIIProperties(RotorProperties):
    model: str = "RIII"
    alphabet: str = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    turnover: int = 22  # V - 23  # W -


class RotorIVProperties(RotorProperties):
    model: str = "RIV"
    alphabet: str = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    turnover: int = 10  # J - 11  # K -


class RotorVProperties(RotorProperties):
    model: str = "RV"
    alphabet: str = "VZBRGITYUPSDNHLXAWMJQOFECK"
    turnover: int = 26  # Z - 1  # A -
