import re
from dataclasses import dataclass

from postal_code.models import PostalCode
from models import Domain


@dataclass
class PCodeDE(PostalCode):
    domain: Domain = Domain.DE
    version: int = 2310
    prefix: tuple[str] = (r"^\d{1,5}$")

    def load(self, slug: str) -> PostalCode:
        prefix, domain, version = self.split_slug(slug) 
        self.validate_domain(domain)
        self.validate_version(version)
        if not re.match(self.prefix[0], prefix):
            raise ValueError(f"prefix is not valide: {prefix}")
        self.prefix, self.is_valid = prefix, True
        return self

    def split_suffix(self, suffix_str: str) -> list[str] | None:
        pattern = r"([A-Z]+)(\d+)(E?)"
        matches = re.match(pattern, suffix_str)
        if matches:
            groups = matches.groups()
            return [groups[0], str(int(groups[1])), groups[2]] if groups[2] else [groups[0], str(int(groups[1]))]
        raise ValueError(f"suffix is not valide: {suffix_str}")
