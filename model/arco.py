from dataclasses import dataclass

from model.classification import Classification


@dataclass
class Arco:
    gene1: Classification
    gene2: Classification
    peso: int