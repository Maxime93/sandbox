import csv

import config
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# get all symbol prices
# prices = client.get_all_tickers()
# for price in prices:
#     print(price)

# Write candlestick data to file
# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
# with open("15mins.csv", "w") as f:
#     writer = csv.writer(f, delimiter=',')
#     for candle in candles:
#         writer.writerow(candle)

candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "20 May, 2020")
with open("2012_2020.csv", "w") as f:
    writer = csv.writer(f, delimiter=',')
    for candle in candles:
        writer.writerow(candle)