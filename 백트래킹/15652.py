def bt(n,k,start,comb,result):
    if(len(comb)==k):
        result.append(comb[:])
        return

    for i in range(start,n+1):
        comb.append(i)
        bt(n,k,i,comb,result)
        comb.pop()

def btcomb(n,k):
    result = []
    bt(n,k,1,[],result)
    return result

N,M = map(int,input().split())

combs = btcomb(N,M)

for comb in combs:
    for i in comb:
        print(i,end=' ')
    print()