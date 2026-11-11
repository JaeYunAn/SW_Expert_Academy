'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
'''

'''
#1 21
#2 11088
#3 1090
'''

T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = 0
    min_sum = float('inf')

    for i in range(N - M + 1):
        current_sum = sum(arr[i: i + M])

        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum

    answer = max_sum - min_sum
        


    print(f'#{tc} {answer}')