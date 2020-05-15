import matplotlib.pyplot as plt
import numpy as np


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
        #if strike - premium > 0:
        xmin = strike - premium
        #else:
        #    xmin = 0

        xrange = [xmin,xmax]

        slant_curve_x = np.array([strike, xmax])
        slant_curve_y = np.array([-premium, premium])

        if xmin<0:
            xrange = [0,xmax]

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
        #if (strike - premium) - premium > 0:
        xmin = (strike - premium) - premium
        #else:
        #    xmin = 0


        xrange = np.array([xmin,xmax])

        slant_curve_x = np.array([xmin, strike])
        slant_curve_y = np.array([premium, -premium])

        if xmin < 0:
            xrange = [0,xmax]

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
