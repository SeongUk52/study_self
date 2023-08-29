def bt(nums,s,comb,result,start):
    if s == sum(comb) and len(comb)>0:
        result[0] += 1
    for i in range(start,len(nums)):
        comb.append(nums[i])
        bt(nums,s,comb,result,i+1)
        comb.pop()

n,s = map(int,input().split())
ll = list(map(int,input().split()))
result = [0]
bt(ll,s,[],result,0)
print(result[0])