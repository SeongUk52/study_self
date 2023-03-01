#단지번호붙이기
import sys
si = sys.stdin.readline()
N = int(si)

graph = [list(map(int,input())) for i in range(N)]
houses = [0]
def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        houses[result] += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            houses.append(0)
            result += 1
houses.pop()
houses.sort()
print(result)
for i in range(result):
    print(houses[i])