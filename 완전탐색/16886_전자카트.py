'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''

'''
#1 89
#2 96
#3 139
'''

T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    Energy = [list(map(int, input().split())) for _ in range(N)]
    answer = 10000

    def solve(now, visited, e):
        global answer
        
        if len(visited) == N:
            e += Energy[now][0]

            if e < answer:
                answer = e
            return

        for i in range(N):
            if i not in visited:
                solve(i, visited + [i], e + Energy[now][i])
    solve(0, [0], 0)
     
    print(f"#{tc} {answer}")