# Give three buckets, the capacity is 8, 5, 3
# the init water in three buckets are 8, 0 ,0
# swaq the water and the make the water to 4,4,0
# return all the possible sequence.
# [(8, 0, 0), (3, 5, 0), (3, 2, 3), (6, 2, 0), (6, 0, 2), (1, 5, 2), (1, 4, 3), (4, 4, 0)]
# [(8, 0, 0), (5, 0, 3), (5, 3, 0), (2, 3, 3), (2, 5, 1), (7, 0, 1), (7, 1, 0), (4, 1, 3), (4, 4, 0)]


# search [8,0,0] to [4,4,0]
# max capicity (8,5,3)
def help(num1, num2, cap1, cap2):
    if num2 == cap2:
        return num1, num2
    
    slot = cap2 - num2

    if num1 > slot:
        return num1 - slot, cap2
    
    return 0, num2 + num1

def transfer_state(state):
    res = []
    capacity = [8, 5, 3]
    for i in range(3):
        for j in range(3):
            if i == j: continue
            n1, n2 = help(state[i], state[j], capacity[i], capacity[j])
            s = list(state)
            s[i], s[j] = n1, n2        
            res.append(tuple(s))
    return res

from collections import deque            
def search():
    parent = {}
    init_state = (8,0,0)
    final_state = (4,4,0)

    visited = []
    queue = deque()
    queue.append(init_state)

    paths = []

    while queue:
        state = queue.popleft()
        if state == final_state:
            paths.append(backtrack(parent, init_state, final_state))
            continue
        visited.append(state)
        states = transfer_state(state)
        for s in states:
            if s in visited:
                continue
            parent[s] = state
            queue.append(s)

    return paths

def backtrack(g, start, end):
    path = [end]
    while path[-1] != start:
        path.append(g[path[-1]])
    
    path.reverse()
    return path

all_paths = search()
for path in all_paths:
    print(path)