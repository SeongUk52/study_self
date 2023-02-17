#6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

x = int(input())
if x//3==1:
    print("spring")
elif x//3==2:
    print("summer")
elif x//3==3:
    print("fall")
else:
    print("winter")