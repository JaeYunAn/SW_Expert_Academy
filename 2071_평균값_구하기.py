'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
'''

'''
#1 24
#2 29
#3 27
'''

T = int(input())

for tc in range(1, T + 1):
    input_numbers = list(map(int, input().split()))

    total = round(sum(input_numbers) / len(input_numbers))


    print(f'#{tc} {total}')