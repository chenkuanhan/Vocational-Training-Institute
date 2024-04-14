import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime, time
from io import BytesIO
import base64
import threading
import pandas as pd

data_2330 = yf.Ticker("2330.TW")

print(data_2330)

history_data = data_2330.history(period="1mo")

period_data = yf.download("2330.TW", '2024-01-01', '2024-03-20')

def get_stock_data(symbol,start,stop):
    data = yf.download(symbol,start,stop)
    return data
 

data = get_stock_data("2330.TW", '2024-01-01', '2024-03-20')


def plot_trend(data, volume=False):
    #mpf.plot(data, type='line')
    mpf.plot(data, type='line', volume=False)
    
def plot_historical(data):
    mpf.plot(data, type='line', volume=True)
    img = BytesIO()#產生圖片物件(2禁制)
    plt.savefig(img, format='png')
    img.seek(0)
    
    historical_polt = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return historical_polt


def plot_trend_avg(data):
    mpf.plot(data, type='line', volume=True, mav=(5,10,20))
    
    


if __name__ == "__main__":
    data = get_stock_data("2330.TW", '2024-01-01', '2024-03-20')
    plot_trend(data)
    plot_historical(data)
    plot_trend_avg(data)
    