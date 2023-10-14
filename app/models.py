from dataclasses import dataclass, field
from enum import Enum


TLD = None


class ErrorSnippet(str, Enum):
    DOMAIN: str = "Slug is not valid for domain: "
    VERSION: str = "Slug is not valid for version: "

    def __str__(self):
        return self.value


class Domain(str, Enum):
    DE: str = "DE"
    CH: str = "CH"
    AT: str = "AT"

    def __str__(self):
        return self.value


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


@dataclass
class NamespaceAddress:
    version: int
    domain: Domain
    subject: Subject
    prefix: tuple[str, ...] | list[str] = field(default_factory=list)
    tld: str | None = TLD
    is_valid: bool = False
    sep: Separator = Separator

    def validate_domain(self, domain: str):
        if domain.split()[0] != self.domain.value:
            raise ValueError(ErrorSnippet.DOMAIN + self.domain.value)

    def validate_version(self, version):
        if version != str(self.version):
            # TODO: Validate version range
            raise ValueError(ErrorSnippet.VERSION + str(self.version))

    def split_by_at(self, slug: str) -> tuple[str, str]:
        if not isinstance(slug, str):
            raise TypeError("slug must be a str")
        slug = slug.upper()
        return slug.split(self.sep.AT)
