'''
5
1
2
11
1295
1692
'''

'''
#1 10
#2 90
#3 110
#4 6475
#5 5076
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = ''
    i = 1
    count = 0
    while True:
        numbers += str(N * i)
        i += 1
        count += 1
        if '0' in numbers and '1' in numbers and '2' in numbers and '3' in numbers and '4' in numbers and '5' in numbers and '6' in numbers and '7' in numbers and '8' in numbers and '9' in numbers:
            break
    print(f'#{tc} {N * count}')