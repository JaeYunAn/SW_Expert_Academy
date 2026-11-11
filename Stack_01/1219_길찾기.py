def dfs(node):
    if node == 99:
        return True
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            if dfs(nxt):
                return True
    return False


for T in range(10):
    tc, cnt = map(int, input().split())
    graph = [[] for _ in range(100)]
    visited = [False] * 100

    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i + 1])

    print(f"#{tc} {1 if dfs(0) else 0}")