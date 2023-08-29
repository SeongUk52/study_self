def soe(n):
    sieve = [True]*n
    sieve[0] = False
    sieve[1] = False
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False
    return sieve
n = int(input())
ll = list(map(int,input().split()))
decL = soe(1001)
cnt = 0
for i in ll:
    if decL[i]:
        cnt+=1
print(cnt)