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
