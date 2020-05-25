import yfinance as yf
from pandas_datareader import data as pdr
import argparse
import mplfinance as mpf
import functions.utility_functions as uf

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--stock', required=True)
    parser.add_argument('--days', default=50)
    args = parser.parse_args()
    args_dict = vars(args)

    print(args_dict['stock'])
    stock = args_dict['stock']
    days = int(args_dict['days'])

    df =uf.get_stock_historical_data(stock)

    df = df.tail(days)

    mpf.plot(df, type='candle', volume=True)

if __name__ == "__main__":

    main()