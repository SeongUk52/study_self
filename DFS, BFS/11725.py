#트리의 부모 찾기
import sys

sys.setrecursionlimit(100000)
def dfs(graph, v, visited,before):
    parents[v] = before
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited,v)

N = int(input())
visited = [False]*(N+1)
graph = [[] for i in range(N+1)]
parents = [0] * (N+1)


for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph,1,visited,0)

for i in parents:
    if i>0:
        print(i)