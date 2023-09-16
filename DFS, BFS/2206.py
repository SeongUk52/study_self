from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[False] * m for _ in range(n)] for _ in range(2)]  # 3차원 배열로 visited 생성
q = deque()
q.append((0, 0, 1, 0))  # 좌표와 길이와 벽 파괴 여부를 함께 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = -1

while q:
    x, y, length, isBreak = q.popleft()

    if x == n - 1 and y == m - 1:
        result = length
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and not visited[isBreak][nx][ny]:
                visited[isBreak][nx][ny] = True
                q.append((nx, ny, length + 1, isBreak))

            if isBreak == 0 and graph[nx][ny] == 1 and not visited[1][nx][ny]:
                visited[1][nx][ny] = True
                q.append((nx, ny, length + 1, 1))

print(result)
