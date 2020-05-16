import plot_functions as pf
import matplotlib.pyplot as plt
import utility_functions as uf
import argparse





def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--order', required=True)
    args = parser.parse_args()
    args_dict = vars(args)
    #ostring = "BTO 1 INTC June 22.5 call at 1.20"

    print(args_dict)

    order_list = args_dict["order"].split(',')

    print(order_list)

    #uf.parse_option_string(args_dict)


    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(1, 1, 1)

    for order in order_list:

        side, multiplier, stock, expiration, strike, type, premium = \
            uf.parse_option_string(order)

        print(side)
        print(multiplier)
        print(stock)
        print(expiration)
        print(strike)
        print(type)
        print(premium)

        ax, xrange = pf.pl_plot(strike,\
                                premium,\
                                type=type,\
                                side=side,\
                                multiplier=multiplier,\
                                axis=ax)

    ax.set_xlim(xrange)

    ax.set_title(order)
    #ax.set_title("{} {} {} of {}".format(multiplier,type,side,stock))
    #ax.title("{} {}".format(type, side))
    ax.set_ylabel("Profit and Loss")
    ax.set_xlabel("Stock Price")

    plt.show()



if __name__ == "__main__":

    main()


