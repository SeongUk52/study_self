#바이러스
def dfs(graph, v, visited, cnt):
    visited[v] = True
    cnt[0] += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, cnt)

N = int(input())
M = int(input())
graph = [[]]
for _ in range(N):
    graph.append([])
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
cnt = [0]
dfs(graph, 1, visited, cnt)
print(cnt[0]-1)
