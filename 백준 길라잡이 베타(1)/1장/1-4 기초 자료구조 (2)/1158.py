from collections import deque
n,k = map(int,input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)
print('<',end='')
while q:
    if len(q) == 1:
        print(q.popleft(),end='')
        break
    for i in range(k-1):
        q.append(q.popleft())
    print(q.popleft(),end=', ')
print('>')
