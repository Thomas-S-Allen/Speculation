import datetime
import matplotlib.pyplot as plt
import numpy as np

def parse_option_string(string):

    print(string)

    string_list = string.split()
    print(string_list)

    print(len(string_list))

    if len(string_list) == 9:

        side = str(string_list[0])
        multiplier = int(string_list[1])
        stock = str(string_list[2])
        expiration = str(' '.join([string_list[3],string_list[4]]))
        strike = float(string_list[5])
        type = str(string_list[6])
        premium = float(string_list[8])

    if len(string_list) == 10:

        side = str(string_list[0])
        multiplier = int(string_list[1])
        stock = str(string_list[2])
        expiration = str(' '.join([string_list[3],string_list[4],\
                                   string_list[5]]))
        strike = float(string_list[6])
        type = str(string_list[7])
        premium = float(string_list[9])

    print("side")
    print(side)
    if side[0].lower() == 'b':
        side = 'buy'
    else:
        side = 'sell'

    return side, multiplier, stock, expiration, strike, type, premium


def check_trading_day(date):

    markets_closed = ['2020-01-01',\
                      '2020-01-20',\
                      '2020-02-17',\
                      '2020-04-10',\
                      '2020-05-25',\
                      '2020-07-03',\
                      '2020-09-07',\
                      '2020-11-26',\
                      '2020-12-25']

    if date in markets_closed:
        return False
    else:
        return True

def check_weekday(date):

    if date.weekday()==5 or date.weekday()==6:
        return False
    else:
        return True






