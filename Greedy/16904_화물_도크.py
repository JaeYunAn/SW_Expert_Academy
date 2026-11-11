'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''

'''
#1 4
#2 4
#3 5
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    work_list = [list(map(int, input().split())) for _ in range(N)]
    work_list.sort(key = lambda e: e[-1])
    answer = 1
    last = work_list[0][1]

    for i in range(1, N):
        if work_list[i][0] >= last:
            answer += 1
            last = work_list[i][-1]

    print(f'#{tc} {answer}')