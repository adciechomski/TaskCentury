from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class GetFile(ABC):
    resource_location: str
    credentials: Optional[object] = None

    @abstractmethod
    def acquire_resource(self):
        pass
