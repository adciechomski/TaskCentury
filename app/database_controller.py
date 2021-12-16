from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import sessionmaker, mapper
from app.datamodel import *

class DatabaseController:

    def __init__(self):
        self.engine = create_engine('sqlite:///cashdb.db', echo=True)

    def insert_data(self, data_object):
        map_object = lambda record: DataModel(**record)

        mapper(DataModel, cash_data)
        metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)()

        objects = map(map_object, data_object)
        session.bulk_save_objects(list(objects))
        session.commit()