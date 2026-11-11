'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''

'''
#1 3
#2 2
#3 3
'''

def make_set(x):
    p[x] = x

def find_set(x):

    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)
    p[king_y] = king_x

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    p = [0] * (N + 1)
    for i in range(1, N + 1):
        make_set(i)

    for i in range(M):
        a = arr[i * 2]
        b = arr[i * 2 + 1]
        union(a, b)

    count = 0
    for i in range(1, N + 1):
        if p[i] == i:
            count += 1

    print(f'#{tc} {count}')