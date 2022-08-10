from typing import no_type_check
import os
from pandas import read_csv
from dotenv import load_dotenv
from tkinter import *


load_dotenv()

key1 = os.environ.get("nyc_odata_api_key")
key2 = os.environ.get("alphavantage_api_key")

#function that filters then creates a new column that does a percent change per year of the filtered data
#four plotly charts: yoy price increase, yoy inflation increase, combined line charts of yoy, and inflation adjusted rental increase
#undervalued/overvalued yoy change of prices v inflation



nyc_odata_csv_filepath = f"https://data.cityofnewyork.us/resource/9ck6-2jew.csv?$limit=28500&$$app_token={key1}"
nyc_odata_df = read_csv(nyc_odata_csv_filepath)
nyc_odata_df = nyc_odata_df.dropna(subset=["neighborhood"])
alphavantage_csv_filepath = f"https://www.alphavantage.co/query?function=INFLATION&datatype=csv&apikey={key2}"
print(nyc_odata_csv_filepath)
print(alphavantage_csv_filepath)


alphavantage_df = read_csv(alphavantage_csv_filepath)

neighborhoods_df = nyc_odata_df["neighborhood"]

neighborhoods = neighborhoods_df.values.tolist()
unique_neighborhoods = list(set(neighborhoods))

OPTIONS = unique_neighborhoods
master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

#def ok():
#    selection = variable.get()
#    #print ("value is:" + variable.get())
#    str(selection)
#    #print(nyc_odata_df.filter(like=selection, axis="neighborhood"))
#    
#    
#
#    
#
#button = Button(master, text="Confirm Selection", command=ok)
#button.pack()

# Button for closing
exit_button = Button(master, text="Display Results", command=master.destroy)
exit_button.pack()

mainloop()

selection = variable.get()
print ("value is:" + variable.get())
filttered_df = nyc_odata_df[nyc_odata_df["neighborhood"].str.contains(selection)]
rent_price_df = nyc_odata_df.groupby("report_year").market_value_per_sqft.mean()



#print(type(unique_neighborhoods))
#print(unique_neighborhoods)
#neighborhood = input("Please type in a NYC neighborhood you'd like to analyze:") # @param ['BEDFORD STUYVESANT', 'CHELSEA', 'ELMHURST' "Other"]
#add error



#try:
#    
#    
#    nyc_odata_df["boro_block_lot"]
#    print(nyc_odata_df.columns)
#except:
#    print("OOPS: Invalid entry. Please try again with a different neighborhood.")




