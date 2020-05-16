import matplotlib.pyplot as plt
import numpy as np


def pl_plot(strike,\
            premium,\
            type='call',\
            side='buy',\
            multiplier=1,\
            axis=None):

    try:
        axis != None
    except:
        print("Need axis object")

    #plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

    prange = 10

    strike = float(strike)
    premium_y = float(premium) * float(multiplier)

    # Define flat part of P&L curve
    flat_curve_y = np.array([-premium_y, -premium_y])

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
        slant_curve_y = np.array([-premium_y, premium_y])

        if xmin<0:
            xrange = [0,xmax]

        if side=='buy':

            pside = "Buy"

            # Note slope = 1, intercept = -(strike+mark)

        if side=='sell':

            pside = "Sell"

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
        slant_curve_y = np.array([premium_y, -premium_y])

        if xmin < 0:
            xrange = [0,xmax]

        if side=='buy':

            pside = "Buy"

            # Note slope = -1, intercept = strike-mark

        if side=='sell':

            pside = "Sell"

            flat_curve_y = -flat_curve_y

            # Note slope = 1, intercept = -(strike-mark)

            slant_curve_y = -slant_curve_y


    #fig = plt.figure(figsize=(8, 5))
    #ax = fig.add_subplot(1, 1, 1)

    axis.plot(flat_curve_x,flat_curve_y,'r')
    axis.plot(slant_curve_x,slant_curve_y,'r')
    axis.plot(xrange,[0,0],'k--')

    #ax.set_xlim(xrange)

    #ax.plt.title("{} {}".format(ptype,porder))
    #ax.plt.ylabel("Profit and Loss")
    #ax.plt.xlabel("Stock Price")


    #plt.show()

    return axis, xrange
