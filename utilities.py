import datetime
import matplotlib.pyplot as plt

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


def pl_plot(strike, mark,type='call',order='buy'):

    fig = plt.figure(figsize=(8, 5))
    #plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

    prange = 10

    strike = float(strike)
    mark = float(mark)

    if type=='call':

        ptype = "Call"

        if order=='buy':

            porder = "Buy"

            flat_curve_y = [-mark,-mark]
            flat_curve_x = [0,strike]

            #slant_curve_x0 = [strike,strike+mark]
            #slant_curve_y0 = [-mark,0]

            # Note slope = 1, intercept = -(strike+mark)

            xval = mark + (strike+mark)

            slant_curve_x = [strike,xval]
            slant_curve_y = [-mark,mark]

            xrange = [(strike+mark)-(xval-strike+mark),xval]

        if order=='sell':

            porder = "Sell"

            flat_curve_y = [mark,mark]
            flat_curve_x = [0,strike]

            # Note slope = -1, intercept = strike+mark

            xval = mark + strike+mark

            slant_curve_x = [strike,xval]
            slant_curve_y = [mark,-mark]

            xrange = [(strike+mark)-(xval-strike+mark),xval]

    if type=='put':

        ptype = "Put"

        if order=='buy':

            porder = "Buy"

            flat_curve_y = [-mark,-mark]
            flat_curve_x = [strike,strike*1000]

            #slant_curve_x0 = [strike-mark,strike]
            #slant_curve_y0 = [0,-mark]

            # Note slope = -1, intercept = strike-mark

            xval = (strike-mark) - mark

            slant_curve_x = [xval,strike]
            slant_curve_y = [mark,-mark]

            xrange = [xval,(strike+mark)-(xval-strike+mark)]

        if order=='sell':

            porder = "Sell"

            flat_curve_y = [mark,mark]
            flat_curve_x = [strike,strike*1000]

            # Note slope = 1, intercept = -(strike-mark)

            xval = (strike - mark) - mark

            slant_curve_x = [0,strike]
            slant_curve_y = [-(strike-mark),mark]

            xrange = [xval,(strike+mark)-(xval-strike+mark)]





    plt.plot(flat_curve_x,flat_curve_y,'r')
    plt.plot(slant_curve_x,slant_curve_y,'r')
    plt.plot(xrange,[0,0],'k--')

    plt.xlim(xrange)

    plt.title("{} {}".format(ptype,porder))
    plt.ylabel("Profit and Loss")
    plt.xlabel("Stock Price")


    plt.show()




