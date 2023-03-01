#섬의 개수
import sys
sys.setrecursionlimit(100000)
w,h = map(int,input().split())
result = []
def dfs(x,y,w,h):
    if x<0 or x>=w or y<0 or y>=h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y,w,h)
        dfs(x-1,y-1,w,h)
        dfs(x-1,y+1,w,h)
        dfs(x,y-1,w,h)
        dfs(x,y+1,w,h)
        dfs(x+1,y,w,h)
        dfs(x+1,y-1,w,h)
        dfs(x+1,y+1,w,h)
        return True
    return False

while w!=0 and h!=0:
    graph=[list(map(int,input().split())) for i in range(h)]
    temp = 0
    for i in range(w):
        for j in range(h):
            if dfs(i,j,w,h)==True:
                temp += 1

    result.append(temp)
    w, h = map(int, input().split())

for i in result:
    print(i)