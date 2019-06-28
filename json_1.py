import json

json_list = []

"""
We have data in csv_file.txt in csv format.
We have to change it to dictionary data type in python first
Then we have to move it to json_file and transfer it to json format file.
"""

"""
Manchester United, Manchester, UK
Real Madrid, Madrid, Spain
Juventus, Turin, Italy
Chelsea, London, UK
"""


csv_file = open('csv_file.txt', 'r')
for line in csv_file.readlines():
    club, city, country = line.strip().split(",")
    data = {
        "club": club,
        "city": city,
        "country": country
    }
    json_list.append(data)

csv_file.close()

json_file = open("json_file.txt", 'w')
json.dump(json_list, json_file)
json_file.close()
