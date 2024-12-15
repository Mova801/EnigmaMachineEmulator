from lib.enigma import enigma, core, models, tests
from lib.enigma import config


def create_enigma_machine(config_class=config.Config) -> enigma.EnigmaMachine:
    e: enigma.EnigmaMachine = enigma.EnigmaMachine(
        rotors_models=config_class.ROTORS_MODEL,
        reflectors_model=config_class.REFLECTORS_MODEL
    )
    return e
