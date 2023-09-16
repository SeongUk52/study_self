n = int(input())
nl = list(map(int,input().split()))
dict = {}   #수 카운팅을 위한 딕셔너리 타입
for i in nl:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
m = int(input())
ml = list(map(int,input().split()))
for i in ml:
    if i in dict:
        print(dict[i], end=' ')
    else:
        print(0,end=' ')