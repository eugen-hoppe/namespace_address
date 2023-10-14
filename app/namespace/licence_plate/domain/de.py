import re
from dataclasses import dataclass

from app.namespace.licence_plate.models import LicencePlate
from app.models import Domain


@dataclass
class LPlateDE(LicencePlate):
    domain: Domain = Domain.DE
    version: int = 2310
    prefix: tuple[str] = (r"^[A-Z]{1,3}$")  # TODO compile
    suffix: tuple[str, str | int, str] = (r"^[A-Z]{1,2}$", r"^\d{1,4}$", r"^E?$")  # TODO compile

    def load(self, slug: str) -> LicencePlate:
        prefix, suffix_str, domain, version = self.split_slug(slug)
        self.validate_domain(domain)
        self.validate_version(version)
        if not re.match(self.prefix[0], prefix):
            raise ValueError(f"prefix is not valide: {prefix}")
        suffix = self.split_suffix(suffix_str)
        for index, snippet in enumerate(suffix):
            if not re.match(self.suffix[index], snippet):
                raise ValueError(f"suffix is not valide: {suffix[index]}")
        self.prefix, self.suffix, self.is_valid = prefix, suffix, True
        return self

    def split_suffix(self, suffix_str: str) -> list[str] | None:
        pattern = re.compile(r"([A-Z]+)(\d+)(E?)")
        matches = re.match(pattern, suffix_str)
        if matches:
            groups = matches.groups()
            return (
                [groups[0], str(int(groups[1])), groups[2]]
                if groups[2]
                else [groups[0], str(int(groups[1]))]
            )
        raise ValueError(f"suffix is not valide: {suffix_str}")
