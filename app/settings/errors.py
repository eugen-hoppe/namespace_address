from enum import Enum


class ErrorSnippet(str, Enum):
    """
    ErrorSnippet
    """
    DOMAIN: str = "Slug is not valid for domain: "
    VERSION: str = "Slug is not valid for version: "

    def __str__(self):
        return self.value
