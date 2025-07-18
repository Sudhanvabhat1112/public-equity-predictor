import numpy as np
import pandas as pd
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:\\Proj 3\\public-equity-predictor\\api_key.env")
API_KEY = os.getenv("API_KEY")

symbol=input("Enter the ticker symbol (name in the stock market) of the company(GOOGL for google) :")
url = "https://www.alphavantage.co/query"
params_high = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",  # last 100 days; 
        "apikey": API_KEY           
    }
params_dema={
    "function": "DEMA",
    "symbol": symbol,               
    "time_period": 14,               
    "series_type": "high",          
    "interval":"daily",
    "apikey": API_KEY
}
params_ema={
    "function": "EMA",
    "symbol": symbol,                
    "time_period": 14,               
    "series_type": "high",          
    "interval":"daily",
    "apikey": API_KEY
}
params_adx={
    "function": "ADX",
    "symbol": symbol,                
    "time_period": 100,               
    "interval":"daily",
    "apikey": API_KEY
}
params_cci={
    "function": "CCI",
    "symbol": symbol,                
    "time_period": 100,               
    "interval":"daily",
    "apikey": API_KEY
}
params_rsi={
    "function": "RSI",
    "symbol": symbol,                
    "time_period": 100,               
    "interval":"daily",
    "series_type": "high",
    "apikey": API_KEY
}
params_sma={
    "function": "SMA",
    "symbol": symbol,                
    "time_period": 100,               
    "interval":"daily",
    "series_type": "high",
    "apikey": API_KEY
}
params_tsm = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSM",
        "outputsize": "compact",  
        "apikey": API_KEY           
    }
params_nvidia = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "NVDA",
        "outputsize": "compact",   
        "apikey": API_KEY           
    }
params_microsoft = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "MSFT",
        "outputsize": "compact",   
        "apikey": API_KEY           
    }
params_meta = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "META",
        "outputsize": "compact",   
        "apikey": API_KEY           
    }


response1 = requests.get(url, params=params_high)
data_high = response1.json()      
response2 = requests.get(url, params=params_dema)
data_dema = response2.json()
response3 = requests.get(url, params=params_ema)
data_ema = response3.json()
response4 = requests.get(url, params=params_adx)
data_adx = response4.json() 
response5 = requests.get(url, params=params_cci)
data_cci = response5.json() 
response6 = requests.get(url, params=params_rsi)
data_rsi = response6.json() 
response7 = requests.get(url, params=params_sma)
data_sma = response7.json() 
response8 = requests.get(url, params=params_tsm)
data_tsm = response8.json() 
response9 = requests.get(url, params=params_nvidia)
data_nvidia = response9.json() 
response10 = requests.get(url, params=params_microsoft)
data_microsoft = response10.json() 
response11 = requests.get(url, params=params_meta)
data_meta = response11.json() 


time_series = data_high["Time Series (Daily)"]   
dates = sorted(time_series.keys(), reverse=True)    #reverse sorts our data_high with date
dema=data_dema["Technical Analysis: DEMA"]
ema = data_ema["Technical Analysis: EMA"] 
adxr = data_adx["Technical Analysis: ADX"] 
cci = data_cci["Technical Analysis: CCI"] 
rsi = data_rsi["Technical Analysis: RSI"] 
sma = data_sma["Technical Analysis: SMA"] 
tsm = data_tsm["Time Series (Daily)"]
nvidia = data_nvidia["Time Series (Daily)"]
microsoft = data_microsoft["Time Series (Daily)"]
meta = data_meta["Time Series (Daily)"]



stock_data = []
for i in dates:
    daily_data = time_series[i]
    daily_data_tsm = tsm[i]
    daily_data_nvi = nvidia[i]
    daily_data_mic = microsoft[i]
    daily_data_meta = meta[i]
    high_price = float(daily_data["2. high"])
    tsm_val=float(daily_data_tsm["2. high"])
    nvi_val=float(daily_data_nvi["2. high"])
    mic_val=float(daily_data_mic["2. high"])
    meta_val=float(daily_data_meta["2. high"])
    dema_value=float(dema.get(i, {}).get("DEMA", 0))
    ema_value = float(ema.get(i, {}).get("EMA", 0))
    adx_val = float(adxr.get(i, {}).get("ADX", 0))
    cci_val = float(cci.get(i, {}).get("CCI", 0))
    rsi_val=float(rsi.get(i, {}).get("RSI", 0))
    sma_val=float(sma.get(i, {}).get("SMA", 0))

    stock_data.append({
        "Date": i,
        "High": high_price,
        "DEMA":dema_value,
        "EMA": ema_value,
        "ADX": adx_val,
        "CCI": cci_val,
        "RSI":rsi_val,
        "SMA":sma_val,
        "TMSC":tsm_val,
        "NVIDIA":nvi_val,
        "Microsoft":mic_val,
        "META":meta_val
         })
df = pd.DataFrame(stock_data)

df.to_csv("C:\\Proj 3\\public-equity-predictor\\alphabet_stock_analysis.csv", index=False)

print(df)
