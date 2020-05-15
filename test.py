import quandl
import yfinance as yf
from pandas_datareader import data as pdr
import datetime
from utilities import check_trading_day, pl_plot

yf.pdr_override()

#quandl.read_key()
#print(quandl.ApiConfig.api_key)

#data = quandl.get("EOD/AAPL", start_date='2020-05-12', end_date='2020-05-12')

#print(data)


stock_string = "MRO"
#stock_string = "JCP"

#stock = yf.Ticker(stock_string)
#print(stock)
#print(stock.history(period="1week"))


data = pdr.get_data_yahoo(stock_string, start="2020-05-01", end="2020-05-14")

print(data)

date = datetime.date.today()

ch = check_trading_day(date)
print(ch)

#pl_plot(.5, .2)
pl_plot(22.50, .85,type='call')
pl_plot(139, 2.3,type='put')


