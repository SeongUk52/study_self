#6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)

a, b = map(int, input().split())
print(a if (a>=b) else b)





'''

참고
3개의 요소로 이루어지는 3항 연산은
"x if C else y" 의 형태로 작성이 된다.
- C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
- x : C의 평가 결과가 True 일 때 사용할 값
- y : C의 평가 결과가 True 가 아닐 때 사용할 값

조건식 또는 값이 True 이면 x 값이 사용되고, True가 아니면 y 값이 사용되도록 하는 코드이다.

'''