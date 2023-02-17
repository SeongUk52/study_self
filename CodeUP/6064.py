#6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)

x = list(map(int, input().split()))
x.sort()
print(x[0])