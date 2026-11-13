from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
opposite = [1, 0, 3, 2]

pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    q = deque()
    q.append((R, C))
    visited[R][C] = 1
    count = 1
    
    while q:
        r, c = q.popleft()
        if visited[r][c] == L:
            continue
        
        for d in pipe[matrix[r][c]]:
            ni = r + di[d]
            nj = c + dj[d]
            
            if 0 <= ni <= N - 1 and 0 <= nj <= M - 1 and visited[ni][nj] == 0:
                if opposite[d] in pipe[matrix[ni][nj]]:
                    visited[ni][nj] = visited[r][c] + 1
                    count += 1
                    q.append((ni, nj))
    print(f'#{tc} {count}')