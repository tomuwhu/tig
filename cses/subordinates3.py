def dfs(graph, start=0):
    n = len(graph)
    dp = [0] * n
    visited, finished = [False] * n, [False] * n
    stack = [start]
    while stack:
        start = stack[-1]
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()
            dp[start] += 1
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]
            finished[start] = True
    return dp
n = int(input())
tree = [[] for _ in range(n)]
for v, p in enumerate(map(int, input().split())):
    tree[p - 1].append(v + 1)
print(*(d - 1 for d in dfs(tree)))