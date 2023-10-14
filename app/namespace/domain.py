from enum import Enum


class Domain(str, Enum):
    DE: str = "DE"
    CH: str = "CH"
    AT: str = "AT"

    def __str__(self):
        return self.value
