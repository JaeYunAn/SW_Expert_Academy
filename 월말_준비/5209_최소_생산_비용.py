'''

3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4
'''

'''
#1 63
#2 78
#3 129
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    row_min = []
    for row in matrix:
        row_min.append(min(row))

    path = []
    visited = [0] * N
    answer = float('inf')

    def perm(depth):
        global answer

        if sum(path) + sum(row_min[depth:]) >= answer:
            return

        if depth == N:
            answer = sum(path)
            return

        for j in range(N):
            if visited[j] == 1:
                continue

            path.append(matrix[depth][j])
            visited[j] = 1

            perm(depth + 1)

            path.pop()
            visited[j] = 0
    perm(0)
    print(f'#{tc} {answer}')