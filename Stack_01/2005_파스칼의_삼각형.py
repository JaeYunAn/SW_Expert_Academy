'''
1
4
'''

'''
#1
1
1 1
1 2 1
1 3 3 1
'''

T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = []
 
    for i in range(N):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = arr[i - 1][j - 1] + arr[i - 1][j]
 
        arr.append(row)
 
    print(f'#{tc}')
    for row in arr:
        print(*row)