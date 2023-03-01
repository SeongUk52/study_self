#숨바꼭질
from collections import deque

def bfs(v):
    que = deque()
    que.append(v)
    dist[v] = 0
    def move(y,d):
        if y < 0 or y > 100000 or dist[y] != -1:
            return
        dist[y] = d
        que.append(y)
    while que:
        x = que.popleft()
        move(x - 1, dist[x] + 1)
        move(x + 1, dist[x] + 1)
        move(x * 2, dist[x] + 1)

N, K = map(int, input().split())
dist = [-1] * 100001
bfs(N)
print(dist[K])