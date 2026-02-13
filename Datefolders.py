import os
from datetime import datetime, date, timedelta

c_date = datetime.today().date()
l_date = date(2026, 12, 31)


def datefolders(c_date, l_date):

        for i in range((l_date-c_date).days+1):
            new_day = c_date + timedelta(days=i)
            os.mkdir(f"C:/Users/vishal.mistry/Desktop/OS Module/{new_day.strftime("%Y-%m-%d")}")

datefolders(c_date,l_date)
