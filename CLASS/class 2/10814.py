#나이순 정렬
import sys

N = int(sys.stdin.readline())
L = []
for _ in range(N):
    a, b = input().split()
    a = int(a)
    L.append([a,b])

L.sort(key=lambda x:x[0])
for i in L:
    print(i[0],i[1])