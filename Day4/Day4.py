import copy
import time
import math
from enum import Enum
import os
import copy
import re

def load_input_lines(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    return Lines

def load_input_string(filename):
    file = open(filename, 'r')
    data = file.read()
    return data

class Range:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        self.bitmask = 0
        for i in range(start,stop+1):
            self.bitmask += 2**i
        

class RangeCompare:
    def __init__(self,Range1 , Range2):
        self.r1=Range1
        self.r2=Range2
        min_start = min([Range1.start,Range2.start])
        min_stop = min([Range1.stop,Range2.stop])
        max_start = max([Range1.start,Range2.start])
        max_stop = max([Range1.stop,Range2.stop])

        if Range1.stop == min_stop and Range1.start == max_start:
            self.full_contained = True
        elif Range2.stop == min_stop and Range2.start == max_start:
            self.full_contained = True
        else:
            self.full_contained = False
        # Task 2
        self.overlap =(self.r1.bitmask & self.r2.bitmask)


def Compare_ranges(Range1, Range2):

    return
        
        


test_string = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

test_data = False
second_strategy = True

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string
    lines_list = data.split('\n')
    compares = []
    fully_contained = 0
    overlap_list = []
    overlapping = 0
    for line in lines_list:
        b = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
        result = re.match(b, line)
        if result is not None:
            g0 = result.group(0)
            g1 = result.group(1)
            g2 = result.group(2)
            g3 = result.group(3)
            g4 = result.group(4)
            r1 = Range(int(g1),int(g2))
            r2 = Range(int(g3),int(g4))
            c = RangeCompare(r1,r2)
            if c.full_contained:
                fully_contained += 1
            if c.overlap:
                overlapping += 1
            overlap_list.append(c.overlap)
            compares.append(c)
    points_task1= []
    points_task2= []
    rucksacks = []
    
    sum_task1 = sum(points_task1)
    sum_task2 = sum(points_task2)

print("Total sum Task1 : "+str(fully_contained))


print("Total sum Task2 : "+str(overlapping))
input("Please press any key")