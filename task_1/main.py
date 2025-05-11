import os
import json
import datetime


# If json file were in inside another directory in working directory
# ,then we could use os.path.join(<folder_location>,<file_name>)

file_path = os.path.join('json_program1.json')

with open(file_path, 'r') as file:
    data = json.load(file)
cur = datetime.datetime.today()
print(cur)

# Convert the string to a datetime object and then do the subsctraction
# x = datetime.datetime.strptime(x,'%Y-%m-%d')

for index, value in enumerate(data):
    # print(data[index]['birth_date'])
    x = data[index]['birth_date']
    x = datetime.datetime.strptime(x, '%Y-%m-%d')
    if (cur.year-x.year) < 18:
        print(data[index])


file.close()
