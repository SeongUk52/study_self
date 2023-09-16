def bt(n,k,start,comb,result,nums):
    if len(comb)==k:
        result.append(comb[:])
        return

    for i in range(start,n):
        comb.append(nums[i])
        bt(n,k,i,comb,result,nums)
        comb.pop()
def btcomb(n,k,nums):
    result = []
    bt(n,k,0,[],result,nums)
    return result

N,M = map(int,input().split())
nums = list(set(map(int,input().split())))
nums.sort()
combs  = btcomb(len(nums),M,nums)
for comb in combs:
    for i in comb:
        print(i, end=' ')
    print()