'''
4
667767
054060
101123
456789
'''

'''
#1 Baby Gin
#2 Baby Gin
#3 Lose
#4 Baby Gin
'''

T = int(input())
for tc in range(1, T + 1):

    num = int(input())

    c = [0] * 12

    for i in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = 0
    rum = 0

    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            rum += 1
            continue
        i += 1

    if tri + rum == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')