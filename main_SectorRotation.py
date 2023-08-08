# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:00:04 2023

@author: asingh
"""

import creds #my credentials for API are stored
from jsonAPIcall import get_json_data 
import pandas as pd
import datetime

date_market_bottom= datetime.date(2022,10,9) #The market bottom of S&P500 during the 2022 bear market

df_companyProfiles= pd.read_excel('companyProfile_NYSE_NASDAQ_NSE_TSX_BSE.xlsx', sheet_name='Sheet1') #contains stock symbols from various exchanges, and their profiles: companyName, industry, sector etc. 
profileColumns= ['symbol','companyName','sector','industry','ipoDate','currency','country']

df_companyProfiles= df_companyProfiles[profileColumns]

df_bottoms = pd.DataFrame(columns=['symbol','sector','industry','country','date_bottom', 'close_bottom'])

for symbol in df_companyProfiles['symbol']:
    
    sector= df_companyProfiles[df_companyProfiles['symbol'] == symbol]['sector']
    industry= df_companyProfiles[df_companyProfiles['symbol'] == symbol]['industry']
    country= df_companyProfiles[df_companyProfiles['symbol'] == symbol]['country']
        
    url1= "https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?serietype=line&apikey={my_api_key}".format(symbol=symbol, my_api_key=creds.my_api_key)
    
    VarDict= {} #defining an empty dictionary object
    VarDict= get_json_data(url1) #request returns dictionary
    
    if VarDict =={}: # if dictionary is empty because ticker symbol didn't exist at that time then skip adding it
       continue
   
    df_symbol= pd.DataFrame(VarDict['historical']) #accessing just the historical column of the dictionary returned to get the historical stock prices
    df_symbol['date'] = pd.to_datetime(df_symbol['date']).dt.date
    
       
    mask = (df_symbol['date'] >= date_market_bottom - pd.Timedelta(days=365)) & (df_symbol['date'] <= date_market_bottom + pd.Timedelta(days=365)) 
   
    df_filtered = df_symbol[mask]
    
    if df_filtered.empty:
        continue
    
    # Find the row with the minimum 'close'; 'close' is the closing price of the stock
    min_row = df_filtered.loc[df_filtered['close'].idxmin()] 
    
    df_bottoms = pd.concat([df_bottoms, pd.DataFrame({'symbol': symbol,'sector': sector,'industry': industry,'country': country,'date_bottom': min_row['date'], 'close_bottom': min_row['close']})], axis= 0)
 
df_bottoms.to_excel('stock_bottoms.xlsx', index=False)

#df_bottoms= pd.read_excel('stock_bottoms_final.xlsx') # uncomment to read from the data provided in the excel in repo

# Filtering for only US stocks
df_bottoms_US= df_bottoms[df_bottoms['country']=='US']
df_bottoms_US.reset_index(drop=True, inplace=True)
df_bottoms_US['date_bottom']= pd.to_datetime(df_bottoms_US['date_bottom']).dt.date

df_bottoms_US['days_wrBottom'] = df_bottoms_US['date_bottom'].apply(lambda x: (x - date_market_bottom).days)
df_sectorBottoms_avg_dayswrBottom = df_bottoms_US.groupby('sector')['days_wrBottom'].mean().reset_index()

