'''
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907
'''

'''
#1 731
#2 18641
#3 2412
'''

from collections import deque

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    que = deque()

    for i in numbers:
        que.append(i)

    for i in range(M):
        number = que.popleft()
        que.append(number)

    print(f'#{tc} {que[0]}')