# DFS와 BFS
# 방문할 수 있는 정점이 여러개면 작은거부터 방문해야함!!!!!!!
from collections import deque
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
visited = [False] * (N + 1)
graph = [[]]
for _ in range(N):
    graph.append([])
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)