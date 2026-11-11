# 10개 테스트 케이스 고정
for tc in range(1, 11):
    # 노드 개수(N번까지 있다.)
    N = int(input())
 
    # 노드의 문자, 왼쪽 자식, 오른쪽 자식
    ch = [''] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
 
    # N줄에 걸쳐 정점 정보가 들어온다
    for _ in range(N):
        # 형태 1) "2 F 4 5"  - 자식 둘
        # 형태 2) "7 E 12"   - 왼쪽 자식만
        # 형태 3) "8 S"      - 리프
        info = input().split()
 
        # 정점 번호
        p = int(info[0])
        # 정점의 문자
        ch[p] = info[1]
 
        # 토큰이 3개 이상이면 왼쪽 자식이 있다
        if len(info) >= 3:
            left[p] = int(info[2])
        # 토큰이 4개면 오른쪽 자식도 있다
        if len(info) == 4:
            right[p] = int(info[3])
 
    # 출력할 문자를 모을 리스트
    result = []
 
    # 중위순회(LVR)
    def inorder(t):
        # t번 노드가 존재하면
        if t:
            # t번노드의 왼쪽 자식(L) 처리
            inorder(left[t])
            # t번 노드(V) 에서 할일 처리
            result.append(ch[t])
            # t번노드의 오른쪽 자식(R) 처리
            inorder(right[t])
 
    # 루트는 항상 1번
    inorder(1)
 
    print(f'#{tc} {"".join(result)}')