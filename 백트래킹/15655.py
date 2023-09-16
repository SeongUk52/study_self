def bt(nums,k,start,comb,result):
    if len(comb)==k:
        result.append(comb[:])
        return
    for i in range(start,len(nums)):
        if nums[i] not in comb:
            comb.append(nums[i])
            bt(nums,k,i+1,comb,result)
            comb.pop()
N,M=map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []
bt(nums,M,0,[],result)
for comb in result:
    for i in comb:
        print(i,end=' ')
    print()