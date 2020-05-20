import functions.plotting.plot_functions as pf
import matplotlib.pyplot as plt
import functions.simulation.mcmc_functions as mcmc
import functions.utility.utility_functions as uf
import functions.utility.date_time_functions as dt
import argparse
import datetime





def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--order', required=True)
    parser.add_argument('--mcmc', default=False)
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


    fig = plt.figure(figsize=(8, 5))
    fig.suptitle(order)
    ax = fig.add_subplot(1, 1, 1)

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

        ax,orange,break_even = pf.pl_plot_naked(strike,\
                                premium,\
                                type=type,\
                                side=side,\
                                multiplier=multiplier,\
                                axis=ax)

    if order_class=="vertical":

        print(order)

        side, multiplier, stock, expiration, strike, type, premium = \
            uf.parse_verical_option_string(order)

        print(side)

        ax,orange,break_even = pf.pl_plot_vertical(strike, \
                          premium, \
                          type=type, \
                          side=side, \
                          multiplier=multiplier, \
                          axis=ax)

    ax.set_ylabel("Profit and Loss per Share")

    # MCMC Simulation
    if args_dict['mcmc'] == 'True':

        df = uf.get_stock_historical_data(stock)

        print(df)

        stdev = uf.get_stock_stdev(df)

        print(stdev)

        print('Expiration')
        if len(expiration) > 1:
            expiration = expiration[0]
        print(expiration)

        start = datetime.date.today().isoformat()
        end = dt.input_to_iso(expiration)
        n_days = dt.get_number_trading_days(start, end)
        #import pdb;pdb.set_trace()
        print('Number of Trading Days:')
        print(n_days)

        #price_path = mcmc.stock_random_walk(df,stdev,n_days)
        #print(price_path)
        prices = mcmc.many_random_walks(df,stdev,n_days)
        print(prices[-10:-1])

        prange = [min(prices),max(prices)]

        prange = [min([min(prange),min(orange)]),\
                  max([max(prange),max(orange)])]

        ax=pf.plot_price_mcmc_histogram(prices,axis=ax)

        prices_gt_breakeven = list(filter(lambda x: x > break_even, prices))

        nsim = len(prices)
        ngt = len(prices_gt_breakeven)
        nlt = nsim - ngt

        prob_gt = round((float(ngt) / float(nsim)) * 100, 2)
        prob_lt = round((float(nlt) / float(nsim)) * 100, 2)

        ax.set_title("{}% below Break Even, {}% above Break Even".\
            format(prob_lt, prob_gt))



    ax.set_xlim(prange)
    #ax.set_title(order)
    #ax.set_title("{} {} {} of {}".format(multiplier,type,side,stock))
    #ax.title("{} {}".format(type, side))
    ax.set_xlabel("Stock Price")

    plt.show()



if __name__ == "__main__":

    main()


