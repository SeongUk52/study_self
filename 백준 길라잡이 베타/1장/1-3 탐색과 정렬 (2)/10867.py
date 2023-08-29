n=int(input())
ll = list(map(int,input().split()))
maxV = 1000
index = [False]*(2*maxV+1)
for i in ll:
    index[i+maxV] = True
cnt = -maxV-1
for i in index:
    cnt+=1
    if i:
        print(cnt,end=' ')