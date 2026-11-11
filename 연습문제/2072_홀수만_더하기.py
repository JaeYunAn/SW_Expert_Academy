'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1 
'''

'''
#1 200
#2 208
#3 121
'''

T = int(input())

for tc in range(1, T + 1):
    input_numbers = list(map(int, input().split()))

    total = 0

    for num in input_numbers:
        if num % 2 == 1:
            total += num

    print(f'#{tc} {total}')
