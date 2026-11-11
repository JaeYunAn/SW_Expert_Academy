'''
3
12 4
1 0 0 0 1 0 0 0 1 0 0 0
8 3
1 0 0 1 0 0 1 0
8 3
1 1 0 0 0 0 0 0
'''

'''
#1 12
#2 8
#3 5
'''

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    leaf = list(map(int, input().split()))

    i = 0
    is_alive = True

    while i < N - 1 and is_alive:
        for j in range(K, 0, -1): 
            if i + j <= N - 1 and leaf[i + j] == 1:
                i += j
                break
        else:
            if i + K > N - 1:
                i = N - 1
            else:
                i = i + K
            is_alive = False

    answer = i + 1
    print(f'#{tc} {answer}')