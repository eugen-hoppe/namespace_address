from dataclasses import dataclass, field
from app.namespace.domain import Domain
from app.options.errors import ErrorSnippet
from app.options.settings import Separator, Subject, TLD


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
        domain_path = domain.split(".")
        if domain_path[0] != self.domain.name:
            raise ValueError(ErrorSnippet.DOMAIN + self.domain.name)
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
