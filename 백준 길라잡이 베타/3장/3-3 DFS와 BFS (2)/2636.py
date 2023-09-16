from collections import deque
def bfs(map,row,col,q0,result):
    cnt = 0
    if not q0:
        return
    for i in q0:
        result[0] = i[2]
        map[i[0]][i[1]] = 0
    for i in map:
        for j in i:
            if j == 1:
                cnt+=1
    if cnt != 0:
        result[1] = cnt
    q1 = deque()
    while q0:
        now = q0.popleft()

        keyRow = [1,-1,0,0]
        keyCol = [0,0,1,-1]
        for i in range(4):
            newRow = now[0]+keyRow[i]
            newCol = now[1]+keyCol[i]
            if 0<=newRow<row and 0<=newCol<col:
                if map[newRow][newCol] == 1:
                    q1.append([newRow,newCol,now[2]+1])
                elif map[newRow][newCol] == 0:
                    q0.append([newRow,newCol,now[2]])
                    map[newRow][newCol] = 2
    bfs(map,row,col,q1,result)



row, col = map(int,input().split())
map = [list(map(int,input().split())) for i in range(row)]
q0 = deque()
q0.append([0,0,0])
result = [0,0]
bfs(map,row,col,q0,result)
for i in result:
    print(i)