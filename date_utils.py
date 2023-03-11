
from datetime import datetime, date
import pprint
from dateutil.rrule import *
from dateutil.rrule import weekdays
pp = pprint.PrettyPrinter(indent=4)

start_date = date(2022,1,1)
en = date(2023,1,1)
l = list(rrule(MONTHLY,byweekday=(TH(4)), dtstart=start_date, until=en))
print(type(l[0]),"Single")
pp.pprint(l)
print(weekdays[3])
