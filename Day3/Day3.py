import copy
import time
import math
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

class Rucksack:
    def __init__(self,contents_string,nr_compartments=2):
        self.contents_string = contents_string
        self.len_contents = len(contents_string)
        self.__content_chars_to_numbers__()

        self.shared_values = dict()
        self.unique_values = dict()
        self.my_dict_list = [dict()]*nr_compartments
        len_compartment = math.floor(self.len_contents / nr_compartments)
        self.compartment = [[0]]*nr_compartments
        self.compartment_string = [[""]]*nr_compartments
        for i in range(nr_compartments):
            self.compartment[i]         = self.contents[i*len_compartment:(i+1)*len_compartment]
            self.compartment_string[i]  = self.contents_string[i*len_compartment:(i+1)*len_compartment]
            self.my_dict_list[i] = self.__count_contents__(self.compartment[i])
        self.my_dict = self.__count_contents__(self.contents)
        for val in self.my_dict_list[0]:
            if val in self.my_dict_list[1]:
                self.shared_values[val] = 1
            else:
                self.unique_values[val] = 1
    def __content_chars_to_numbers__(self):
        self.contents = [0]*self.len_contents
        for i in range(self.len_contents):
            char = self.contents_string[i]
            ascii = ord(char)
            if ascii > 90: # Is it a small letter?
                value = 1 + ascii - 97 # a = 97
            else:
                value = 27 + ascii - 65 # A = 65
            self.contents[i] =value

    def __count_contents__(self,content):
        my_dict = dict()
        for val in content:
            if val in my_dict:
                my_dict[val]+= 1
            else:
                my_dict[val] = 1
        return my_dict
        


test_string = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

test_data = False
second_strategy = True

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string
    rucksack_list = data.split('\n')
    points= []
    points_task2= []
    rucksacks = []
    for rucksack_string in rucksack_list:
        rucksack = Rucksack(rucksack_string)
        for value in rucksack.shared_values.keys():
            points.append(int(value))
        print("B")
        rucksacks.append(rucksack)
        

    nr_groups = math.floor(len(rucksacks)/3.0)
    
    for i in range(nr_groups):
        shared_items = dict()
        group_rucksacks = rucksacks[i*3:(i+1)*3]
        for rs in group_rucksacks:
            for item in rs.my_dict.keys():
                if item in shared_items:
                    shared_items[item]+= 1
                else:
                    shared_items[item] = 1
        for item in shared_items.keys():
            if shared_items[item] > 2:
                print("Shared item is "+ str(item))
                points_task2.append(int(item))
            else:
                pass
            
    sum_task1 = sum(points)

    sum_task2 = sum(points_task2)

print("Total sum Task1 : "+str(sum_task1))


print("Total sum Task2 : "+str(sum_task2))
input("Please press any key")