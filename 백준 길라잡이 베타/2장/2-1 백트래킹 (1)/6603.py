def bt(k,start,comb,result,nums):
    if len(comb) == k:
        result.append(comb[:])
        return
    for i in range(start,len(nums)):
        comb.append(nums[i])
        bt(k,i+1,comb,result,nums)
        comb.pop()

ll=[1]
while ll[0] != 0:
    ll = list(map(int,input().split()))
    result = []
    bt(6,1,[],result,ll)
    for i in result:
        for j in i:
            print(j,end=' ')
        print()
    print()

