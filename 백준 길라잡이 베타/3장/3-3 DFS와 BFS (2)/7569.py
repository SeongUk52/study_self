from collections import deque

def bfs (map,n,m,h):
    q = deque()
    cnt = 0
    for x in range(h):
        for i in range(n):
            for j in range(m):
                if map[x][i][j] == 1:
                    q.append([i,j,0,x])
    while q:
        now = q.popleft()
        if now[2] > cnt:
            cnt = now[2]
        keyRow = [1,-1,0,0,0,0]
        keyCol = [0,0,1,-1,0,0]
        keyHei = [0,0,0,0,1,-1]
        for i in range(6):
            newRow = now[0]+keyRow[i]
            newCol = now[1]+keyCol[i]
            newHei = now[3]+keyHei[i]
            if 0 <= newRow < n and 0 <= newCol <m and 0 <= newHei < h and map[newHei][newRow][newCol] == 0 :
                q.append([newRow,newCol,now[2]+1,newHei])
                map[newHei][newRow][newCol] = 1
    for i in map:
        for j in i:
            for k in j:
                if k == 0:
                    cnt = -1
    print(cnt)

m,n,h = map(int,input().split())
map = [[list(map(int,input().split())) for i in range(n)] for j in range(h)]
bfs(map,n,m,h)
