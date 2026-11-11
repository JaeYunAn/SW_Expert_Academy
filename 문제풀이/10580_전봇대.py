T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    cnt = 0
    for i in range(1, N):
        for j in range(i):
            if arr[j][1] > arr[i][1]:
                cnt += 1
    print(f"#{tc} {cnt}")
