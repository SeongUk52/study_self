def tPointer(ll,n):
    s,e = 0,0
    sum = ll[0]
    result = 0
    while s < len(ll) and e < len(ll):
        if sum < n:
            e += 1
            if e>=len(ll):
                break
            sum += ll[e]
        elif sum > n:
            sum -= ll[s]
            s += 1
            if s>=len(ll):
                break
        elif sum == n:
            result += 1
            e += 1
            if e>=len(ll):
                break
            sum += ll[e]
    print(result)

def deci(n):
    ll = []
    dec = [True]*(n+1)
    if n <2 :
        return []
    dec[0],dec[1] = False,False
    for i in range(2,n+1):
        if dec[i]:
            ll.append(i)
            for j in range(i+i,n+1,i):
                dec[j] = False
    return ll

n = int(input())
if n == 1:
    print(0)
else:
    ll = deci(n)
    tPointer(ll,n)