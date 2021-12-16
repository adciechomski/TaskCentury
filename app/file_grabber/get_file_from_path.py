from abc import ABC, abstractmethod
from dataclasses import dataclass
import csv
import os

from app.file_grabber.get_file import GetFile

@dataclass
class GetFileFromPath(GetFile):
    resource_location: str

    def acquire_resource(self):
        self.resource_location = os.path.abspath(self.resource_location)
        print(f"getting file from path: {self.resource_location}")     
        try:   
            file = open(self.resource_location) #("C:\sqlite\data.csv")
        except FileNotFoundError as e:
            print("file not found - try again")
            exit()
        csvreader = csv.reader(file)
        headers = next(csvreader)
        print(headers)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()
        return rows, headers
