#6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)

a = int(input())
if a<0:
    if a%2==0:
        print('A')
    else:
        print('B')
else:
    if a%2==0:
        print('C')
    else:
        print('D')