'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''

'''
#1 2
#2 0
#3 3
'''

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    A.sort()

    for i in B:
        left = 0
        right = N - 1

        D = -1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == i:
                count += 1
                break

            elif A[mid] > i:
                right = mid - 1
                if D == 0:
                    break
                else:
                    D = 0

            elif A[mid] < i:
                left = mid + 1
                if D == 1:
                    break
                else:
                    D = 1
    
    print(f'#{tc} {count}')