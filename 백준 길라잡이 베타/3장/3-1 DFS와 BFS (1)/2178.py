from collections import deque


def bfs(graph, n, m):
    keyRow = [1, -1, 0, 0]
    keyCol = [0, 0, 1, -1]
    q = deque()
    q.append((0, 0, 1))  # 시작 위치와 거리 함께 저장
    graph[0][0] = 0  # 시작 위치 방문 처리

    while q:
        now = q.popleft()
        row, col, distance = now
        if row == n - 1 and col == m - 1:
            return distance
        for d in range(4):
            newRow, newCol = row + keyRow[d], col + keyCol[d]
            if 0 <= newRow < n and 0 <= newCol < m and graph[newRow][newCol] == 1:
                q.append((newRow, newCol, distance + 1))
                graph[newRow][newCol] = 0  # 방문한 위치 처리

    return -1  # 경로가 없는 경우


n, m = map(int, input().split())
mapA = [list(map(int, input())) for _ in range(n)]
shortest_distance = bfs(mapA, n, m)
print(shortest_distance)
