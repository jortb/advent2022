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
        
        


test_string = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

test_data = True
second_strategy = True

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string
    rucksack_list = data.split('\n')
    points_task1= []
    points_task2= []
    rucksacks = []
    
    sum_task1 = sum(points_task1)
    sum_task2 = sum(points_task2)

print("Total sum Task1 : "+str(sum_task1))


print("Total sum Task2 : "+str(sum_task2))
input("Please press any key")