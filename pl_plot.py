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

    #print(args_dict)

    #order_list = args_dict["order"].split(',')

    #print(order_list)

    #uf.parse_option_string(args_dict)

    order = args_dict['order']

    order_class = uf.check_order_class(order)

    print(order_class)


    fig = plt.figure(figsize=(8, 5))
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

        ax = pf.pl_plot_naked(strike,\
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

        ax = pf.pl_plot_vertical(strike, \
                          premium, \
                          type=type, \
                          side=side, \
                          multiplier=multiplier, \
                          axis=ax)

    ax.set_title(order)
    #ax.set_title("{} {} {} of {}".format(multiplier,type,side,stock))
    #ax.title("{} {}".format(type, side))
    ax.set_ylabel("Profit and Loss")
    ax.set_xlabel("Stock Price")

    plt.show()



if __name__ == "__main__":

    main()


