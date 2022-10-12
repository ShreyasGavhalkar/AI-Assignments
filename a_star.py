import copy

class puzzle_instance:
    def __init__(self, row, col, state):
        self.space = [row, col]
        self.state = state
        self.h_score = -1
    def move_right(self):
        if(self.space[1] == 2):
            print("cannot move the space right")
        else:
            temp = self.state[self.space[0]][self.space[1]+1]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]][self.space[1]+1] = -1
            self.space = [self.space[0],self.space[1]+1]   
    def move_left(self):
        if(self.space[1] == 0):
            print("cannot move the space left")
        else:
            temp = self.state[self.space[0]][self.space[1]-1]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]][self.space[1]-1] = -1
            self.space = [self.space[0],self.space[1]-1]

    def move_up(self):
        if(self.space[0] == 0):
            print("cannot move the space up")
        else:
            temp = self.state[self.space[0]-1][self.space[1]]
            self.state[self.space[0]][self.space[1]] = temp
            self.state[self.space[0]-1][self.space[1]] = -1
            self.space = [self.space[0]-1,self.space[1]]

    def move_down(self):
        if(self.space[0] == 2):
            print("cannot move the space down")
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
    state = copy.deepcopy(puzzle.state)
    space = copy.deepcopy(puzzle.space)
    temp1 = puzzle_instance(space[0], space[1], state)
    temp2 = puzzle_instance(space[0], space[1], state)
    temp3 = puzzle_instance(space[0], space[1], state)
    temp4 = puzzle_instance(space[0], space[1], state)
    return []


def a_star(puzzle, goal_state):
    breakpoint()
    closed_list = []
    closed_list.append(puzzle)
    g=0
    while(True):
        puzzle.h_score = puzzle.get_h_score(goal_state)
        if puzzle.h_score  == 0:
            print(f"Reached goal at g={g}")
            closed_list.append(puzzle)
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
    [7,-1,9]
    ]
    ans = a_star(puzzle, goal_state)
    show_path(ans)
    print("*********************************")
