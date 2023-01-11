import copy
import time
import math
from enum import Enum
import os
import copy

class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

def load_input_lines(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    return Lines

def load_input_string(filename):
    file = open(filename, 'r')
    data = file.read()
    return data

class rps_game:
    def __init__(self,input_player,input_villian):
        self.input_player = input_player
        self.input_villian = input_villian


        if (input_player == input_villian):
            # Draw
            self.win = False
            # 
            self.draw = True
            # Calculate points
            self.points = 1 +self.input_player.value + 3
        elif(input_player.value%3 == (input_villian.value+1)%3):
            # Draw
            self.win = True
            # 
            self.draw = False
            # Calculate points
            self.points = 1 +self.input_player.value + 6
        else:
            # Lose
            self.win = False
            # 
            self.draw = False
            # Calculate points
            self.points = 1 + self.input_player.value 
            

test_string = """A Y
B X
C Z"""

test_data = False
second_strategy = True

if __name__ == "__main__":
    filename = "Input.txt"
    cur_dir = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir,filename)
    data = load_input_string(file_path)
    if test_data: data = test_string
    game_list = data.split('\n')
    points= []
    for str_game in game_list:
        str_moves = str_game.split(' ')
        move_villian = ord(str_moves[0])-65 # ASCII 65 = A
        if second_strategy:
            lose_draw_win = ord(str_moves[1])-88 # ASCII 88 = X
            if lose_draw_win == 0:
                # Force Lose
                move_player = (move_villian-1)%3
            elif lose_draw_win == 1:
                # Force Draw
                move_player = move_villian
            else:
                # Force Win
                move_player = (move_villian+1)%3
        else:
            move_player = ord(str_moves[1])-88 # ASCII 88 = X
        game =rps_game(RPS(move_player),RPS(move_villian))
        points.append(game.points) 

    sum = sum(points)


print("Total sum : "+str(sum))
input("Please press any key")