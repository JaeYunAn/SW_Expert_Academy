'''
1
5
14054
44250
02032
51204
52212
'''

'''
#1 23
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    center = N // 2
    crop_sum = 0

    for i in range(N):
        for j in range(N):
            if abs(i - center) + abs(j - center) <= center:
                crop_sum += matrix[i][j]
    print(f'#{tc} {crop_sum}')