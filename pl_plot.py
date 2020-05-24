import functions.plot_functions as pf
import matplotlib.pyplot as plt
import functions.mcmc_functions as mcmc
import functions.utility_functions as uf
import functions.date_time_functions as dtf
import functions.options_functions as of
import numpy as np
import argparse
import datetime


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--order', required=True)
    parser.add_argument('--mcmc', default=False)
    parser.add_argument('--volatility_period', default=10)
    parser.add_argument('--end_date', default=False)
    args = parser.parse_args()
    args_dict = vars(args)
    #ostring = "BTO 1 INTC June 22.5 call at 1.20"

    #print(args_dict)

    #order_list = args_dict["order"].split(',')

    #print(order_list)

    #uf.parse_option_string(args_dict)

    order = args_dict['order']

    order_class = uf.check_order_class(order)

    print(order_class)


    if order_class == "naked":
        side, multiplier, stock, expiration, strike, type, premium = \
            uf.parse_naked_option_string(order)

        print(side)
        print(multiplier)
        print(stock)
        print(expiration)
        print(strike)
        print(type)
        print(premium)

        return_function,break_even = of.naked_option(strike,\
                                premium,\
                                type=type,\
                                side=side,\
                                multiplier=multiplier)

        option_range = [break_even - 2*float(premium),\
                        break_even + 2*float(premium)]

        return_range = [-premium - 1, premium+1]


    if order_class=="vertical":

        print(order)

        side, multiplier, stock, expiration, strike, type, premium = \
            uf.parse_verical_option_string(order)

        print(side)

        return_function,break_even = of.vertical_spread(strike, \
                          premium, \
                          type=type, \
                          side=side, \
                          multiplier=multiplier)

        width = abs(strike[0] - strike[1])
        option_range = [break_even - 2*width,\
                        break_even + 2*width]

        max_premium = max(premium[0],premium[1])
        return_range = (-max_premium - 1, max_premium + 1)


    if min(option_range) < 0:
        option_range[0] = 0

    xvals = np.linspace(0,break_even*10,break_even*100)

    yvals = []
    for val in xvals:
        yvals.append(return_function(val))


    fig = plt.figure(figsize=(8, 5))
    fig.suptitle(order)
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(xvals,yvals, 'r')
    ax.set_xlim(option_range)
    ax.set_ylim(return_range)
    ax.set_ylabel("Profit and Loss per Share")

    # MCMC Simulation
    if args_dict['mcmc'] == 'True':

        df = uf.get_stock_historical_data(stock)

        print(df)

        stdev = uf.get_stock_stdev(df,\
                                   period=int(args_dict['volatility_period']))

        print(stdev)


        print('Expiration')
        if isinstance(expiration, str) == False:
            expiration = expiration[0]
        print(expiration)

        if args_dict['end_date'] != False:
            expiration = args_dict['end_date']

        start = datetime.date.today().isoformat()
        end = dtf.input_to_iso(expiration)
        n_days = dtf.get_number_trading_days(start, end)
        #import pdb;pdb.set_trace()
        print('Number of Trading Days:')
        print(n_days)

        #price_path = mcmc.stock_random_walk(df,stdev,n_days)
        #print(price_path)
        prices = mcmc.many_random_walks(df,stdev,n_days)
        print(prices[-10:-1])

        mcmc_range = [min(prices),max(prices)]

        if min(mcmc_range) < 0:
            mcmc_range = [0,max(prices)]

        mcmc_range = [min([min(mcmc_range),min(option_range)]),\
                  max([max(mcmc_range),max(option_range)])]

        ax=pf.plot_price_mcmc_histogram(prices,axis=ax)

        prices_gt_breakeven = list(filter(lambda x: x > break_even, prices))

        nsim = len(prices)
        ngt = len(prices_gt_breakeven)
        nlt = nsim - ngt

        prob_gt = round((float(ngt) / float(nsim)) * 100, 2)
        prob_lt = round((float(nlt) / float(nsim)) * 100, 2)

        ax.set_title("{}% below Break Even, {}% above Break Even".\
            format(prob_lt, prob_gt))

        ax.set_xlim(mcmc_range)


    #ax.set_title(order)
    #ax.set_title("{} {} {} of {}".format(multiplier,type,side,stock))
    #ax.title("{} {}".format(type, side))
    ax.set_xlabel("Stock Price")

    plt.show()



if __name__ == "__main__":

    main()


