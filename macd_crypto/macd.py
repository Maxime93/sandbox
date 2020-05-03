import pandas as pd
from stockstats import StockDataFrame

def read_dataset(filename):
    print('Reading data from %s' % filename)
    df = pd.read_csv(filename)
    df.datetime = pd.to_datetime(df.datetime) # change type from object to datetime
    df = df.set_index('datetime')
    df = df.sort_index() # sort by datetime
    print(df.shape)
    return df

def run(filename):
    df = read_dataset(filename)
    df = StockDataFrame.retype(df)
    df['macd'] = df.get('macd') # calculate MACD
    print(df)

if __name__ == "__main__":
    filename = "BTC_USD_Bitstamp_day_2020-05-02.csv"
    run(filename)