'''
3
10
0011001110
10
0000100001
10
0111001111
'''

'''
#1 3
#2 1
#3 4
'''

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    nums = list(map(int, input()))
    count = 0
    counts = [0] * len(nums)

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            counts[i] = count
        else:
            count = 0

    print(f'#{tc} {max(counts)}')