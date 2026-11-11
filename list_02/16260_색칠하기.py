'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

'''
#1 4
#2 5
#3 7
'''

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    paper = [[0] * 10 for _ in range(10)]
    purple = 0

    for _ in range(N):
        i1, j1, i2, j2, color = list(map(int, input().split()))

        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                paper[i][j] += color

                if paper[i][j] == 3:
                    purple += 1
    
    print(f'#{tc} {purple}')