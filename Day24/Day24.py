import copy
import time
import math
from enum import Enum
import os
 
class StormMovement(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class blizzard:
    def __init__(self,direction=StormMovement.LEFT,start_x=1, start_y=1):
        self.direction = direction
        self.x = start_x
        self.y = start_y
        self.storms = []
    
    def update(self):
        if self.direction == StormMovement.UP:
            self.x = self.x
            self.y = self.y - 1
        elif self.direction == StormMovement.DOWN:
            self.x = self.x
            self.y = self.y + 1
        elif self.direction == StormMovement.LEFT:
            self.x = self.x - 1
            self.y = self.y
        elif self.direction == StormMovement.RIGHT:
            self.x = self.x + 1
            self.y = self.y

    def wrap(self,rows,cols):
        if self.x > (cols-1):
            self.x = 0
        elif self.x < 0:
            self.x = cols-1

        if self.y > (rows-1):
            self.y = 0
        elif self.y < 0:
            self.y = rows-1
        

class storm_map:
    
    def __init__(self,cols,rows,Debug=True):
        self.Debug = Debug
        self.Done = False
        self.rows = rows
        self.cols = cols
        self.initialize_map_empty()
        self.initialize_dijkstra_map()
        self.storms = []
        self.maps = []

    def load_map_and_stroms(self,filename='TestMap.dat'):
        file1 = open(filename, 'r')
        Lines = file1.readlines()
        #
        storms = []
        #
        line_count = 0
        
        for line in Lines:
            
            #
            char_count = 0
            
            #
            for char in line:
                
                
                if char == '#':
                    val = -1
                elif char == '^':
                    val = 0
                    storms.append(blizzard(StormMovement.UP,char_count,line_count))
                elif char == 'v':
                    val = 0
                    storms.append(blizzard(StormMovement.DOWN,char_count,line_count))
                elif char == '<':
                    val = 0
                    storms.append(blizzard(StormMovement.LEFT,char_count,line_count))
                elif char == '>':
                    val = 0
                    storms.append(blizzard(StormMovement.RIGHT,char_count,line_count))
                else:
                    val = 0

                self.base_map[line_count][char_count] = val
                #
                char_count += 1
                if char_count >= self.cols:
                    break
            #
            line_count += 1
            #
            if line_count >= self.rows:
                break
        #
        self.map = copy.deepcopy(self.base_map)
        #
        for storm in storms:
            self.add_storm(storm)

    def load_base_map(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if (y==0) or (y==(self.rows-1)) or (x==0) or (x==(self.cols-1)):
                    self.base_map[y][x] = -1
                else:
                    self.base_map[y][x] = 0 # j + i * cols

    def initialize_map_empty(self):
        self.map = [[0 for x in range(self.cols)] for y in range(self.rows)]
        self.base_map = copy.deepcopy(self.map)

        self.first_row = self.map[0]
        a=1

    def initialize_dijkstra_map(self):
        self.reset_dijkstra_and_set_goal(1,0,self.cols-2,self.rows-1)

    def reset_dijkstra_and_set_goal(self,start_x,start_y,goal_x,goal_y):
        self.Done = False
        dv = 65535
        self.base_dijkstra = [[dv for x in range(self.cols)] for y in range(self.rows)]
        self.dijkstra = copy.deepcopy(self.base_dijkstra)
        self.searcher_positions = [[start_x,start_y]] # Start with one searcher
        self.goal_position = [goal_x,goal_y]
        self.searcher_step = 0

    def get_map_value_xy(self,x,y):
        if x<self.cols and y<self.rows:
            return self.map[y][x]
        else:
            return -1

    def set_map_value_xy(self,x,y,val):
        self.map[y][x] = val

    def get_dijkstr_value_xy(self,x,y):
        if x<self.cols and y<self.rows:
            d =self.dijkstra
            return d[y][x]
        else:
            return -1

    def set_dijkstr_value_xy(self,x,y,value):
        d = self.dijkstra
        d[y][x] = value

    def get_map_value_pos(self,pos):
        val =  self.get_map_value_xy(pos[0],pos[1])
        #test = self.map[pos[1]][pos[0]]
        return val

    def __go_dijkstra__(self,searcher_list,index):
        #
        searcher = searcher_list[index]
        # Have we been here already?
        dijkstra_val = self.get_dijkstr_value_xy(searcher[0]  ,searcher[1])
        # Update current dijkstra  
        map_val = self.get_map_value_pos(searcher)
        if dijkstra_val <= self.searcher_step:
            self.searcher_positions[index] = [-1,-1]
            return False
        elif map_val == 0:
            self.set_dijkstr_value_xy(searcher[0]  ,searcher[1],self.searcher_step)
        else:
            searcher_list[index] = [-1,-1]
            return False

        return True

    def update_dijkstra(self):       
        # 
        if self.Debug:
            print("Update Dijkstra with "+str(len(self.searcher_positions))+" searcher positions")
        # Extend dijkstra
        self.dijkstra=copy.deepcopy(self.base_dijkstra)
        #
        if True:
            self.update_searchers_index_based()
        else:
            self.update_searchers()
        #
        self.searcher_step += 1
        #
        if self.Debug:
            print("After Dijkstra : "+str(len(self.searcher_positions))+" searcher positions")
        return 

    def update_searchers_index_based(self):
        new_searcher_positions_indices=[]
        for i in range(len(self.searcher_positions)):#searcher in self.searcher_positions:
            searcher = self.searcher_positions[i]
            #
            new_searcher_positions_indices.append(searcher[0]+searcher[1]*self.cols)
            # get up map value
            map_up      = self.get_map_value_xy(searcher[0]  ,searcher[1]-1)
            if map_up == 0:
                new_searcher_positions_indices.append(searcher[0]+(searcher[1]-1)*self.cols)
            # get up map value
            map_down    = self.get_map_value_xy(searcher[0]  ,searcher[1]+1)
            if map_down == 0:
                new_searcher_positions_indices.append(searcher[0]+(searcher[1]+1)*self.cols)
            # get up map value
            map_left    = self.get_map_value_xy(searcher[0]-1,searcher[1]  )
            if map_left == 0:
                new_searcher_positions_indices.append(searcher[0]-1+searcher[1]*self.cols)
            # get up map value
            map_right   = self.get_map_value_xy(searcher[0]+1,searcher[1]  )
            if map_right == 0:
                new_searcher_positions_indices.append(searcher[0]+1+searcher[1]*self.cols)

        new_searcher_positions = []
        new_searcher_positions_indices_filtered = list(set(new_searcher_positions_indices))
        for new_searcher_positions_index in new_searcher_positions_indices_filtered:
            x = new_searcher_positions_index%self.cols
            y = math.floor(new_searcher_positions_index/self.cols)
            new_searcher_positions.append([x,y])

        self.searcher_positions = new_searcher_positions

        kept_search_positions =[]
        for i in range(len(self.searcher_positions)):
            #
            searcher = self.searcher_positions[i]
            #
            good_entry = self.__go_dijkstra__(self.searcher_positions,i)
            if good_entry:
                kept_search_positions.append(searcher)
            #if searcher[1]==(self.rows-1):
            if searcher[0]==self.goal_position[0] and searcher[1]==self.goal_position[1]:
                print("Found Solution after :" +str(self.searcher_step) + " steps")
                self.Done = True

        self.searcher_positions = kept_search_positions
        #self.searcher_positions.remove(None)
        #self.searcher_positions = list(filter(lambda x: x != [-1,-1], self.searcher_positions))

    def update_searchers(self):
        #
        new_searcher_positions=[]
        for i in range(len(self.searcher_positions)):#searcher in self.searcher_positions:
            searcher = self.searcher_positions[i]
            # get up map value
            map_up      = self.get_map_value_xy(searcher[0]  ,searcher[1]-1)
            if map_up == 0:
                new_searcher_positions.append([searcher[0]  ,searcher[1]-1])
            # get up map value
            map_down    = self.get_map_value_xy(searcher[0]  ,searcher[1]+1)
            if map_down == 0:
                new_searcher_positions.append([searcher[0]  ,searcher[1]+1])
            # get up map value
            map_left    = self.get_map_value_xy(searcher[0]-1,searcher[1]  )
            if map_left == 0:
                new_searcher_positions.append([searcher[0]-1,searcher[1]  ])
            # get up map value
            map_right   = self.get_map_value_xy(searcher[0]+1,searcher[1]  )
            if map_right == 0:
                new_searcher_positions.append([searcher[0]+1,searcher[1]  ])

            
        #
        self.searcher_positions.extend(new_searcher_positions)
        #
        for i in range(len(self.searcher_positions)):
            #
            searcher = self.searcher_positions[i]
            #
            self.__go_dijkstra__(self.searcher_positions,i)
            #if searcher[1]==(self.rows-1):
            if searcher[0]==self.goal_position[0] and searcher[1]==self.goal_position[1]:
                print("Found Solution after :" +str(self.searcher_step) + " steps")
                self.Done = True

        #self.searcher_positions.remove(None)
        self.searcher_positions = list(filter(lambda x: x != [-1,-1], self.searcher_positions))


    def add_storm(self,storm=blizzard()):
        self.storms.append(storm)
        self.__storm_to_map__(storm)

    def update(self):
        # Reinitialize current map
        self.map = copy.deepcopy(self.base_map)
        # Update storms
        for storm in self.storms:
            # Moving boolean
            moving = True
            # While loop
            while(moving):
                # Storm update
                storm.update()
                # Wrap values to within map
                storm.wrap(self.rows,self.cols)
                # Update current map
                moving = self.__storm_to_map__(storm)
        #
        self.update_dijkstra()
        #Copy current map to maps
        if self.Debug:
            self.maps.append(copy.deepcopy(self.map))
        
    def __storm_to_map__(self,storm):
        #
        ContinueMoving = False
        # 
        cur_value = self.get_map_value_xy(storm.x,storm.y)
        #
        if (cur_value == -1):
            ContinueMoving = True
        elif (cur_value > 0) and (cur_value < 10):
            self.set_map_value_xy(storm.x,storm.y, cur_value + 1)
        elif (cur_value == 11) or (cur_value == 12) or (cur_value == 13) or (cur_value == 14):
            self.set_map_value_xy(storm.x,storm.y, 2)
        else:
            if storm.direction == StormMovement.UP :
                self.set_map_value_xy(storm.x,storm.y, 11)
            elif storm.direction == StormMovement.DOWN :
                self.set_map_value_xy(storm.x,storm.y, 12)
            elif storm.direction == StormMovement.LEFT :
                self.set_map_value_xy(storm.x,storm.y, 13)
            elif storm.direction == StormMovement.RIGHT :
                self.set_map_value_xy(storm.x,storm.y, 14)
            else:
                self.set_map_value_xy(storm.x,storm.y, 1)
        #
        return ContinueMoving

    def dijkstra_to_string(self):
        #
        d = self.dijkstra
        #

        str_map = ""
        for y in range(self.rows):
            for x in range(self.cols):
                value = d[y][x]+1
                str_map += str(value).rjust(6," ")
            str_map += "\r\n"
        return str_map   

    def map_to_string(self):
        str_map = ""
        for y in range(self.rows):
            for x in range(self.cols):
                value = self.map[y][x] # 
                if value == -1:     # Wall etc
                    char = "#"
                elif value == 1:
                    char = "1"
                elif value == 2:
                    char = "2"
                elif value == 3:
                    char = "3"
                elif value == 4:
                    char = "4"
                elif value == 11:
                    char = "^"
                elif value == 12:
                    char = "v"
                elif value == 13:
                    char = "<"
                elif value == 14:
                    char = ">"
                else:#value == 0:    # Nothing there
                    char = "."
                str_map += str(char)
            str_map += "\r\n"
        return str_map


cur_path = os.getcwd()
cur_dir = os.path.dirname(__file__)

time_per_goal = []
tic = time.time_ns()
if False:
    Debug = 2
    M = storm_map(8,6)
    goals = [[6,5],[1,0],[6,5]]
    filename = "TestMap.dat"
else:
    Debug = 0
    M = storm_map(102,37,False)
    goals = [[100,36],[1,0],[100,36]]
    filename = "AdventOfCodeDat.dat"
file_path = os.path.join(cur_dir,filename)
M.load_map_and_stroms(file_path)

goals_reached = 0
goal_steps = []
toc = time.time_ns()
time_per_goal.append((toc-tic)/ (10 ** 9))
tic = time.time_ns()
for iii in range(1000):
    M.update()
    if Debug==1:
        print(M.map_to_string())
        print(M.dijkstra_to_string())
        time.sleep(0.05)
    elif Debug==1:
        print('.',end ="")
        if iii%100==0 and iii!=0:
            print('')
    if M.Done:
        goal_steps.append(M.searcher_step)
        toc = time.time_ns()
        time_per_goal.append((toc-tic)/ (10 ** 9))
        tic = time.time_ns()
        if goals_reached < len(goals)-1:
            old_goal = goals[goals_reached]
            goals_reached += 1
            new_goal = goals[goals_reached]
            M.reset_dijkstra_and_set_goal(old_goal[0],old_goal[1],new_goal[0],new_goal[1])
        else:
            break

if not Debug:
    print('')
    print(M.map_to_string())

print("time required to reach goals : ")
print(time_per_goal)
print("steps required to reach goals : ")
print(goal_steps)
print("total steps required to reach goals : ")
print(sum(goal_steps))