'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''

'''
#1 15
#2 18
#3 33
'''

di = [0, 1]
dj = [1, 0]

def solve(i, j, now_sum):
    global answer

    if (i, j) == (N - 1, N - 1):

        if now_sum < answer:
            answer = now_sum
        return

    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < N:
            solve(ni, nj, now_sum + matrix[ni][nj])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = float('inf')

    solve(0, 0, matrix[0][0])

    print(f"#{tc} {answer}")