n, k = map(int,input().split())
q = [i for i in range(1,n+1)]
print('<',end='')
while q:
    for _ in range(k-1):
        q.append(q.pop(0))
    print(q.pop(0),end='')
    if q:
        print(',',end=' ')
    else:
        print('>')