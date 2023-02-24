#신입 사원

T = int(input())
resultList=[]
for _ in range(T):
    N = int(input())
    lower0 = 100000
    lower1 = 100000
    cnt = 0
    applicantList = []
    for i in range(N):
        applicantList.append(list(map(int, input().split())))

    applicantList.sort(key=lambda x: x[0])

    temp = applicantList[0][1]
    for i in applicantList:
        if i[1] <= temp:
            temp = i[1]
            cnt += 1
    resultList.append(cnt)

for i in resultList:
    print(i)


