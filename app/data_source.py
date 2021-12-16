from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict
import datetime
from app.file_grabber.get_file import GetFile

@dataclass
class DataSource:
    file: str = None
    headers: List[str] = None
    dataobject: Dict[int, Dict[str, str]] = field(default_factory=dict)

    def get_data(self, file_grabber: GetFile):    
        self.file, self.headers = file_grabber.acquire_resource()
        self.preprocess_data()

    def preprocess_data(self):
        list_of_records = []
        headers = self.headers[0].split(";")
        n = 0
        for record in self.file:
            record_list = record[0].split(";")
            list_of_records.append({key: value for key, value in zip(headers, record_list)})
            n += 1
            print(record)
        
        list_of_records = map(self.set_data_types, list_of_records)
        self.dataobject = list(list_of_records)


    def set_data_types(self, record):
        record['Date'] = datetime.datetime.strptime(record['Date'], "%Y-%m-%d")
        record['Next_Trading_Day'] = datetime.datetime.strptime(record['Next_Trading_Day'], "%Y-%m-%d") 
        record['Cash_Dividend_Gross_Amount'] = float(record['Cash_Dividend_Gross_Amount'])
        record['Cash_Dividend_Net_Amount'] = float(record['Cash_Dividend_Net_Amount'])
        record['Index_Shares'] = int(record['Index_Shares'])
        record['Index_New_Shares'] = int(record['Index_New_Shares'])
        record['Free_Float'] = float(record['Free_Float'])
        record['New_Free_Float'] = float(record['New_Free_Float'])
        record['Close_Local'] = float(record['Close_Local'])
        record['Adjusted_Close_local_Priceindex'] = float(record['Adjusted_Close_local_Priceindex'])
        record['Adjusted_Close_local_Returnindex_net'] = float(record['Adjusted_Close_local_Returnindex_net'])
        record['Adjusted_Close_local_Returnindex_gross'] = float(record['Adjusted_Close_local_Returnindex_gross'])
        record['PriceIndex_Adj_Factor'] = int(record['PriceIndex_Adj_Factor'])
        record['ReturnIndex_Adj_Factor_net'] = float(record['ReturnIndex_Adj_Factor_net'])
        record['ReturnIndex_Adj_Factor_gross'] = float(record['ReturnIndex_Adj_Factor_gross'])
        return record

    def validate_data(self):
        pass
