#!/usr/bin/env python
# coding: utf-8

# # Anna -- Bold -- 24761366

# In[279]:


#importing libraries
import csv
from collections import defaultdict
from typing import List, Dict, Any, Tuple
import numpy as np
import pandas as pd 
import math


# ## 1. File I/O + Parsing

# In[280]:


#read the csv file from the disk
def read_ohlcv(path: str) -> list[dict]:
    rows = []
    try:
        with open(path, 'r', newline='') as file: #opens the file
            csv_dict_reader = csv.DictReader(file, delimiter=',')
            for row in csv_dict_reader: #parses the data 
               rows.append(row)
        return rows
    except: #if the csv file is broken 
        if FileNotFoundError:
            print("File Not Found.")
        else:
            print("Error.")


# ## 2.Summary Function that Returns a Tuple

# In[281]:


#Compute highest high and lowest low from high and low.
#Return a tuple exactly in that order: (symbol, highest_high, lowest_low).

def stock_summary(rows_for_symbol) -> tuple:
    symbol = rows_for_symbol[0]['Ticker'] #pulling the ticker symbol
    highs = []
    lows = []
    for row in rows_for_symbol:
        highs.append(float(row['High'])) #finding the high
        lows.append(float(row['Low'])) #finding the low
    highest_high = max(highs)
    lowest_low = min(lows)
    return (symbol, highest_high, lowest_low)


# ## 3.Technical Analysis Function

# In[282]:


def technical_analysis(closes: list[float]) -> dict: #returns a dict with keys
    closes_array = np.array(closes)
    result = {'sma_30': None, 'ema_30': None, 'three_month_return': None, 'average_vol': None}
    span = 30
   
    #sma_30, 30 day simple moving average
    if len(closes_array) >= 30:
        result['sma_30'] = float(np.mean(closes_array[-30:]))

    #ema_30, 30 day exponential moving average
    if len(closes_array) >= span:
        alpha = 2/(span + 1) 
        ema = closes_array[0]
        for i in closes_array[1:]:
            ema = alpha * i + (1 - alpha) * ema
        result['ema_30'] = float(ema)

    #three month return, last daily return
    if len(closes_array) >= 2:
        result['three_month_return'] = float((closes_array[-1] / closes_array[-2] - 1)) #formula (close_t/close_{t-1}-1)

    #average_vol, sample standard deviation of daily returns over last 20 periods
    if len(closes_array) >= 21: #if there are 20 periods, it needs 21 calculations
        last_periods = closes_array[-21:]
        dailyreturns = (last_periods[1:] / last_periods[:-1] - 1) #formula (close_t/close_{t-1}-1)
        result['average_vol'] = float(np.std(dailyreturns, ddof=1))

    else: 
        print("None")

    return result


# ## 4.Main Program

# In[283]:


def stock_report(path):
    results = {}
    my_rows = read_ohlcv(path) #reads the csv file 

    if not my_rows: #if the file does not upload 
        print("File Not Found.")
        return results
    
    tickers_list = []
    for row in my_rows:
        if row['Ticker'] not in tickers_list:
            tickers_list.append(row['Ticker'])
    tickers_list = sorted(tickers_list) #sorts list alphabetically
    for ticker in tickers_list:
        ticker_rows = []
        for row in my_rows:
            if row['Ticker'] == ticker:
                ticker_rows.append(row)

        #get summary statistics
        symbol, highest_high, lowest_low = stock_summary(ticker_rows)
        
        #get closing prices for technical analysis
        closes = []
        for row in ticker_rows:
            closes.append(float(row['Close']))
        tech = technical_analysis(closes)
        
        #add to results dictionary
        results[ticker] = {
            'highest_high': highest_high,
            'lowest_low': lowest_low,
            'tech': tech
        }
    
    return results

def print_results(results):
     for ticker, data in results.items():
        print(f"{ticker}:")
        print(f" \n Highest High: {data['highest_high']}")
        print(f" \n Lowest Low: {data['lowest_low']}")
        print(f" \n Tech: {data['tech']   }")


# ## Run

# In[284]:


stock_report('stock_data_july_to_september.csv')

