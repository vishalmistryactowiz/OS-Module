import os
from datetime import datetime, date, timedelta

user_date = input("Enter a Date YYYY-MM-DD:- ")

def create_files(folder_path, file_date):
    file_base = f"{folder_path}/{file_date.strftime('%Y-%m-%d')}"

    extensions = [".txt", ".py", ".js", ".html"]

    for ext in extensions:
        with open(file_base + ext, "w") as f:
            f.write(str(file_date))


def datefolders(user_date):
    try:
        c_date = datetime.strptime(user_date, "%Y-%m-%d").date()
        year = c_date.year
        l_date = date(year, 12, 31)

        for i in range((l_date - c_date).days + 1):
            new_day = c_date + timedelta(days=i)

            folder_path = f"C:/Users/vishal.mistry/Desktop/OS Module/{new_day.strftime('%Y-%m-%d')}"
            os.mkdir(folder_path)

            if new_day.month == 12:
                last_date = date(new_day.year, 12, 31)
            else:
                next_month = date(new_day.year, new_day.month + 1, 1)
                last_date = next_month - timedelta(days=1)

            file_date = last_date - timedelta(days=i)
            create_files(folder_path, file_date)

        print("Folders and multiple files created")

    except FileExistsError:
        print("Folders already created")

datefolders(user_date)
