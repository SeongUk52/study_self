#6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)

x = list(map(int,input().split()))
for i in x:
    if i % 2 ==0:
        print("even")
    else:
        print("odd")