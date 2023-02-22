#잃어버린 괄호

N = input()
cnt = 0
numM = N.split('-')
sumN = 0
for i in numM:
    temp = list(map(int,i.split('+')))

    if cnt == 0:
        for j in temp:
            sumN += j
            cnt = 1
    elif cnt == 1:
        for j in temp:
            sumN -= j

print(sumN)

'''
-로 구분하여 한번 나누고 +로 구분하여 두번째로 나눔
첫번째 나눔 중 처음항복을 제외하고 모두 빼면 정답이 나옴
'''