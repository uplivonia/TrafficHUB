from abc import ABC, abstractmethod
from typing import Any, Dict

class Connector(ABC):
    """Base connector interface for a network."""

    def __init__(self, credentials: Dict[str, Any] | None = None):
        self.credentials = credentials or {}

    @abstractmethod
    def meta(self) -> Dict[str, Any]:
        ...

    @abstractmethod
    def post(self, channel: str, content: Dict[str, Any]) -> Dict[str, Any]:
        ...

    def health(self) -> Dict[str, Any]:
        return {"ok": True}
