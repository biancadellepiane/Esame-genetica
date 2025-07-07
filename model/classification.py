from dataclasses import dataclass

@dataclass
class Classification:
    GeneID: str
    Localization: str

    def __str__(self):
        return f"{self.GeneID} | Loc.: {self.Localization}"

    def __eq__(self, other):
        return self.GeneID == other.GeneID

    def __hash__(self):
        return hash(self.GeneID)
