from typing import no_type_check
import os
import pandas as pd
from pandas import read_csv
from dotenv import load_dotenv
from tkinter import *
import plotly.graph_objects as go






load_dotenv()

key1 = os.environ.get("nyc_odata_api_key")
key2 = os.environ.get("alphavantage_api_key")

#function that filters then creates a new column that does a percent change per year of the filtered data
#four plotly charts: yoy price increase, yoy inflation increase, combined line charts of yoy, and inflation adjusted rental increase
#undervalued/overvalued yoy change of prices v inflation



nyc_odata_csv_filepath = f"https://data.cityofnewyork.us/resource/9ck6-2jew.csv?$limit=28500&$$app_token={key1}"
nyc_odata_df = read_csv(nyc_odata_csv_filepath)
nyc_odata_df = nyc_odata_df.dropna(subset=["neighborhood"])
alphavantage_csv_filepath = f"https://www.alphavantage.co/query?function=CPI&interval=semiannual&datatype=csv&apikey={key2}"




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
filtered_df = nyc_odata_df[nyc_odata_df["neighborhood"].str.contains(selection)]
rent_price_df = filtered_df.groupby("report_year").market_value_per_sqft.mean().to_frame().reset_index()
rent_price_df.rename(columns={'index':'report_year'})
rent_price_df = rent_price_df.sort_values(by='report_year', ascending=FALSE)





#print(alphavantage_df)
alphavantage_df["year"]=pd.DatetimeIndex(alphavantage_df['timestamp']).year
alphavantage_df["month"]=pd.DatetimeIndex(alphavantage_df['timestamp']).month
alphavantage_df = alphavantage_df[alphavantage_df["month"] == 1]

m = alphavantage_df.year.isin(filtered_df.report_year)
alphavantage_df = alphavantage_df[m]
alphavantage_df = alphavantage_df.sort_values(by='year', ascending = FALSE)


early_rent = rent_price_df.iloc[-1].to_dict()["market_value_per_sqft"]
latest_rent = rent_price_df.iloc[0].to_dict()["market_value_per_sqft"]
early_cpi = alphavantage_df.iloc[-1].to_dict()["value"]
latest_cpi = alphavantage_df.iloc[0].to_dict()["value"]
valuation_variable = (latest_rent -early_rent) - (latest_rent * (early_cpi/latest_cpi))
try:
    rent_price_df.iloc[1]
except:
    print("Not enough data")
    quit()


print(valuation_variable)

if valuation_variable > 0:
    print("UNDERVALUED")
elif valuation_variable == 0:
    print("FAIR MARKET VALUE")
else:
    print("OVERVALUED")

rent_prices = go.Scatter(x=rent_price_df['report_year'], y=rent_price_df['market_value_per_sqft'], name='Average Rent Price Per Sqft')
cpi_trend = go.Scatter(x=alphavantage_df['year'], y=alphavantage_df['value'], name='CPI Index')

fig = go.Figure(data=[rent_prices, cpi_trend])
fig.update_layout(title=f"{selection} Average Rent v CPI Index")
fig.show()



















