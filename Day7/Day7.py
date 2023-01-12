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

test_data = False
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


def recursive_search_max_size(folder,selected_dirs,select_size = 100000):
    for child_key in folder.children:
        child =folder.children[child_key]
        if isinstance(child,Folder):
            recursive_search_max_size(child,selected_dirs,select_size)
            if child.size<select_size:
                selected_dirs.append(child)

def recursive_search_min_size(folder,selected_dirs,select_size = 100000):
    for child_key in folder.children:
        child =folder.children[child_key]
        if isinstance(child,Folder):
            recursive_search_min_size(child,selected_dirs,select_size)
            if child.size>select_size:
                selected_dirs.append(child)

def recursive_parse_size(folder,indent=0):
    total_file_size = 0
    for child_key in folder.children:
        child =folder.children[child_key]
        if isinstance(child,Folder):
            dir_size = recursive_parse_size(child,indent + 1)
            total_file_size +=dir_size
        else:
            total_file_size += child.size
    
    folder.size = total_file_size
    return total_file_size

a =    94853
b = 14848514
c =  8504156
d = 19307490
test = a + b + c + d

def recursive_print(folder,indent):
    tab= "  "
    for child_key in folder.children:
        child =folder.children[child_key]
        if isinstance(child,Folder):
            print(tab*indent + "-" + child.name + " - " + str(child.size) + " (directory)")
            dir_size = recursive_print(child,indent+1)
        else:
            print(tab*indent + "-" + child.name + " - " + str(child.size))

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
            reg_file = re.compile(r"(\d+) ([\w.]+)")
            
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

    recursive_parse_size(Root,0)
    print("###############")
    recursive_print(Root,0)   

    selected_dirs_task1 = []
    recursive_search_max_size(Root,selected_dirs_task1)
    total_size_task1 = 0

    
    for cur_dir in selected_dirs_task1:
        total_size_task1 +=cur_dir.size

    required_total = 70000000
    required_space = 30000000
    required_cleanup = required_space -  (required_total -Root.size)
    selected_dirs_task2 = []
    recursive_search_min_size(Root,selected_dirs_task2,required_cleanup)
    answer_task1 = total_size_task1

    costs = []
    possible_remove_sizes = []
    for cur_dir in selected_dirs_task2:
        cost=cur_dir.size-required_cleanup
        costs.append(dict(name=cur_dir.name,cost=cost,size=cur_dir.size))
        possible_remove_sizes.append(cur_dir.size)

    possible_remove_sizes.sort()


    answer_task2 = possible_remove_sizes[0]
    
    


print("Total sum Task1 : "+str(answer_task1))


print("Total sum Task2 : "+str(answer_task2))
input("Please press any key")