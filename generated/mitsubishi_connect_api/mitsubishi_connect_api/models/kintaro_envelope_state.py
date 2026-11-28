from enum import StrEnum


class KintaroEnvelopeState(StrEnum):
    F = "F"
    S = "S"

    def __str__(self) -> str:
        return str(self.value)
