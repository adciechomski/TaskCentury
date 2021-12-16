from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, TIMESTAMP, Float
from sqlalchemy.orm import sessionmaker, mapper

metadata = MetaData()
cash_data = Table('cash_data', metadata,
    Column('Id', Integer, primary_key=True, autoincrement=True),
    Column('Date', TIMESTAMP),
    Column('Next_Trading_Day', TIMESTAMP),
    Column('Index_Symbol', String(255)),
    Column('Internal_Key', String(255)),
    Column('ISIN', String(255)),
    Column('Company_Name', String(255)),
    Column('Corporate_Action_Type', String(255)),
    Column('Cash_Dividend_Gross_Amount', Float),
    Column('Cash_Dividend_Net_Amount', Float),
    Column('Cash_Dividend_Currency', String(255)),
    Column('Corporate_Action_Description', String(255)),
    Column('Index_Shares', Integer),
    Column('Index_New_Shares', Integer),
    Column('Free_Float', Float),
    Column('New_Free_Float', Float),
    Column('Close_Local', Float),
    Column('Adjusted_Close_local_Priceindex', Float),
    Column('Adjusted_Close_local_Returnindex_net', Float),
    Column('Adjusted_Close_local_Returnindex_gross', Float),
    Column('PriceIndex_Adj_Factor', Integer),
    Column('ReturnIndex_Adj_Factor_net', Float),
    Column('ReturnIndex_Adj_Factor_gross', Float)
    )

@dataclass
class DataModel:
    __tablename__ = "cash_data"
    Id: int = None 
    Date: str = None
    Next_Trading_Day: str = None
    Index_Symbol: str = None
    Internal_Key: str = None
    ISIN: str = None
    Company_Name: str = None
    Corporate_Action_Type: str = None
    Cash_Dividend_Gross_Amount: str = None
    Cash_Dividend_Net_Amount: str = None
    Cash_Dividend_Currency: str = None
    Corporate_Action_Description: str = None
    Index_Shares: str = None
    Index_New_Shares: str = None
    Free_Float: str = None
    New_Free_Float: str = None
    Close_Local: str = None
    Adjusted_Close_local_Priceindex: str = None
    Adjusted_Close_local_Returnindex_net: str = None
    Adjusted_Close_local_Returnindex_gross: str = None
    PriceIndex_Adj_Factor: str = None
    ReturnIndex_Adj_Factor_net: str = None
    ReturnIndex_Adj_Factor_gross: str = None