from url import URL
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

class Request:
    handlers: dict[str, 'RequestHandler'] = {}

    @classmethod
    def register_handler(cls, scheme: str, handler: 'RequestHandler'):
        cls.handlers[scheme] = handler

    def fetch(self, url: 'URL', headers: Optional[dict[str, str]] = None) -> str:
        assert url.scheme in self.handlers, f"No handler registered for scheme: {url.scheme}"
        return self.handlers[url.scheme].fetch(url, headers)

class RequestHandler(ABC):
    @abstractmethod
    def fetch(self, url: 'URL', headers: Optional[dict[str, str]] = None) -> str:
        pass
