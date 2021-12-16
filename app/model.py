from app.factory import create_file_grabber
from app.data_source import DataSource
from app.database_controller import DatabaseController
from app.datamodel import DataModel


class Model:

    def __init__(self):
        self.database_controller = DatabaseController()
        self.datasource = DataSource()

    def init_proccess(self):
        try:
            file_grabber = create_file_grabber()
        except Exception as ex:
            print("getting resource handler failed")
            exit()
        try:
            self.datasource.get_data(file_grabber)        
        except Exception as ex:
            print("grabbing given file failed")
            exit()
        try:
            self.database_controller.insert_data(self.datasource.dataobject)
        except Exception as ex:
            print("loading data into DB failed")
            exit()

        print("file has been loaded into DB")



