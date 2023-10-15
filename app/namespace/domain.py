from enum import Enum, auto


class Domain(Enum):
    DE = auto()
    CH = auto()
    AT = auto()

    def __str__(self):
        return self.name
