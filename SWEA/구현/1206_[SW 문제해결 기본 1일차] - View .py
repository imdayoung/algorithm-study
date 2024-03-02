for i in range(1, 11):
    cnt = 0
    n = int(input())
    buildings = list(map(int, input().split()))
     
    for j in range(2, n - 2):
        max_neighbor = max(buildings[j - 2], buildings[j - 1], buildings[j + 1], buildings[j + 2])
        if buildings[j] < max_neighbor:
            continue
         
        cnt = cnt + buildings[j] - max_neighbor
 
    print("#"+str(i), end = " ")
    print(cnt)