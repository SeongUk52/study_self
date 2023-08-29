import sys

deci = [True]*(1000000+1)
deci[0] = deci[1] = False
m = int(1000000**0.5)
for i in range(2,m+1):
    if deci[i]:
        for j in range(i+i,1000000+1,i):
            deci[j] = False
def gbh(n,deci):
    for i in range(3,n//2+1,2):
        if deci[i] and deci[n-i]:
            return [i,n-i]
    return None
n = int(sys.stdin.readline())
while(n != 0):
    result = gbh(n,deci)
    if result:
        print(f'{n} = {result[0]} + {result[1]}')
    else:
        print("Goldbach's conjecture is wrong.")
    n = int(sys.stdin.readline())