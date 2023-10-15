import re
from dataclasses import dataclass

from app.namespace.licence_plate.models import LPlate
from app.models import Domain


@dataclass
class LPlateDEv2310(LPlate):
    domain: str = Domain.DE.name.lower()
    version: int = 2310
    prefix: tuple[re.Pattern | str] = (r"^[A-Z]{1,3}$",)
    suffix: tuple[str, str | int, str] | tuple[re.Pattern, ...] = (
        r"^[A-Z]{1,2}$",
        r"^\d{1,4}$",
        r"^E?$",
    )

    def load(self, slug: str) -> LPlate:
        prefix, suffix_str, domain, version = self.split_slug(slug)
        if not version:
            version = str(self.version)
        self.validate_domain(domain)
        self.validate_version(version)
        if not re.match(self.prefix[0], prefix):
            raise ValueError(f"prefix is not valid: {prefix}")
        suffix = self.split_suffix(suffix_str)
        for index, snippet in enumerate(suffix):
            if not re.match(self.suffix[index], snippet):
                raise ValueError(f"suffix is not valid: {suffix[index]}")
        self.prefix, self.suffix, self.is_valid = prefix, suffix, True
        return self

    def split_suffix(self, suffix_str: str) -> list[str] | None:
        matches = re.match(re.compile(r"([A-Z]+)(\d+)(E?)"), suffix_str)
        if matches:
            groups = matches.groups()
            return (
                [groups[0], str(int(groups[1])), groups[2]]
                if groups[2]
                else [groups[0], str(int(groups[1]))]
            )
        raise ValueError(f"suffix is not valid: {suffix_str}")

    def licence_plate(self, lp_sep: str = "-") -> str:
        return "".join(self.prefix) + lp_sep + "".join(self.suffix)
