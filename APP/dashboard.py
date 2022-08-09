from typing import no_type_check
import os
from pandas import read_csv
from dotenv import load_dotenv

load_dotenv()

key1 = os.environ.get("nyc_odata_api_key")
key2 = os.environ.get("alphavantage_api_key")
nyc_odata_csv_filepath = f"https://data.cityofnewyork.us/resource/9ck6-2jew.csv?$limit=27000&$$app_token={key1}"
alphavantage_csv_filepath = f"https://www.alphavantage.co/query?function=INFLATION&datatype=csv&apikey={key2}"
print(nyc_odata_csv_filepath)
print(alphavantage_csv_filepath)

alphavantage_df = read_csv(alphavantage_csv_filepath)
print(alphavantage_df.columns)
nyc_odata_df = read_csv(nyc_odata_csv_filepath)
print(nyc_odata_df.columns)
    

