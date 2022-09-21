from queue import PriorityQueue 


def hueristic(node): 
    dist_dict = { 0: 5, 1: 6, 2: 2, 3: 1, 4: 0} 
    return dist_dict[node] 


adj_mat = [[1,2],[0,3,4],[0,3,4],[0,1,2,4],[1,2,3]] 
visited = list() 


for i in range(5): 
    visited.append(False) 
start_state = 0 
goal_state = 4 
pq =PriorityQueue() 
pq.put((hueristic(start_state),start_state)) 
path= [] 


while(not pq.empty()): 
    h,state= pq.get() 
    visited[state] = True 
    path.append(state) 
    if(state == goal_state): 
        break;
    else: 
        mat = adj_mat[state]; 
        for i in adj_mat[state]: 
            if(visited[i] == False): 
            pq.put((hueristic(i),i)) 

print(f"Final Path: {path}") 

