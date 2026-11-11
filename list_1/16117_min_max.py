'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

'''
#1 630739
#2 740510
#3 838110
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    max_v = arr[0]
    min_v = arr[0]

    for i in range(1, N):
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]

    ans = max_v - min_v
        
    print(f'#{tc} {ans}')