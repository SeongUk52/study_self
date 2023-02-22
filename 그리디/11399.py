#ATM

N = int(input())
P = list(map(int,input().split()))
P.sort()

sum=0
cnt=0
for i in P:
    cnt+=i
    sum+=cnt

print(sum)
