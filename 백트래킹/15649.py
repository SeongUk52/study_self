def bt(n,k,comb,result):
    if len(comb)==k:
        result.append(comb[:])
        return
    for i in range(1,n+1):
        if i not in comb:
            comb.append(i)
            bt(n,k,comb,result)
            comb.pop()

N,M = map(int,input().split())
result = []
bt(N,M,[],result)
for comb in result:
    for i in comb:
        print(i,end=' ')
    print()