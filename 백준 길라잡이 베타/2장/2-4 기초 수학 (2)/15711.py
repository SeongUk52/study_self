import sys

maxi = int(2*10**12)
deci = [True] * (maxi+1)
m = int(maxi**0.5)
deci[0],deci[1]=False,False
for i in range(2,m+1):
    if deci[i]:
        for j in range(i+i,maxi+1,i):
            deci[j] = False

def couple(n,deci):
    if deci[2] and deci[n-2]:
        return 'YES'
    for i in range(3,n//2+1,2):
        if deci[i] and deci[n-i]:
            return 'YES'
    return 'NO'
t = int(input())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    print(couple(a+b,deci))