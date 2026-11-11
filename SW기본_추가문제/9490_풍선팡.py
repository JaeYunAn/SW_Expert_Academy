'''
3
3 5
2 1 1 2 2 
2 2 1 2 2 
2 2 1 1 2 
5 5
3 4 1 2 3 
3 4 1 3 2 
2 3 2 4 1 
1 4 4 1 3 
2 2 3 4 4 
5 8
1 3 4 4 4 4 3 3 
4 1 2 4 3 1 4 4 
4 1 4 4 1 4 2 1 
3 2 4 2 1 1 2 1 
4 4 1 4 4 2 2 2 
'''

'''
#1 10
#2 26
#3 40
'''

T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(M):

            count = arr[i][j]

            for k in range(1, count + 1):
                for d in range(4):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k

                    if 0 <= ni < N and 0 <= nj < M:
                        count += arr[ni][nj]

            answer = max(answer, count)
    print(f'#{tc} {answer}')