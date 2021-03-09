import datetime
from datetime import date
import time
import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS, Please set env var called 'ALPHAVANTAGE_API_KEY'")

if API_KEY == "OOPS, Please set env var called 'ALPHAVANTAGE_API_KEY'":
    print(API_KEY)
    print("Exiting program...")
    quit()

def to_usd(my_price):
    return f"${my_price:,.2f}" # Credit to the man, the myth, the legend, Michael Rossetti

print("-------------------------")
print("Welcome to Robo-Advisor! Analyze your stocks instantly and easily here!")
print("-------------------------")
print("Below, you are asked to input a stock ticker. When you are done, enter 'done'. \n(Maximum 5 Stocks)")
print("-------------------------")
print("-------------------------")

ticker = ""
ticker_list = []
counter = 0 # A maximum of 5 stocks can be analyzed at one time; this is AlphaVantage API's rate limit.

while(str.casefold(ticker) != str.casefold("Done") and counter < 5):
    ticker = input("Enter a stock ticker here: ") 
    if len(ticker) == 0 or len(ticker) > 5 or ticker.isalpha() == False: 
        print("Oops! Please enter a valid stock ticker, such as 'MSFT'.")
        continue
    else:
        if str.casefold(ticker) != str.casefold("Done"):
            ticker_list.append(ticker.upper())
            counter += 1

for stock_ticker in ticker_list:
    requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock_ticker +"&apikey={API_KEY}"
    response = requests.get(requests_url)
    ticker_info = json.loads(response.text)
    try:
        ticker_time_series = ticker_info["Time Series (Daily)"]
    except:
        print("Oops! Robo-Advisor was unable to retrieve data for", stock_ticker + ".\nPlease Double Check that the ticker is spelled correctly.")
        print("Exiting program...")
        exit()

    records = []

    for date1, daily_data in ticker_time_series.items(): # had to name date "date1" because it interfered with stating current time in final output.
        record = {
            "timestamp": date1,
            "open": float(daily_data["1. open"]),
            "high": float(daily_data["2. high"]),
            "low": float(daily_data["3. low"]),
            "close": float(daily_data["4. close"]),
            "volume": int(daily_data["5. volume"]),
        }
        records.append(record)

    records_df = pd.DataFrame(records)
    records_df.to_csv("data/prices_" + stock_ticker)

    recent_highs = []
    recent_lows = []

    for record in records:
        recent_highs.append(record["high"])
        recent_lows.append(record["low"])

    symbol = stock_ticker
    latest_data = records[0]["timestamp"]
    latest_close = records[0]["close"]
    recent_high = max(recent_highs)
    recent_low = min(recent_lows)
    recommendation = ""

    if recent_high < (2 * recent_low) and latest_close > (recent_low * 1.1):
        recommendation = "BUY!"
    else:
        recommendation = "DON'T BUY!"

    if recommendation == "BUY!":
        explain = str(symbol + " stock is not too risky and has recorded steady gains over the past 100 days.")
    else:
        explain = str(symbol + " stock is either too risky, or is not growing enough - or worse - both!")

    e = datetime.datetime.now() # helpful website to put time in attractive format: https://phoenixnap.com/kb/get-current-date-time-python

    print("-------------------------")
    print("SELECTED SYMBOL:", symbol)
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT:", date.today(), e.strftime("%I:%M %p"))
    print("-------------------------")
    print("LATEST DATA FROM:", latest_data)
    print("LATEST CLOSE:", to_usd(latest_close))
    print("RECENT HIGH:", to_usd(recent_high))
    print("RECENT LOW:", to_usd(recent_low))
    print("-------------------------")
    print("RECOMMENDATION:", recommendation)
    print("RECOMMENDATION REASON:", explain)
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------\n")