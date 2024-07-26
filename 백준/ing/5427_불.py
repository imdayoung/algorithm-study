import sys
sys.stdin = open("input.tt")
# import deepcopy


# def get_next_map(graph):
    
    

answers = []
t = int(sys.stdin.readline())

for _ in range(t):
    answer = "IMPOSSIBLE"
    
    w, h = map(int, sys.stdin.readline().split())
    building_map = []
    fire_to_spread = []
    cur_x, cur_y = 0, 0
    
    for i in range(h):
        temp = list(map(str, sys.stdin.readline().rstrip()))
        for j in range(w):
            if temp[j] == '*':
                fire_to_spread.append((i, j))
            elif temp[j] == "@":
                cur_x, cur_y = i, j
                
        building_map.append(temp)
        
    