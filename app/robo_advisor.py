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

print("-------------------------")
print("Welcome to Robo-Advisor! Analyze your stocks instantly and easily here!")
print("-------------------------")
print("Below, you are asked to input a stock ticker. When you are done, enter 'done'.")
print("-------------------------")
print("-------------------------")

ticker = ""
ticker_list = []

while(str.casefold(ticker) != str.casefold("Done")):
    ticker = input("Enter a stock ticker here:") 
    if len(ticker) == 0 or len(ticker) > 5 or ticker.isalpha() == False: 
        print("Oops! Please enter a valid stock ticker, such as 'MSFT'.")
        continue
    else:
        if str.casefold(ticker) != str.casefold("Done"):
            ticker_list.append(ticker.upper())

print(ticker_list)






requests_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(requests_url)



# print("-------------------------")
# print("SELECTED SYMBOL: XYZ")
# print("-------------------------")
# print("REQUESTING STOCK MARKET DATA...")
# print("REQUEST AT: 2018-02-20 02:00pm")
# print("-------------------------")
# print("LATEST DAY: 2018-02-20")
# print("LATEST CLOSE: $100,000.00")
# print("RECENT HIGH: $101,000.00")
# print("RECENT LOW: $99,000.00")
# print("-------------------------")
# print("RECOMMENDATION: BUY!")
# print("RECOMMENDATION REASON: TODO")
# print("-------------------------")
# print("HAPPY INVESTING!")
# print("-------------------------")