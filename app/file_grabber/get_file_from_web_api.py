from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from app.file_grabber.get_file import GetFile

@dataclass
class GetFileFromWebApi(GetFile):
    resource_location: str
    credentials: Optional[object] = None

    def acquire_resource(self):
        print("getting file from path")


