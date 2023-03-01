#적록색약
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline()

N =int(si)
graph1 = [list(input()) for i in range(N)]
graph2 = [arr[:] for arr in graph1]

def dfsR(x,y,graph):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if graph[y][x] == 'R':
        graph[y][x] = 0
        dfsR(x-1,y,graph)
        dfsR(x,y-1,graph)
        dfsR(x+1,y,graph)
        dfsR(x,y+1,graph)
        return True
    return False
def dfsG(x,y,graph):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if graph[y][x] == 'G':
        graph[y][x] = 0
        dfsG(x-1,y,graph)
        dfsG(x,y-1,graph)
        dfsG(x+1,y,graph)
        dfsG(x,y+1,graph)
        return True
    return False
def dfsB(x,y,graph):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if graph[y][x] == 'B':
        graph[y][x] = 0
        dfsB(x-1,y,graph)
        dfsB(x,y-1,graph)
        dfsB(x+1,y,graph)
        dfsB(x,y+1,graph)
        return True
    return False
result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if dfsR(i,j,graph1)==True:
            result1 +=1
        if dfsG(i,j,graph1)==True:
            result1 +=1
        if dfsB(i,j,graph1)==True:
            result1 +=1

for i in range(N):
    for j in range(N):
        if graph2[j][i] == 'G':
            graph2[j][i] = 'R'
for i in range(N):
    for j in range(N):
        if dfsR(i,j,graph2)==True:
            result2 +=1
        if dfsB(i,j,graph2)==True:
            result2 +=1

print(result1)
print(result2)