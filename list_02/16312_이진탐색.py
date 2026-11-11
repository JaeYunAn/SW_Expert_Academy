'''
3
400 300 350
1000 299 578
1000 222 888
'''

'''
#1 A
#2 0
#3 A
'''

def binary_search(P, key):
    start = 1
    end = P
    count = 0
 
    while start <= end:
        count += 1
        middle = (start + end) // 2
 
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
 
T = int(input())
for t in range(1, T + 1):
    P, A, B = map(int, input().split())
 
    count_a = binary_search(P, A)
    count_b = binary_search(P, B)
 
    if count_a < count_b:
        winner = 'A'
    elif count_b < count_a:
        winner = 'B'
    else:
        winner = '0'
 
    print(f'#{t} {winner}')