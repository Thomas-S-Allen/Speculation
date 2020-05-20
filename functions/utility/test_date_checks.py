import date_time_functions as dt


date1 = '2020-05-20'
date2 = '2020-10-18'

trading_day = dt.check_trading_day(date1)

print(trading_day)

date_list = dt.create_date_list(date1,date2)

#print(date_list)

n_days = dt.get_number_trading_days(date1,date2)
print(n_days)

date = 'May 29'

newdate = dt.input_to_iso(date)

print(newdate)

date = 'May 29 2022'

newdate = dt.input_to_iso(date)

print(newdate)
