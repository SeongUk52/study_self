from collections import deque
def bfs(goal,node, visited):
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()

        print(v, end=' ')
        if v*2<=goal:
            if not (visited[v*2]):
                queue.append(v*2)
                visited[v*2] = True
        if v*10+1<=goal:
            if not (visited[v*10+1]):
                queue.append(v*10+1)
                visited[v*10+1] = True

A,B = map(int,input().split())

visited = [False]*(B+1)
bfs(B,A,visited)
