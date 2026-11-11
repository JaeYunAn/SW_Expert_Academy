'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
'''

'''
#1 1
#2 4
#3 11
'''

T = int(input())

for tc in range(1, T + 1):
    text = input()

    top = -1
    stack = [0] * len(text)

    for i in text:
        top += 1
        stack[top] = i
        if stack[top] == stack[top - 1]:
            stack.pop(top)
            stack.pop(top - 1)
            top -= 2

    print(f'#{tc} {len(stack)}')