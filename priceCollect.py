from fastquant import get_pse_data

import pandas as pd
import pandas_datareader.data as web

import matplotlib.pyplot as plt
from matplotlib import style

import datetime as dt
import os
import numpy as np
import bs4 as bs
import pickle #easily save list of companies
import requests

import traceback

style.use('ggplot')

def save_psei_tickers():
    resp = requests.get('https://www.pesobility.com/stock') # insert data source link
    soup = bs.BeautifulSoup(resp.text, "lxml") #turns source code into a BeautifulSoup object
    table = soup.find(text="Symbol").find_parent("table")

    tickers = []
    
    for row in table.findAll('tr')[0:]: #each row, after the header row
        ticker = row.findAll('td')[0].text #first td becomes soup object
        # print(ticker)
        tickers.append(ticker.strip())  #remove "\n"

    with open("READ_WRITE/PSEItickers.pickle", "wb") as f:    #serializes Python objects
        pickle.dump(tickers, f)

    # print(tickers)
    return tickers


# Get full data from fastquant based on saved pickle
def get_data_from_fastquant(reload_psei=True): #change condition if data collection was edited (IPO etc.)
    if not os.path.exists('READ_WRITE/'): #check for directory to save dataset
        os.makedirs('READ_WRITE/')

    if reload_psei:
        tickers = save_psei_tickers()
    else:
        with open("READ_WRITE/PSEItickers.pickle", "rb") as f: #read serialized objects
            tickers = pickle.load(f)

    if not os.path.exists('READ_WRITE/pse_dfs'): #check for directory to save dataset
        os.makedirs('READ_WRITE/pse_dfs')

    x1,y1,z1 = (int(i) for i in input("Starting date (yyyy,mm,dd): ").split(","))
    start = dt.datetime(x1,y1,z1)  #data timeline to be analyzed
    x2,y2,z2 = (int(i) for i in input("Ending date (yyyy,mm,dd): ").split(","))
    end = dt.datetime(x2,y2,z2)
    # end = dt.datetime.now()

    for ticker in tickers:
        try:
            if not os.path.exists('READ_WRITE/pse_dfs/{}.csv'.format(ticker)): # just in case your connection breaks, we'd like to save our progress!
                df = get_pse_data(ticker, str(start.date()), str(end.date()))
                # df.reset_index(inplace=True)
                # df.set_index("Date", inplace=True)
                # df = df.drop("Symbol", axis=1)
                df.to_csv('READ_WRITE/pse_dfs/{}.csv'.format(ticker)) #add each ticker to dataset directory
                print(ticker + ' added')
            else:
                print('Already have {}'.format(ticker))

        except Exception as err:
            print(ticker + ' skipped')
            print(err)
            # traceback.print_exc()

            # if err == """'NoneType' object has no attribute 'empty'""":
            #     continue
            # elif err == """'NoneType' object has no attribute 'to_csv'""":
            #     continue
            # else:
            #   break
            continue

get_data_from_fastquant()
