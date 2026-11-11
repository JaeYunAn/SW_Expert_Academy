'''
2
5 2
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
4 4
4 4
7 3
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35
36 37 38 39 40 41 42
43 44 45 46 47 48 49
1 1 1
1 1 1
1 1 1
'''

'''
#1
20 20 20 20
20 20 20 20
20 20 20 20
20 20 20 20
#2
90 99 108 117 126
153 162 171 180 189
216 225 234 243 252
279 288 297 306 315
342 351 360 369 378
'''

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_lens = [list(map(int, input().split())) for _ in range(M)]
    matrix_lens_new = [[0] * (N - M + 1) for _ in range(N - M + 1)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            energy = 0
            for k in range(M):
                for L in range(M):
                    energy += (matrix[i + k][j + L] + matrix_lens[k][L])
            matrix_lens_new[i][j] = energy

    print(f'#{tc}')
    for row in matrix_lens_new:
        print(*row)