'''
4
3 2 1
1 2 3
3 5 5
5 6 6
'''

'''
#1 -1
#2 0
#3 1
#4 2
'''

T = int(input())

for tc in range(1, T + 1):
    a, b, c = map(int, input().split())

    if a < b < c and a != 0 and b != 0 and c != 0:
        print(f'#{tc} 0')
        continue
    elif a < 1 or b < 2 or c < 3:
        print(f'#{tc} -1')
        continue
    eat = 0
    if b >= c:
        eat += b - (c - 1)
        b = c - 1
    if a >= b:
        eat += a - (b - 1)
        a = b - 1
    print(f'#{tc} {eat}')