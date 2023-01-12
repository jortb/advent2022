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
    

test_string = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

test_data = True
second_strategy = True

class Folder:
    def __init__(self,parent=None,name="Root"):
        self.parent = parent
        self.name = name
        self.children = dict()
        self.size = 0

class File:
    def __init__(self,parent=None,size=0,name=""):
        self.parent = parent
        self.size = size
        self.name = name


def recursive_search(folder,indent=0):
    tab= "  "
    total_file_size = 0
    for child_key in folder.children:
        child =folder.children[child_key]
        if isinstance(child,Folder):
            print(tab*indent + "-" + child.name + " - " + str(child.size))
            dir_size = recursive_search(child,indent + 1)
            total_file_size +=dir_size
        else:
            print(tab*indent + "-" + child.name + " - " + str(child.size))
            total_file_size += child.size
    
    folder.size = total_file_size
    return total_file_size

Root = Folder()
if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string

    lines_list = data.split('\n')

    cur_path = Root
    for line in lines_list:
        # User input?
        if line[0]=='$':
            b = re.compile(r"\$ (\w+) ([\w./]*)")
            result = re.match(b,line)
            if result is not None:
                g1 = result.group(1)
                g2 = result.group(2)
                if g1 == "cd":
                    if g2 == "..":
                        cur_path = cur_path.parent
                    elif g2 == '/':
                        cur_path = Root
                    else:
                        if not (g2 in cur_path.children):
                            cur_path.children[g2] = Folder(cur_path,g2)
                        cur_path = cur_path.children[g2]
                elif g1 == "ls":
                    pass
                else:
                    pass
        else:
            reg_file = re.compile(r"(\d+) (\w+)")
            
            result = re.match(reg_file,line)
            if result is not None:
                g1 = result.group(1)
                g2 = result.group(2)
                if not (g2 in cur_path.children):
                    cur_path.children[g2] = File(cur_path,int(g1),g2)
                continue
            
            reg_folder = re.compile(r"dir (\w+)")
            result = re.match(reg_folder,line)
            if result is not None:
                g1 = result.group(1)
                if not (g1 in cur_path.children):
                    cur_path.children[g1] = Folder(cur_path,g1)
                continue

    recursive_search(Root)
    print("###############")
    recursive_search(Root)   
    answer_task1 = ""

    answer_task2 = "marker_found_task2"
    
    


print("Total sum Task1 : "+str(answer_task1))


print("Total sum Task2 : "+str(answer_task2))
input("Please press any key")