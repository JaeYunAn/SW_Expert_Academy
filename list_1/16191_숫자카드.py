'''
3
5
49679
5
08271
10
7797946543
'''

'''
#1 9 2
#2 8 1
#3 7 3
'''

T = int(input())

for tc in range(1, T + 1):

    card = int(input())
    card_numbers_input = int(input())

    card_numbers = [0] * 10

    for i in range(card):
        card_numbers[card_numbers_input % 10] += 1
        card_numbers_input //= 10

    max_count = 0
    max_num = 0

    for i in range(10):

        if card_numbers[i] >= max_count:
            max_count = card_numbers[i]
            max_num = i

    print(f'#{tc} {max_num} {max_count}')