#촌수계산
import sys
sys.setrecursionlimit(100000)

def dfs(graph, v, visited, cnt, temp):
    visited[v] = [True]
    cnt[v] = [temp]
    temp += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, cnt, temp)

n = int(sys.stdin.readline())
x,y = map(int,input().split())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = [[0] for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph,y,visited,cnt,0)
if cnt[x][0]==0:
    print(-1)
else:
    print(cnt[x][0])