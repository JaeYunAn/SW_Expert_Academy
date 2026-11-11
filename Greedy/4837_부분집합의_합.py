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

for tc in range(1, T + 1):
    A = []
    for i in range(1, 13):
        A.append(i)

    N, K = map(int, input().split())
    path = []
    subset_list = []

    def subset(idx):
        if idx == len(A):
            subset_list.append(path[:])
            return

        subset(idx + 1)

        path.append(A[idx])
        subset(idx + 1)
        path.pop()

    subset(0)

    count = 0
    for i in range(len(subset_list)):
        if len(subset_list[i]) == N and sum(subset_list[i]) == K:
            count += 1

    print(f'#{tc} {count}')