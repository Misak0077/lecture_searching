import os
import json
from dataclasses import field

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):

    file_path = os.path.join(cwd_path, file_name)

    with open(file_name, 'r') as file:
        data = json.load(file)

    if field not in data:
        return None
    else:
        return data[field]

def linear_search(sekvence, hledaneCislo):
    count = sekvence.count(hledaneCislo)
    positions = []
    for i in range(len(sekvence)):
        if hledaneCislo == sekvence[i]:
            positions.append(sekvence[i])
    return positions, count





def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    print(sequential_data)



if __name__ == '__main__':
    main()