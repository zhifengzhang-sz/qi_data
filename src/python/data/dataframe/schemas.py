import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema, Check, Index

KLineSchema=DataFrameSchema(
    {'Open':Column(float)
    ,'High':Column(float)
    ,'Low':Column(float)
    ,'Close':Column(float)
    ,'Adj Close':Column(float)
    ,'Volume':Column(float)
    ,'Amount':Column(float,required=False)
    },
    index=Index(pd.Timestamp,name='Date'),
    strict='filter'
)

MACDSchema=DataFrameSchema(
    {'macd':Column(float,nullable=True)
    ,'signal':Column(float,nullable=True)
    ,'hist':Column(float,nullable=True)
    },
    index=Index(pd.Timestamp,name='Date'),
    strict='filter'
)

BuySchema=DataFrameSchema(
    {'Buy':Column(float)
    ,'NShare':Column(int)
    },
    index=Index(pd.Timestamp,name='Date'),
    strict='filter'
)

SellSchema=DataFrameSchema(
    {'Sell':Column(float)
    ,'NShare':Column(int)
    },
    index=Index(pd.Timestamp,name='Date'),
    strict='filter'
)