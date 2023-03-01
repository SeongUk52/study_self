#유기농 배추
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline()
T = int(si)

def dfs(M,N,x,y):
    if x>=M or x<0 or y>=N or y<0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(M,N,x-1,y)
        dfs(M,N,x,y-1)
        dfs(M,N,x+1,y)
        dfs(M,N,x,y+1)
        return True
    return False

result = [0] * T
for ttt in range(T):
    M, N, K = map(int,input().split())
    graph = [[0]*M for i in range(N)]
    for _ in range(K):
        a, b = map(int,input().split())
        graph[b][a] = 1
    for i in range(M):
        for j in range(N):
            if dfs(M,N,i,j) == True:
                result[ttt] += 1

for i in result:
    print(i)