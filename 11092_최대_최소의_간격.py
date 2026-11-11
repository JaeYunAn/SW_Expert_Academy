'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3 
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10
'''

'''
#1 4
#2 6
#3 18
'''

T = int(input())

for tc in range(1, T + 1):

    num = int(input())
    nums = list(map(int, input().split()))

    min_idx = 0
    min_num = nums[0]
    max_idx = 0
    max_num = nums[0]

    for i in range(num):

        if nums[i] < min_num:
            min_num = nums[i]
            min_idx = i

        if nums[i] >= max_num:
            max_num = nums[i]
            max_idx = i

    print(f'#{tc} {abs(max_idx - min_idx)}')