T = int(input())

for t in range(1, T + 1):

    N = int(input())
    nums = map(int, input().split())

    nums = sorted(nums)

    print(f'#{t}', *nums)