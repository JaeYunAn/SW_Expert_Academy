'''
3
2 3
0 1 1
0 2 6
1 2 1
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
#2 4
#3 10
'''

from heapq import heappop, heappush
 
def dijkstra(s):
    heap = []
    heappush(heap, (0, s))
    D[s] = 0
 
    while heap:
        w, v = heappop(heap)
 
        if w > D[v]:
            continue
 
        for nv, nw in G[v]:
            new_distance = w + nw
 
            if new_distance < D[nv]:
                D[nv] = new_distance
                heappush(heap, (new_distance, nv))
 
 
T = int(input())
 
for t in range(1, T + 1):
    V, E = map(int, input().split())
 
    G = [[] for _ in range(V + 1)]
 
    for i in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
         
    INF = 10 ** 9
    D = [INF] * (V + 1)
 
    dijkstra(0)
 
    ans = D[V]
    print(f"#{t} {ans}")