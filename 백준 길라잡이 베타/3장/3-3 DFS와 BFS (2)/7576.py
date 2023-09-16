from collections import deque

def bfs (map,n,m):
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == 1:
                q.append([i,j,0])
    while q:
        now = q.popleft()
        if now[2] > cnt:
            cnt = now[2]
        keyRow = [1,-1,0,0]
        keyCol = [0,0,1,-1]
        for i in range(4):
            newRow = now[0]+keyRow[i]
            newCol = now[1]+keyCol[i]
            if 0 <= newRow < n and 0 <= newCol <m and map[newRow][newCol] == 0 :
                q.append([newRow,newCol,now[2]+1])
                map[newRow][newCol] = 1
    for i in map:
        for j in i:
            if j == 0:
                cnt = -1
    print(cnt)

m,n = map(int,input().split())
map = [list(map(int,input().split())) for i in range(n)]
bfs(map,n,m)
