import numpy as np
import talib

# close = np.random.random(100)
# print(close)
# print()

# output = talib.SMA(close)
# print(output)
# print()

# upper, middle, lower = talib.BBANDS(close, matype=talib.MA_Type.T3)
# print(upper)
# print(middle)
# print(lower)

# rsi = talib.RSI(close)
# print(rsi)

data = np.genfromtxt('15mins.csv', delimiter=',')
# Exctract 4th column, which is the closing price
close = data[:,4]
print(close)
print()

rsi = talib.RSI(close)
print(rsi)