'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''

'''
#1 2
#2 13
#3 22
'''

from heapq import heappop, heappush
 
def prim(s):
    heap = []
    MST = [0] * (V+1)
    MIN = 0
    cnt = 0
 
    heappush(heap, (0, s))
 
    while cnt < V+1 and heap:
        w, v = heappop(heap)
 
        if MST[v]:
            continue
 
        MST[v] = 1
        MIN += w
        cnt += 1
 
        for nv, nw in G[v]:
 
            if MST[nv]:
                continue
 
            heappush(heap, (nw, nv))
 
    return MIN
 
T = int(input())
 
for t in range(1, T + 1):
    V, E = map(int, input().split())
 
    G = [[] for _ in range(V+1)]
 
    for i in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
        G[e].append((s, w))
 
 
    print(f'#{t} {prim(0)}')