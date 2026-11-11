T = int(input())

def diet(i, score, cal):
    global max_score

    if cal > K:
        return
    
    if i == N:
        max_score = max(max_score, score)
        return

    diet(i + 1, score + matrix[i][0], cal + matrix[i][1])

    diet(i + 1, score + 0, cal + 0)

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0

    diet(0, 0, 0)

    print(f'#{tc} {max_score}')