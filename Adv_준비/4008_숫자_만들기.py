T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    card_list = []
    for i in range(4):
        if i == 0:
            for j in range(card[i]):
                card_list.append('+')
        elif i == 1:
            for j in range(card[i]):
                card_list.append('-')
        elif i == 2:
            for j in range(card[i]):
                card_list.append('*')
        elif i == 3:
            for j in range(card[i]):
                card_list.append('/')
    path = []
    path_list = []
    visited = [0] * len(card_list)

    def perm(depth):
        if depth == len(card_list):
            path_list.append(path[:])
            return

        for i in range(len(card_list)):
            if visited[i] == 1:
                continue
            if i > 0 and card_list[i] == card_list[i - 1] and visited[i - 1] == 0:
                continue

            path.append(card_list[i])
            visited[i] = 1

            perm(depth + 1)

            path.pop()
            visited[i] = 0
    perm(0)

    max_answer = -100000000
    min_answer = 100000000
    answer_list = []

    for i in path_list:
        answer = numbers[0]
        for j in range(len(i)):
            if i[j] == '+':
                answer += numbers[j + 1]
            elif i[j] == '-':
                answer -= numbers[j + 1]
            elif i[j] == '*':
                answer *= numbers[j + 1]
            elif i[j] == '/':
                answer = int(answer / numbers[j + 1])
        if answer <= min_answer:
            min_answer = answer

    for i in path_list:
        answer = numbers[0]
        for j in range(len(i)):
            if i[j] == '+':
                answer += numbers[j + 1]
            elif i[j] == '-':
                answer -= numbers[j + 1]
            elif i[j] == '*':
                answer *= numbers[j + 1]
            elif i[j] == '/':
                answer = int(answer / numbers[j + 1])
        if answer >= max_answer:
            max_answer = answer

    print(f'#{tc} {max_answer - min_answer}')