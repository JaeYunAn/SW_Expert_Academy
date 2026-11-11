# 스택 외부(icp) 우선순위
icp = {"(": 3, "*": 2, "/": 2, "+": 1, "-": 1}
# 스택 내부(isp) 우선순위
isp = {"(": 0, "*": 2, "/": 2, "+": 1, "-": 1}
 
def get_post_fix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""
 
    # 연산자를 저장할 스택
    stack = []
 
    for i in range(n):
        # 중위표기식 i번째 토큰(연산자인지 피연산자인지)
        if infix[i] not in "()+-*/":
            postfix += infix[i]
        else:
            # 연산자
            # 오른쪽 괄호
            # 스택 안에 있는 연산자
            # 왼쪽 괄호를 꺼낼 때
            if infix[i] == ")":
                while stack:
                    # 연산자 하나 꺼내서
                    op = stack.pop()
                    # 왼쪽 괄호이면 꺼내기 중단
                    if op == "(":
                        break
                    postfix += op
 
            else:
                # 스택에서 연산자를 꺼내는 상황부터 체크
                # 현재 연산자 보다 우선순위가 같거나 높은 연산자가 스택에 있는 경우
                # infix[i]의 우선순위 <= stack의 꼭대기 연산자의 우선순위
 
                # 스택 안의 연산자의 우선순위가 높으므로 먼저 계산이 되어야 한다.
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    postfix += stack.pop()
 
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
 
    return postfix
 
def get_result(postfix):
    stack = []
 
    for c in postfix:
        # c가 연산자인지 피연산자인지
        if c not in "+-*/":
            stack.append(int(c))
        else:
            e = stack.pop()
            s = stack.pop()
            result = 0
 
            if c == "+":
                result = s + e
            elif c == "-":
                result = s - e
            elif c == "*":
                result = s * e
            elif c == "/":
                # 계산 결과 실수
                result = s // e
 
            stack.append(result)
    return stack.pop()
 
for t in range(1, 11):
    N = int(input())
    susik = input()
    postfix = get_post_fix(susik, N)
    result = get_result(postfix)
    print(f'#{t} {result}')