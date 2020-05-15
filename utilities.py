import datetime
import matplotlib.pyplot as plt
import numpy as np

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


def pl_plot(strike, premium,type='call',order='buy'):

    fig = plt.figure(figsize=(8, 5))
    #plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

    prange = 10

    strike = float(strike)
    premium = float(premium)

    # Define flat part of P&L curve
    flat_curve_y = np.array([-premium, -premium])

    if type=='call':

        ptype = "Call"

        flat_curve_x = np.array([0, strike])

        xmax = (strike + premium) + premium
        if strike - premium > 0:
            xmin = strike - premium
        else:
            xmin = 0

        xrange = [xmin,xmax]

        slant_curve_x = np.array([strike, xmax])
        slant_curve_y = np.array([-premium, premium])

        if order=='buy':

            porder = "Buy"

            # Note slope = 1, intercept = -(strike+mark)

        if order=='sell':

            porder = "Sell"

            # Flat part of curve now greater than 0
            flat_curve_y = -flat_curve_y

            # Note slope = -1, intercept = strike+mark

            slant_curve_y = -slant_curve_y

    if type=='put':

        ptype = "Put"

        flat_curve_x = np.array([strike, strike * 1000])

        xmax = strike + premium
        if (strike - premium) - premium > 0:
            xmin = (strike - premium) - premium
        else:
            xmin = 0


        xrange = np.array([xmin,xmax])

        slant_curve_x = np.array([xmin, strike])
        slant_curve_y = np.array([premium, -premium])

        if order=='buy':

            porder = "Buy"

            # Note slope = -1, intercept = strike-mark

        if order=='sell':

            porder = "Sell"

            flat_curve_y = -flat_curve_y

            # Note slope = 1, intercept = -(strike-mark)

            slant_curve_y = -slant_curve_y



    plt.plot(flat_curve_x,flat_curve_y,'r')
    plt.plot(slant_curve_x,slant_curve_y,'r')
    plt.plot(xrange,[0,0],'k--')

    plt.xlim(xrange)

    plt.title("{} {}".format(ptype,porder))
    plt.ylabel("Profit and Loss")
    plt.xlabel("Stock Price")


    plt.show()




