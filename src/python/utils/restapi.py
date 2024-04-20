import requests
import pandas as pd
import os

def api_get(url:str)->pd.DataFrame:
    response=requests.get(url)
    return pd.DataFrame(response.json())

def get_env_licence(vendor:str)->str|None:
    return os.getenv(vendor+'_licence')
