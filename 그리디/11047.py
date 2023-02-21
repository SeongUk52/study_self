#동전 0

N,K = map(int, input().split())
L = []
cnt=0
now=K
i=N-1
for i in range(N):
    L.append(int(input()))

while now >0:
    cnt+=now//L[i]
    now=now%L[i]
    i-=1

print(cnt)