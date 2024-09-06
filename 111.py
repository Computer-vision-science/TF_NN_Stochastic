#a = datetime(1986, 11, 20, 22, 46,45, 8443)
#a = date(1986, 11, 20)
#b = time(20, 6, 55)
#c = datetime.combine(a, b)
#b = a.time()
#print(datetime.now())
#print(datetime.utcnow())
#print(datetime.today())
#print(a.timestamp())
#print(datetime.fromtimestamp(2543665634.23782))
'''
dt = input('Enter date/time how DD.MM.YYYY HH:MM:SS: ')
d, t = dt.split(' ')
d = [int(i) for i in d.split('.')]
t = [int(i) for i in t.split(':')]

dt_end = datetime(d[2], d[1], d[0], t[0], t[1], t[2])
print(dt_end)

dt = input('Enter date/time how HH:MM: ')
dt_end = datetime.strptime(dt, '%H:%M')
print(dt_end)
b = a.replace(year = 2050)
print(a)
print(a.isoformat())


def is_available_date(booked_dates, date_for_booking):
    from datetime import datetime
    for i in range(len(booked_dates)):
        if len(booked_dates[i]) > 12:
            booked_dates[i] = booked_dates[i].split('-')
            booked_dates[i][0] = datetime.strptime(booked_dates[i][0], '%d.%m.%Y')
            booked_dates[i][1] = datetime.strptime(booked_dates[i][1], '%d.%m.%Y')
            booked_dates[i] = [booked_dates[i][0], booked_dates[i][1]]
        else:
            booked_dates[i] = [datetime.strptime(booked_dates[i], '%d.%m.%Y'),
                               datetime.strptime(booked_dates[i], '%d.%m.%Y')]
    if len(date_for_booking) > 12:
        date_for_booking = date_for_booking.split('-')
        date_for_booking[0] = datetime.strptime(date_for_booking[0], '%d.%m.%Y')
        date_for_booking[1] = datetime.strptime(date_for_booking[1], '%d.%m.%Y')
        date_for_booking = [date_for_booking[0], date_for_booking[1]]
    else:
        date_for_booking = [datetime.strptime(date_for_booking, '%d.%m.%Y'),
                            datetime.strptime(date_for_booking, '%d.%m.%Y')]

    for a in date_for_booking:
        for b in booked_dates:
            if b[0] <= a <= b[1]:
                return 'False'
    return 'True'

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

from datetime import timedelta, date

td1 = timedelta(hours=-7, minutes=-30)
td2 = timedelta(days=3)
td3 = timedelta(weeks=-5, hours=-11)
td4 = timedelta(days=2, hours=2)
a = date(2022, 10, 27) - td1
print(td3)
print(abs(td3))

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = birthday - today

print(days)

from datetime import datetime, time, timedelta

dt = datetime.strptime('02.11.2021 07:15', '%d.%m.%Y %H:%M')
dt0 = [timedelta(hours=21, minutes=0), timedelta(hours=18, minutes=0)][dt.weekday() > 5]
print([dt0 - timedelta(hours=dt.hour, minutes=dt.minute), 'Магазин не работает']
      [timedelta(hours=dt.hour, minutes=dt.minute) > dt0])



print(datetime.today().time() - time(18, 0, 0))

import time

S = 0
a = time.monotonic()
for i in range(110000000):
    S += i

print(time.monotonic() - a)
#10.746323259998462
#10.892685357001028
#11.417758976998812
#12.314302802000384

import calendar, locale
#locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(calendar.month_name[2])
calendar.prcal(1986)
'''

from datetime import datetime, date

from dateutil.relativedelta import relativedelta, FR, TU
from dateutil.easter import easter
from dateutil.parser import parse
import tensorflow





