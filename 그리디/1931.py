#회의실 배정

'''
문제 해결 전략
1. 끝나는 시간이 제일 작은 회의를 먼저 찾는다.
2. 앞서 찾은 회의의 끝나는 시간 보다 크거나 같은 시작시간 중 끝나는 시간이 제일 작은 회의를 찾는다.
'''
cnt = 0 # 회의의 최대 개수 카운트
N = int(input()) # 회의의 개수
t = 0 #현재 시간
dl =[] #회의 리스트
pt = 0
for i in range(N):
    x, y = map(int,input().split())
    dl.append([x,y])
dl.sort()
dl.sort(key=lambda x:x[1])  #y기준 정렬

for i in range(pt,N):
    if t>dl[i][0]:
        continue
    else:
        pt = i
        t = dl[i][1]
        cnt += 1

print(cnt)
