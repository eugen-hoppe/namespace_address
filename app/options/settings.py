from enum import Enum


TLD = "ehoppe.com"


class Separator(str, Enum):
    TAG: str = ":"
    AT: str = "@"
    DOT: str = "."

    def __str__(self):
        return self.value


class Subject(str, Enum):
    LICENCE_PLATE: str = "licence-plate"
    POSTAL_CODE: str = "postal-code"

    def __str__(self):
        return self.value
