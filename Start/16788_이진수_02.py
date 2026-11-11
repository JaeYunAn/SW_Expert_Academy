'''
3
0.625
0.1
0.125
'''

'''
#1 101
#2 overflow
#3 001
'''

T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    arr = []

    while N != 0:
        N *= 2

        if N >= 1:
            arr.append(1)
            N -= 1
        else:
            arr.append(0)

        if len(arr) == 13:
            break

    if len(arr) >= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', ''.join(map(str, arr)))