'''
3
3 6
5 15
5 10
'''

'''
#1 1
#2 1
#3 0
'''

T = int(input())

arr = [i for i in range(1, 13)]
N = 12

for tc in range(1, T + 1):

    n, k = map(int, input().split())

    answer = 0

    for i in range(1 << N):

        ith_cnt = 0
        ith_sum = 0
        
        for j in range(N):
            if i & (1 << j):
                ith_sum += arr[j]
                ith_cnt += 1
    
        if ith_sum == k and ith_cnt == n:
            answer += 1
    
    print(f'#{tc} {answer}')