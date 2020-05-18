import statistics
import utility_functions as uf
import numpy as np


def stock_random_walk(df,stdev,period,path=False):

    price = float(df['Close'].tail(1))

    #print(price)

    price_path = [price]

    index=0
    while index < period:

        price = price + np.random.normal(0,stdev,1)
        price_path.append(float(price))

        index = index + 1

    if path==False:
        return price_path[-1]
    else:
        return price_path


def many_random_walks(df,stdev,period,iterations=10000):

    prices = []
    index = 0
    while index < iterations:

        prices.append(stock_random_walk(df,stdev,period,path=False))

        index = index + 1

    return prices

