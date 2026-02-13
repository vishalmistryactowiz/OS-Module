import os
from datetime import datetime, date, timedelta

c_date = datetime.today().date()

l_date = date(2026, 12, 31)

remaining_days = (l_date - c_date).days

if not os.path.exists("Date"):
    os.mkdir("Date")

if remaining_days > 0:
    for i in range(remaining_days + 1):
        new_day = c_date + timedelta(days=i)
        os.mkdir(f"Date/{new_day.strftime("%Y-%m-%d")}")


