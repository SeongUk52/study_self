def bt(n,k,visited,comb,result,nums):
    if len(comb)==k:
        result.append(comb[:])
        return
    for i in range(0,n):
        if(not visited[i]):
            comb.append(nums[i])
            visited[i]=True
            bt(n,k,visited,comb,result,nums)
            comb.pop()
            visited[i]=False

def btcomb(n,k,nums):
    result = []
    bt(n,k,[False]*n,[],result,nums)
    return result

N,M=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
combs=btcomb(N,M,numbers)
for comb in combs:
    for i in comb:
        print(i,end=' ')
    print()
