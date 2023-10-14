from dataclasses import dataclass
from models import NamespaceAddress, Subject


@dataclass
class PostalCode(NamespaceAddress):
    subject: Subject = Subject.POSTAL_CODE.value
        
    def slug(self) -> str:
        if not self.is_valid:
            raise ValueError("slug is not valid")
        lp_id = "".join(self.prefix) + self.sep.DOT
        namespace = self.subject + self.sep.DOT + self.domain
        if self.tld:
            namespace += self.sep.DOT + self.tld
        namespace += self.sep.TAG + str(self.version)
        return f"{lp_id}{self.sep.AT}{namespace}".lower()
    
    def split_slug(self, slug: str) -> tuple[str, str, str, str]:
        prefix, namespace = self.split_by_at(slug)
        domain, version = namespace.split(self.sep.TAG)
        return prefix, domain, version
