import sys
import heapq
def board88(board,q):
    result = 0
    for i in board:
        gap = 1
        temp = ''
        cnt = 0
        for j in i:
            cnt += 1
            if temp == j:
                gap += 1
            if temp !=j or cnt is len(i):
                result += gap // 2
                gap = 1
            temp = j
    heapq.heappush(q,result)
def compareBoard(board,cb,q):
    result = 0
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if cb[i][j]!=board[i][j]:
                result +=1
    heapq.heappush(q,result)
n,m,= map(int,input().split())
board = [[] for i in range(n)]
bwl=['B','W','B','W','B','W','B','W']
wbl=['W','B','W','B','W','B','W','B']
q = []
for i in range(n):
    board[i] = list(input())
bb=[bwl,wbl,bwl,wbl,bwl,wbl,bwl,wbl]
bw=[wbl,bwl,wbl,bwl,wbl,bwl,wbl,bwl]
for i in range(0,n-7):
    for j in range(0,m-7):
        compareBoard([row[j:j+8] for row in board[i:i+8]],bb,q)
        compareBoard([row[j:j+8] for row in board[i:i+8]],bw,q)
#         board88([row[j:j+8] for row in board[i:i+8]],q)
print(heapq.heappop(q))