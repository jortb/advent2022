import copy
from enum import Enum
import os
import copy

def load_input_lines(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    return Lines

def load_input_string(filename):
    file = open(filename, 'r')
    data = file.read()
    return data

class elf:
    def __init__(self,list_of_calories):
        self.list_of_calories = list_of_calories
        self.sum = sum(self.list_of_calories)

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    string_per_elf_list = data.split('\n\n')
    elves= []
    for string_per_elf in string_per_elf_list:
        string_calories_list = string_per_elf.split('\n')
        calories_list = [0] * len(string_calories_list)
        for i in range(len(string_calories_list)):
            try:
                calories_list[i] = int(string_calories_list[i])
            except:
                calories_list[i] = 0
        cur_elf = elf(calories_list)
        elves.append(cur_elf)
    data = data

    sums = []
    highest_sum = -1
    for cur_elf in elves:
        sums.append(cur_elf.sum)
        if cur_elf.sum > highest_sum:
           highest_sum =cur_elf.sum

    sorted_sums = copy.deepcopy(sums)
    sorted_sums.sort()
    highest_sum_check = sorted_sums[-1]
    top3_total = sorted_sums[-1]+sorted_sums[-2]+sorted_sums[-3]

print("Highest sum : "+str(highest_sum))
print("Highest top3 sum : "+str(top3_total))
input("Please press any key")