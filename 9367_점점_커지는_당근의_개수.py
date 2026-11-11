'''
4
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
8
1 2 1 2 3 1 2 1
'''

'''
#1 5
#2 3
#3 1
#4 3
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    count_list = []
    count = 1
    count_list.append(1)
    for i in range(1, N):
        if C[i] > C[i - 1]:
            count += 1
            count_list.append(count)
        elif C[i] <= C[i - 1]:
            count = 1
            count_list.append(count)
    print(f'#{tc} {max(count_list)}')