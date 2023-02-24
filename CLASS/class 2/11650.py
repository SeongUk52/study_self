#좌표 정렬하기
import sys

N = int(sys.stdin.readline())
LL=[]
for _ in range(N):
    a = list(map(int,input().split()))
    LL.append(a)

LL.sort(key=lambda x:x[1])
LL.sort(key=lambda x:x[0])
for i in LL:
    print(i[0],i[1])
