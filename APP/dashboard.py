from typing import no_type_check
import os
from pandas import read_csv
from dotenv import load_dotenv

load_dotenv()

key1 = os.environ.get("nyc_odata_api_key")
key2 = os.environ.get("alphavantage_api_key")

#function that filters then creates a new column that does a percent change per year of the filtered data
#four plotly charts: yoy price increase, yoy inflation increase, combined line charts of yoy, and inflation adjusted rental increase
#undervalued/overvalued yoy change of prices v inflation



nyc_odata_csv_filepath = f"https://data.cityofnewyork.us/resource/9ck6-2jew.csv?$limit=28500&$$app_token={key1}"
nyc_odata_df = read_csv(nyc_odata_csv_filepath)
alphavantage_csv_filepath = f"https://www.alphavantage.co/query?function=INFLATION&datatype=csv&apikey={key2}"
print(nyc_odata_csv_filepath)
print(alphavantage_csv_filepath)
print(nyc_odata_df.columns)

alphavantage_df = read_csv(alphavantage_csv_filepath)
print(alphavantage_df.columns)

neighborhood = input("Please type in a NYC neighborhood you'd like to analyze:") # @param ['BEDFORD STUYVESANT', 'CHELSEA', 'ELMHURST' "Other"]
#add error
neighborhood = neighborhood.upper()
print(neighborhood)

#try:
#    
#    
#    nyc_odata_df["boro_block_lot"]
#    print(nyc_odata_df.columns)
#except:
#    print("OOPS: Invalid entry. Please try again with a different neighborhood.")




