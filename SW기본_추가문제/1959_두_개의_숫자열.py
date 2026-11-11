'''
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
'''

'''
#1 30
#2 63
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        Aj, Bj = Bj, Aj
    max_sum = 0
    for i in range(M - N + 1):
        current_sum = 0
        for j in range(N):
            current_sum += Bj[i + j] * Aj[j]
        if current_sum > max_sum:
            max_sum = current_sum
    print(f'#{tc} {max_sum}')