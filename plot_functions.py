import matplotlib.pyplot as plt
import numpy as np
import utility_functions as uf
import mcmc_functions as mcmc


def pl_plot_naked(strike,\
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

    strike = float(strike)
    premium_y = float(premium) * float(multiplier)

    # Define flat part of P&L curve
    flat_curve_y = np.array([-premium_y, -premium_y])

    if type=='call':

        ptype = "Call"

        break_even = strike + premium

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

        break_even = strike - premium

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

    zero_range = [0,10**6]
    axis.plot(flat_curve_x,flat_curve_y,'r')
    axis.plot(slant_curve_x,slant_curve_y,'r')
    axis.plot(zero_range,[0,0],'k--')

    axis.set_xlim(xrange)

    #plt.show()

    return axis,xrange, break_even



def pl_plot_vertical(strike,\
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

    type = type[0]

    strike = {side[0]:float(strike[0]), side[1]:float(strike[1])}
    premium = {side[0]:float(premium[0]),side[1]:premium[1]}

    # Common
    width = abs(strike['buy'] - strike['sell'])
    net = abs(premium['sell'] - premium['buy'])


    if type == 'call':

        # Bear Call Spread (Credit Spread)
        if strike['buy'] > strike['sell']:

            print('Bear Call')
            print('Credit Spread')

            #reward = premium['sell'] - premium['buy']
            reward = net

            risk = -(width - net)

            break_even = strike['sell'] + premium['sell']

            print('Risk Reward')
            print(risk)
            print(reward)

            xrange = [strike['sell']-width,strike['buy']+width]

            x1 = np.array([0,strike['sell']])
            y1 = np.array([reward,reward])

            x2 = np.array([strike['sell'],strike['buy']])
            y2 = [reward,risk]

            x3 = np.array([strike['buy'],strike['buy']*1000])
            y3 = np.array([risk,risk])



        #Bull Call Spread (Debit Spread)
        if strike['buy'] < strike['sell']:

            print('Bull Call')
            print('Debit Spread')

            #risk = premium['buy'] - premium['sell']
            risk = -net

            reward = width - net

            break_even = strike['buy'] - premium['buy']

            print('Risk Reward')
            print(risk)
            print(reward)

            xrange = [strike['buy']-width,strike['sell']+width]

            x1 = np.array([0, strike['buy']])
            y1 = np.array([risk, risk])

            x2 = np.array([strike['buy'], strike['sell']])
            y2 = [risk, reward]

            x3 = np.array([strike['sell'], strike['sell'] * 1000])
            y3 = np.array([reward, reward])

    if type == 'put':

        # Bear Put Spread (Debit Spread)
        if strike['buy'] > strike['sell']:

            print('Bear Put')
            print('Debit Spread')

            #risk = premium['buy'] - premium['sell']
            risk = -net

            reward = width - net

            break_even = strike['buy'] - premium['buy']

            print('Risk Reward')
            print(risk)
            print(reward)

            xrange = [strike['sell']-width,strike['buy']+width]

            x1 = np.array([0,strike['sell']])
            y1 = np.array([reward,reward])

            x2 = np.array([strike['sell'],strike['buy']])
            y2 = [reward,risk]

            x3 = np.array([strike['buy'],strike['buy']*1000])
            y3 = np.array([risk,risk])

        # Bull Put Spread (Credit Spread)
        if strike['buy'] < strike['sell']:

            print('Bull Put')
            print('Credit Spread')

            #reward = premium['sell'] - premium['buy']
            reward = net
            risk = -(reward - net)

            break_even = strike['sell'] + premium['sell']

            print('Risk Reward')
            print(risk)
            print(reward)

            xrange = [strike['buy']-width,strike['sell']+width]

            x1 = np.array([0,strike['buy']])
            y1 = np.array([risk,risk])

            x2 = np.array([strike['buy'],strike['sell']])
            y2 = [risk,reward]

            x3 = np.array([strike['sell'],strike['sell']*1000])
            y3 = np.array([reward,reward])


    # Define flat part of P&L curve
    #flat_curve_y = np.array([-premium_y, -premium_y])

    if xrange[0] < 0:
        xrange = [0, xrange[1]]

    zero_range = [0,10**6]

    axis.plot(x1, y1,'r')
    axis.plot(x2, y2,'r')
    axis.plot(x3, y3,'r')
    #axis.plot(slant_curve_x,slant_curve_y,'r')
    axis.plot(zero_range,[0,0],'k--')

    axis.set_xlim(xrange)




    #plt.show()

    return axis, xrange, break_even


def plot_price_mcmc_histogram(prices,axis=None):

    try:
        axis != None
    except:
        print("Need axis object")

    axis = axis.twinx()

    axis.hist(prices,bins=30,density=True,alpha=0.3)

    return axis



