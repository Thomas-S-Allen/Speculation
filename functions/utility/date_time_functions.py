import datetime
import pytz

def check_trading_day(date):

    markets_closed = ['2020-01-01',\
                      '2020-01-20',\
                      '2020-02-17',\
                      '2020-04-10',\
                      '2020-05-25',\
                      '2020-07-03',\
                      '2020-09-07',\
                      '2020-11-26',\
                      '2020-12-25',\
                      #
                      '2021-01-01',\
                      '2021-01-18',\
                      '2021-02-15',\
                      '2021-04-02',\
                      '2021-05-31',\
                      '2021-07-05',\
                      '2021-09-06',\
                      '2021-11-25',\
                      '2021-12-24',\
                      #
                      '2022-01-17',\
                      '2022-02-21',\
                      '2022-04-15',\
                      '2022-05-30',\
                      '2022-07-04',\
                      '2022-09-05',\
                      '2022-11-24',\
                      '2022-12-26']



    if date in markets_closed:
        return False
    else:
        return True

def check_weekday(date):

    if date.weekday()==5 or date.weekday()==6:
        return False
    else:
        return True

def create_date_list(start,end):

    print(start)

    print(end)

    start = datetime.date.fromisoformat(start)
    end = datetime.date.fromisoformat(end)

    print(end-start)

    date = start
    date_list = []

    while date != end:
        date = date + datetime.timedelta(1)
        #print(date)

        if check_trading_day(date) and check_weekday(date) == True:
            date_list.append(date.isoformat())

    return date_list

def get_number_trading_days(start,end):

    date_list = create_date_list(start,end)

    return len(date_list)

def numerical_month(month):

    if month == "January":
        return 1
    elif month == "February":
        return 2
    elif month == "March":
        return 3
    elif month == "April":
        return 4
    elif month == "May":
        return 5
    elif month == "June":
        return 6
    elif month == "July":
        return 7
    elif month == "August":
        return 8
    elif month == "September":
        return 9
    elif month == "October":
        return 10
    elif month == "November":
        return 11
    elif month == "December":
        return 12

def check_market_today():
    pass

def input_to_iso(date):

    print(date)
    print(date.split())

    if len(date.split()) == 2:
        print(date)
        date = date.split()

        year = datetime.date.today().year
        month = numerical_month(date[0])
        day = int(date[1])

        return datetime.date(year, month, day).isoformat()

    if len(date.split()) == 3:
        print(date)
        date = date.split()

        year = int(date[2])
        month = numerical_month(date[0])
        day = int(date[1])

        return datetime.date(year, month, day).isoformat()



