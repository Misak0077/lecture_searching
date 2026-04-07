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
            positions.append(i-1)
    return positions, count

def binary_search(seznam, hledaneCislo):
    right = len(seznam) - 1
    left = 0
    while left <= right:
        mid = (left + right) //2
        if hledaneCislo == seznam[mid]:
            return mid
        elif seznam[mid] < hledaneCislo:
            left = mid
        else:
            right = mid
    return None





def main():
    sequential_data = read_data("sequential.json","ordered_numbers")
    unsequential_data = read_data("sequential.json","unordered_numbers")
    print(sequential_data)
    linear = linear_search(unsequential_data,1)
    print(linear)
    binar = binary_search(sequential_data,8)
    print(binar)




if __name__ == '__main__':
    main()