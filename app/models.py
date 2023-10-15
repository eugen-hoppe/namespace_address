from re import Pattern
from dataclasses import dataclass, field
from app.namespace.domain import Domain
from app.settings.errors import ErrorSnippet
from app.settings.options import TLD
from app.settings.constants import Separator, Subject


@dataclass
class NamespaceAddress:
    version: int
    domain: Domain | str
    subject: Subject | str
    prefix: tuple[str | Pattern, ...] | list[str] = field(default_factory=list)
    tld: str | None = TLD
    is_valid: bool = False
    sep: Separator = Separator

    def validate_domain(self, domain: str):
        domain_path = domain.lower().split(".")
        if domain_path[0] != str(self.domain):
            raise ValueError(ErrorSnippet.DOMAIN + str(self.domain))
        tld: str | None = None
        for level, name in enumerate(domain_path):
            if level == 1:
                subject = name.lower()
                if not subject in Subject.__members__.values():
                    raise ValueError("Namespace Error")
                if subject != self.subject:
                    raise ValueError("Subject Error")
            if level > 1:
                if level == 2:
                    tld = ""
                tld += name + "."
        if tld:
            if tld.removesuffix(".").lower() != self.tld:
                raise ValueError("Namespace Provider Error")

    def validate_version(self, version):
        if version != str(self.version):
            # TODO: Validate version range
            raise ValueError(ErrorSnippet.VERSION + str(self.version))

    def split_by_at(self, slug: str) -> tuple[str, str]:
        if not isinstance(slug, str):
            raise TypeError("slug must be a str")
        slug = slug.upper()
        return slug.split(self.sep.AT)
