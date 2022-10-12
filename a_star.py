class puzzle_instance:
    def __init__(self, row, col, state):
        self.space = [row, col]
        self.state = state
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

 

def h_score(mat1, mat2):
    h=0
    if mat1==mat2:
        return 0
    else:
        for i in range(len(mat1)):
            for j in range(len(i)):
                if mat1[i][j] == mat2[i][j]:
                    continue
                else:
                    h+=1
    return h


def a_star(puzzle, goal_state):
    open_list = []
    closed_list = []
    closed_list.append(puzzle)
    g=0
    while(True):
        h_score = h_score(puzzle.state, goal_state)
        if h_score  == 0:
            print(f"Reached goal at g={g}")
            break







if __name__ == '__main__':
    first_state = [
    [1,2,3],
    [4,5,6],
    [7,8,-1]
    ]
    #print(first_state)
    puzzle = puzzle_instance(2,2,first_state)
    print(puzzle.state)
    puzzle.move_left()
    print(puzzle.state)
    puzzle.move_up()
    print(puzzle.state)
    puzzle.move_right()
    print(puzzle.state)
    puzzle.move_down()
    print(puzzle.state)
