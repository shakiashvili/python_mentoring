import os
import json
import datetime


def read_json_file(data: str) -> dict:
    file_path = os.path.join(data)
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


def search_age_minors(data: dict) -> list:
    minors = []
    cur = datetime.datetime.today()
    for index, value in enumerate(data):
        x = data[index]['birth_date']
        x = datetime.datetime.strptime(x, '%Y-%m-%d')
        if (cur.year-x.year) < 18:
            minors.append(data[index])
    return minors


if __name__ == "__main__":
    data = read_json_file('json_program1.json')
    minors = search_age_minors(data)
