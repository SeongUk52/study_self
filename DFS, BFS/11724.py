#연결 요소의 개수
def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

N, M = map(int,input().split())
visited = [False] * (N+1)
graph =[[] for i in range(N+1)]
result = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    if not visited[i]:
        dfs(graph,i,visited)
        result += 1

print(result)
