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

        len_compartment = math.floor(self.len_contents / nr_compartments)
        self.compartment = [[0]]*nr_compartments
        self.compartment_string = [[""]]*nr_compartments
        for i in range(nr_compartments):
            self.compartment[i]         = self.contents[i*len_compartment:(i+1)*len_compartment]
            self.compartment_string[i]  = self.contents_string[i*len_compartment:(i+1)*len_compartment]
            
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


test_string = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

test_data = True
second_strategy = True

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string
    rucksack_list = data.split('\n')
    points= []
    for rucksack_string in rucksack_list:
        rucksack = Rucksack(rucksack_string)
        print("B")
        

    sum = sum(points)


print("Total sum : "+str(sum))
input("Please press any key")