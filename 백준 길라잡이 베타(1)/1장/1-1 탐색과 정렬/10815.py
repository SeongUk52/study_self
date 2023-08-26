n = int(input())
nl = list(map(int,input().split()))
m = int(input())
ml = list(map(int,input().split()))
max = 10000000
index = [False]*2*max
for i in nl:
    index[i+max] = True
for i in ml:
    if index[i+max]:
        print(1,end=' ')
    else:
        print(0,end=' ')