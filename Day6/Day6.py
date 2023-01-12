import copy
import time
import math
from enum import Enum
import os
import copy
import re
from collections import deque

def load_input_lines(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    return Lines

def load_input_string(filename):
    file = open(filename, 'r')
    data = file.read()
    return data
    

test_string = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

test_data = False
second_strategy = True

def find_nr_distinct_chars(line,nr_distinct=4):
    marker_found = False
    mem = deque()
    counter = 0
    while(not marker_found):
        mem.append(line[counter])
        if len(mem)>nr_distinct: mem.popleft()
        counter += 1
        #
        if len(mem)==nr_distinct:
            my_dict = dict()
            for char in mem:
                my_dict[char] = True
            if len(my_dict.keys()) ==nr_distinct:
                marker_found = counter
                print("Found marker after character : "+str(marker_found))

    return marker_found

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string

    lines_list = data.split('\n')

    for line in lines_list:
        marker_found = find_nr_distinct_chars(line)
            
    print("############")
    for line in lines_list:
        marker_found_task2 = find_nr_distinct_chars(line,14)

        
    answer_task1 = marker_found

    answer_task2 = marker_found_task2
    
    


print("Total sum Task1 : "+str(answer_task1))


print("Total sum Task2 : "+str(answer_task2))
input("Please press any key")