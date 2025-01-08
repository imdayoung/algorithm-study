import sys
import heapq


T = int(sys.stdin.readline())
for _ in range(T):
    answer = 1
    energies = [1]
    
    N = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(C)
    
    while len(C) > 1:
        A = heapq.heappop(C)
        B = heapq.heappop(C)
        
        energy = A * B
        
        heapq.heappush(C, energy)
        energies.append(energy)
    
    for energy in energies:
        answer = answer * energy % 1000000007

    print(answer)
