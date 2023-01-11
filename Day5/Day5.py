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
        
        


test_string = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

test_data = False
second_strategy = True

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string
    #
    data_parts = data.split("\n\n")
    # Process part 1
    lines_list = data_parts[0].split('\n')
    #
    lines_list.reverse()
    
    b = re.compile(r"\s+(\d)")
    #
    results = re.findall(b, lines_list[0])
    numbers =list(map(int, results))
    #
    stacks = []
    for i in range(max(numbers)):
        stacks.append(deque())
    for line in lines_list[1:]:
        b = re.compile(r"[\[\s]([\w\s])[\]\s]\s?")
        results = re.findall(b, line)
        for i in range(len(results)):
            char= results[i]
            if char != ' ':
                stacks[i].append(char)
    # Process part 2
    lines_list = data_parts[1].split('\n')
    actions = []
    for line in lines_list:
        b = re.compile(r"move (\d+) from (\d+) to (\d+)")
        result = re.match(b, line)
        if result is not None:
            g1 = result.group(1)
            g2 = result.group(2)
            g3 = result.group(3)
            #
            move_nr = int(g1)
            from_nr = int(g2)-1     # Zero based index
            to_nr = int(g3)-1       # Zero based index
            my_dict = dict(move_nr=move_nr,from_nr=from_nr,to_nr=to_nr)

            actions.append(my_dict)

    stacks_task2 = copy.deepcopy(stacks)

    for action in actions:
        # Task 2
        temp_stack = deque()
        for i in range(action['move_nr']):
            temp = stacks_task2[action['from_nr']].pop()
            temp_stack.append(temp)

        for i in range(action['move_nr']):
            temp = temp_stack.pop()
            stacks_task2[action['to_nr']].append(temp)
        # Task 1
        for i in range(action['move_nr']):
            temp = stacks[action['from_nr']].pop()
            stacks[action['to_nr']].append(temp)

    answer_task1 = ""
    for stack in stacks:
        answer_task1 +=stack.pop()

    answer_task2 = ""
    for stack in stacks_task2:
        answer_task2 +=stack.pop()
    
    


print("Total sum Task1 : "+str(answer_task1))


print("Total sum Task2 : "+str(answer_task2))
input("Please press any key")