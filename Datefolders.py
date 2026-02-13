import os
from datetime import datetime, date, timedelta

user_date =input("Enter a Date YYYYMMDD:-")

def datefolders(user_date):
    try:
        c_date = datetime.strptime(user_date, "%Y-%m-%d").date()
        year = c_date.year
        l_date = date(year, 12, 31)

        for i in range((l_date-c_date).days+1):
            new_day = c_date + timedelta(days=i)
            os.mkdir(f"C:/Users/vishal.mistry/Desktop/OS Module/{new_day.strftime("%Y-%m-%d")}")
        print("Folders is Created")

    except FileExistsError:
        print("Folders is already Created")


datefolders(user_date)
