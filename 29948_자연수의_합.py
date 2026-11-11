'''
3
1
10
10000
'''

'''
#1 1
#2 4
#3 141
'''

T = int(input())

for tc in range(1, T + 1):
    M = int(input())

    N = 0
    S = 0

    while True:
        N += 1
        S += N

        if S >= M:
            break
    print(f'#{tc} {N}')