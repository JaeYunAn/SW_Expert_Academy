'''
2
10
1234567890
4
2467
10
1234567890
4
2475
'''

'''
#1 1
#2 0
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_N = list(map(int, input()))
    M = int(input())
    num_M = list(map(int, input()))
    answer = 1
    num_list = []
    for i in num_M:
        for j in range(N):
            if i == num_N[j]:
                num_list.append(i)
                num_N[j] = -1
                break
            else:
                num_N[j] = -1
    if num_list != num_M:
        answer = 0
    print(f'#{tc} {answer}')