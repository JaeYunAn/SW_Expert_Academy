'''
10
0 0 254 185 76 227 84 175 0 0
10
0 0 251 199 176 27 184 75 0 0
11
0 0 118 90 243 178 99 100 200 0 0
'''

'''
#1 111
#2 60
#3 165
'''

for tc in range(10):

    N = int(input())
    buildings = list(map(int, input().split()))

    answer = 0

    for i in range(2, N - 2):

        building = buildings[i - 2: i + 3]
        building = sorted(building)

        if buildings[i] == building[-1]:

            height = buildings[i] - building[-2]

            answer += height

    print(f'#{tc + 1} {answer}')