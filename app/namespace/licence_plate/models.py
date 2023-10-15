import re

from dataclasses import dataclass, field
from app.models import NamespaceAddress, Subject


@dataclass
class LPlate(NamespaceAddress):
    suffix: tuple[str | re.Pattern, ...] | list[str] = field(default_factory=list)
    subject: str = Subject.LICENCE_PLATE.value

    def __post_init__(self):
        self.prefix = tuple([re.compile(pattern) for pattern in self.prefix])
        self.suffix = tuple([re.compile(pattern) for pattern in self.suffix])

    def slug(self) -> str:
        if not self.is_valid:
            raise ValueError("Licence Plate is not valid")
        lp_id = "".join(self.prefix) + self.sep.DOT + "".join(self.suffix)
        namespace = self.domain + self.sep.DOT + self.subject
        if self.tld:
            namespace += self.sep.DOT + self.tld
        namespace += self.sep.TAG + str(self.version)
        return f"{lp_id}{self.sep.AT}{namespace}".lower()

    def split_slug(self, slug: str) -> tuple[str, str, str, str | None]:
        address, namespace = self.split_by_at(slug)
        prefix, suffix = address.split(self.sep.DOT)
        domain, *version = namespace.split(self.sep.TAG)
        return prefix, suffix, domain, version[0] if version else None

    def namespace(self) -> str:
        namespace = self.domain + self.sep.DOT + self.subject
        if self.tld:
            namespace += self.sep.DOT + self.tld
        namespace += self.sep.TAG + str(self.version)
        return namespace.lower()

    def at_namespace(self) -> str:
        return f"{self.sep.AT}{self.namespace()}"

    def licence_plate(self, lp_sep: str = "-") -> str:
        return "".join(self.prefix) + lp_sep + "".join(self.suffix)
