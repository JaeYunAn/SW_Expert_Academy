'''
3
5 5
WWWWW
WLLWW
WLWWW
WWLWW
WWLLW
5 7
LLLLLLL
LLLLLLL
LLLLLLL
LLLLLLL
LLLLLLL
6 6
LWLWLW
WLWLWL
LWLWLW
WLWLWL
LWLWLW
WLWLWL
'''

'''
#1 2
#2 1
#3 18
'''

from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'L' and visited[i][j] == 0:
                count += 1

                q = deque()
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    ci, cj = q.popleft()

                    for d in range(4):
                        ni = ci + di[d]
                        nj = cj + dj[d]

                        if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 'L' and visited[ni][nj] == 0:
                            q.append((ni, nj))
                            visited[ni][nj] = 1
    print(f'#{tc} {count}')