import csv
import os

def read_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, mode="r", encoding="UTF-8") as file:
            return list(csv.reader(file))
    return []



def write_data(file_name: str, data:list) -> None:
    with open(file_name, mode="w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def append_data(file_name, data):
    with open(file_name, mode="a", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)