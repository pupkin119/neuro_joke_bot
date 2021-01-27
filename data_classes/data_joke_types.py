from dataclasses import dataclass


@dataclass
class MarkovJokeTypes:
    ranevstakay: str = "ranevstakay"
    sex_joke: str = "sex_joke"


@dataclass
class NeuroJokeTypes:
    sex_joke: str = "neuro_sex_joke"
