from enum import StrEnum


class IdmResultCode(StrEnum):
    SUCCESS = "200"
    UNAUTHORIZED = "401"

    def __str__(self) -> str:
        return str(self.value)
