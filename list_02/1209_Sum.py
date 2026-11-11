for _ in range(10):
    tc = int(input())

# 매트릭스
    matrix = [list(map(int, input().split())) for _ in range(100)]

# 각 합이 들어갈 빈 리스트
    sum_list = []

# 행의 합
    for i in matrix:
        sum_list.append(sum(i))

# 열의 합
    for j in range(100):
        col_sum = 0

        for i in range(100):
            col_sum += matrix[i][j]

        sum_list.append(col_sum)

# 정방향 대각선의 합  
    cross_sum = 0

    for i in range(100):
        for j in range(100):
            if i == j:
                cross_sum += matrix[i][j]
    sum_list.append(cross_sum)

# 역방향 대각선의 합  
    cross_sum_reverse = 0

    for i in range(100):
        for j in range(100):
            if 100 - 1 - i == j:
                cross_sum_reverse += matrix[i][j]
    sum_list.append(cross_sum_reverse)
 
    print(f'#{tc} {max(sum_list)}')