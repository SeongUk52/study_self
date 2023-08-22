def bt(n,k,start,comb,result):
    if(len(comb)==k):
        result.append(comb[:])
        return

    for i in range(start,n+1):
        comb.append(i)
        bt(n,k,i+1,comb,result)
        comb.pop()

def btcomb(n,k):
    result = []
    bt(n,k,1,[],result)
    return result

N,K = map(int,input().split())
combs = btcomb(N,K)
for comb in combs:
    for i in comb:
        print(i,end=' ')
    print()