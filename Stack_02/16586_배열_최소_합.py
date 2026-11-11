'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''

'''
#1 8
#2 14
#3 9
'''

# 핵심은 i번 행에서 j번 열을 골라서 합을 만들자, 대신 J는 중복 불가 0번행 => 0번열
def make_farm(i, selected, s):
    global answer
    if s >= answer:  #  가지치기: 더 볼 필요 없음
        return
    if i == N:
        if s < answer:
            answer = s
        return
 
    for j in range(N):
        if not selected[j]:
            selected[j] = 1
            make_farm(i+1, selected, s+matrix[i][j])
            selected[j] = 0
 
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
 
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    answer = 100
 
    make_farm(0, [0]*N, 0)
 
    print(f"#{tc} {answer}")