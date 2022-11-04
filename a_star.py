import copy

class puzzle_instance:
    def __init__(self, row, col, state):
        self.space = [row, col]
        self.state = state
        self.h_score = -1

    def move_right(self):
        if(self.space[1] == 2):
            # print("cannot move the space right")
            pass
        else:
            temp = self.state[self.space[0]][self.space[1]+1]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]][self.space[1]+1] = -1
            self.space = [self.space[0],self.space[1]+1]   
    def move_left(self):
        if(self.space[1] == 0):
            pass
            
        else:
            temp = self.state[self.space[0]][self.space[1]-1]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]][self.space[1]-1] = -1
            self.space = [self.space[0],self.space[1]-1]

    def move_up(self):
        if(self.space[0] == 0):
            pass
            
        else:
            temp = self.state[self.space[0]-1][self.space[1]]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]-1][self.space[1]] = -1
            self.space = [self.space[0]-1,self.space[1]]

    def move_down(self):
        if(self.space[0] == 2):
            pass
            
        else:
            temp = self.state[self.space[0]+1][self.space[1]]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]+1][self.space[1]] = -1
            self.space = [self.space[0]+1,self.space[1]]

    def get_h_score(self, final_state):
        h=0
        if self.state == final_state:
            return h
        else:
            for i in range(len(self.state)):
                for j in range(len(self.state[i])):
                    if self.state[i][j] != final_state[i][j]:
                        h+=1
        return h
 

def generate_children(puzzle):
    ret = []
    temp1 = copy.deepcopy(puzzle)
    temp1.move_left()
    ret.append(temp1)
    temp2 = copy.deepcopy(puzzle)
    temp2.move_right()
    ret.append(temp2)
    temp3 = copy.deepcopy(puzzle)
    temp3.move_up()
    ret.append(temp3)
    temp4 = copy.deepcopy(puzzle)
    temp4.move_down()
    ret.append(temp4)

    return ret


def a_star(puzzle, goal_state):
    closed_list = []
    closed_list.append(puzzle)
    g=0
    while(True):
        puzzle.h_score = puzzle.get_h_score(goal_state)
        if puzzle.h_score  == 0:
            print(f"Reached goal at g={g}")
            return closed_list
        else:
            children = generate_children(puzzle)
            g+=1
            f_score = 999
            for i in children:
                i.h_score = i.get_h_score(goal_state)
                temp = g+i.h_score
                if temp<f_score:
                    f_score = temp
                    puzzle = i
            closed_list.append(puzzle)
    return []


def show_path(closed_list):
    for i in closed_list:
        print(i.state)

if __name__ == '__main__':
    first_state = [
    [1,2,3],
    [4,-1,6],
    [7,8,9]
    ]
    #print(first_state)
    puzzle = puzzle_instance(1,1,first_state)
    print("*****************************")
    goal_state = [
    [1,2,3],
    [4,8,6],
    [-1,7,9]
    ]
    ans = a_star(puzzle, goal_state)
    show_path(ans)
