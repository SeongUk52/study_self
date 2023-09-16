def btb(k,ll,comb,result):
    if result:
        return
    if len(comb) == k+1:
        for i in range(k):
            if ll[i]=='<':
                if comb[i] > comb[i+1]:
                    return
            else:
                if comb[i] < comb[i+1]:
                    return
        result.append(comb[:])
        return
    for i in range(9,8-k,-1):
        if i not in comb:
            comb.append(i)
            btb(k,ll,comb,result)
            comb.pop()
def bts(k,ll,comb,result):
    if result:
        return
    if len(comb) == k+1:
        for i in range(k):
            if ll[i]=='<':
                if comb[i] > comb[i+1]:
                    return
            else:
                if comb[i] < comb[i+1]:
                    return
        result.append(comb[:])
        return
    for i in range(k+1):
        if i not in comb:
            comb.append(i)
            bts(k,ll,comb,result)
            comb.pop()

k = int(input())
ll = list(input().split())
resultB = []
resultS = []
btb(k,ll,[],resultB)
bts(k,ll,[],resultS)
for i in resultB[0]:
    print(i,end='')
print()
for i in resultS[0]:
    print(i,end='')