from collections import deque

n = int(input())
q=deque()
for i in range(1,n+1):
    q.append(i)
if n == 1:
    print(1)
while(len(q)>1):
    q.popleft()
    if len(q)>1:
        q.append(q.popleft())

    else:
        print(q.popleft())
        break