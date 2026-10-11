"""Minimum policy boundaries; not production AEGIS."""
from dataclasses import dataclass

class PolicyDenied(ValueError):
    pass

@dataclass(frozen=True)
class RequestPolicy:
    provider: str
    purpose: str
    allow_cloud: bool = False
    personal_ack: bool = False

    def check(self) -> None:
        if self.provider not in {"agy", "ollama", "gemini-api"}:
            raise PolicyDenied("Unknown provider; default-deny")
        if self.purpose not in {"personal", "fleet"}:
            raise PolicyDenied("Purpose must be personal or fleet")
        if self.provider == "agy":
            if self.purpose != "personal" or not self.personal_ack:
                raise PolicyDenied("Antigravity CLI is personal-only and requires --personal-ack")
            if not self.allow_cloud:
                raise PolicyDenied("Cloud inference requires --allow-cloud")
        elif self.provider == "gemini-api" and not self.allow_cloud:
            raise PolicyDenied("Cloud inference requires --allow-cloud")
