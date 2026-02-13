import os
from datetime import datetime, date, timedelta

c_date = datetime.today().date()

l_date = date(2026, 12, 31)

remaining_days = (l_date - c_date).days

main_folder = "Date"
if not os.path.exists(main_folder):
    os.mkdir(main_folder)


if remaining_days > 0:
    for i in range(remaining_days + 1):
        new_day = c_date + timedelta(days=i)
        folder_name = new_day.strftime("%Y-%m-%d")

        # Create full path inside Date folder
        folder_path = os.path.join(main_folder, folder_name)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    print("Folders created successfully inside 'Date' directory!")
else:
    print("The date has already passed.")
