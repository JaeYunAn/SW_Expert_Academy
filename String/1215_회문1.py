for tc in range(1, 11):
    M = int(input())
    matrix = [list(input()) for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8 - M + 1):
            text_row = []
            for k in range(M):
                text_row.append(matrix[i][j + k])
            if text_row == text_row[::-1]:
                count += 1

    for j in range(8):
        for i in range(8 - M + 1):
            text_col = []
            for k in range(M):
                text_col.append(matrix[i + k][j])
            if text_col == text_col[::-1]:
                count += 1
    print(f'#{tc} {count}')