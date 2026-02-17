import os
from datetime import datetime ,date


source = 'C:/Users/vishal.mistry/Desktop/OS Module/Date_26/'
destination ='C:/Users/vishal.mistry/Desktop/OS Module/Date_27/'

def move_files(source, destination):
    print(source)
    for dir in os.listdir(source):
        dir_path = os.path.join(source, dir)
        for file in os.listdir(dir_path):
            source_file_path = dir_path + '/' + file
            source_date_str = source_file_path.split('/')[-2]
            source_date = datetime.strptime(source_date_str, '%Y-%m-%d')
            destination_date = source_date.replace(year=source_date.year+1).date()
            destination_date_str = destination_date.strftime('%Y-%m-%d')
            destination_dir_path = destination + '/' + destination_date_str
            os.makedirs(destination_dir_path, exist_ok=True)
            destination_file_path = destination_dir_path + '/' + file
            print(source_file_path)
            os.rename(source_file_path, destination_file_path)

def remove_file(destination):
     for i in os.listdir(destination):
        folder_path = os.path.join(destination, i)

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if file.endswith('.py') or file.endswith('.js'):
                os.remove(file_path)
            
# move_files(source=source, destination=destination)
remove_file(destination=destination)