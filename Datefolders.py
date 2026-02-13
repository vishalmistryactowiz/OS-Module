import os
from datetime import datetime, date, timedelta

def datefolders():
    c_date = datetime.today().date()
    l_date = date(2026, 12, 31)

    if not os.path.exists("Date"):
        os.mkdir("Date")

        for i in range((l_date-c_date).days+1):
            new_day = c_date + timedelta(days=i)
            os.mkdir(f"Date/{new_day.strftime("%Y-%m-%d")}")

datefolders()
