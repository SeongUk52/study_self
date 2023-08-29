def bt(start,n,combs,combl,results,resultl):
    if len(combs)==n//2:
        results.append(combs[:])
        for i in range(n):
            if i not in combs:
                combl.append(i)
        resultl.append(combl[:])
        while combl:
            combl.pop()
        return
    for i in range(start,n):
        if i not in combs:
            combs.append(i)
            bt(i+1,n,combs,combl,results,resultl)
            combs.pop()

def min(graph,combs,combl,n):
    sum = float('infinity')
    for i in range(len(combs)):
        t1 = 0
        t2 = 0
        for j in range(0,n//2):
            for k in range(0,n//2):
                if j != k:
                    t1+=graph[combs[i][j]][combs[i][k]]
                    t2+=graph[combl[i][j]][combl[i][k]]
        if sum > abs(t1-t2):
            sum = abs(t1-t2)
    return sum
n = int(input())
s = [list(map(int,input().split())) for i in range(n)]
results=[]
resultl=[]
bt(0,n,[],[],results,resultl)
print(min(s,results,resultl,n))