from enum import StrEnum


class CreateSpeedAlertRequestSpeedUnit(StrEnum):
    KMH = "KMH"
    MPH = "MPH"

    def __str__(self) -> str:
        return str(self.value)
