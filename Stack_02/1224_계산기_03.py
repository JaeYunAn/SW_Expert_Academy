T = 10
 
for tc in range(1, T + 1):
    N = int(input())
    expression = input()
 
    stack = []
    result = ''
 
    for c in expression:
        if '0' <= c <= '9':
            result += c
 
        elif c == '(':
            stack.append(c)
 
        elif c == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
 
        elif c == '*':
            while stack and stack[-1] == '*':
                result += stack.pop()
            stack.append(c)
 
        elif c == '+':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(c)
 
    while stack:
        result += stack.pop()
 
    stack = []
 
    for c in result:
        if '0' <= c <= '9':
            stack.append(int(c))
        else:
            b = stack.pop()
            a = stack.pop()
 
            if c == '+':
                stack.append(a + b)
            elif c == '*':
                stack.append(a * b)
 
    print(f'#{tc} {stack.pop()}')