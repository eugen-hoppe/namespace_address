from dataclasses import dataclass, field
from app.models import NamespaceAddress, Subject


@dataclass
class LicencePlate(NamespaceAddress):
    suffix: tuple[str, ...] | list[str] = field(default_factory=list)
    subject: Subject = Subject.LICENCE_PLATE.value
        
    def slug(self) -> str:
        if not self.is_valid:
            raise ValueError("Licence Plate is not valide")
        lp_id = "".join(self.prefix) + self.sep.DOT + "".join(self.suffix)
        namespace = self.domain + self.sep.DOT + self.subject
        if self.tld:
            namespace += self.sep.DOT + self.tld
        namespace += self.sep.TAG + str(self.version)
        return f"{lp_id}{self.sep.AT}{namespace}".lower()
    
    def split_slug(self, slug: str) -> tuple[str, str, str, str]:
        address, namespace = self.split_by_at(slug)
        prefix, suffix = address.split(self.sep.DOT)
        domain, version = namespace.split(self.sep.TAG)
        return prefix, suffix, domain, version
    
    def namespace(self) -> str:
        namespace = self.domain + self.sep.DOT + self.subject
        if self.tld:
            namespace += self.sep.DOT + self.tld
        namespace += self.sep.TAG + str(self.version)
        return namespace.lower()
    
    def at_namespace(self) -> str:
        return f"{self.sep.AT}{self.namespace()}"
