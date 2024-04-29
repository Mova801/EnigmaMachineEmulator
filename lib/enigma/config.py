from models import rotors_models, reflectors_models


class Config:
    ROTORS_MODEL: tuple[rotors_models.RotorProperties, ...] = [
        rotors_models.RotorIProperties(), rotors_models.RotorVProperties(), rotors_models.RotorIIIProperties()
    ]
    REFLECTORS_MODEL: reflectors_models.ReflectorProperties = reflectors_models.ReflectorBProperties
