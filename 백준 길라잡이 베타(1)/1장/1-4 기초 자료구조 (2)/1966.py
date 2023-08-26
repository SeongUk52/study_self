from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    ll = list(map(int,input().split()))
    q = deque()
    cnt = 0
    for i in ll:
        q.append(i)
    while q:
        if q[0]<max(q):
            q.append(q.popleft())
            m -= 1
            if m<0:
                m += len(q)
        else:
            q.popleft()
            m -= 1
            cnt += 1
            if m<0:
                print(cnt)
                break