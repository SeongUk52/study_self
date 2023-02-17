#6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)

a, b = map(int, input().split())
print(a+b,'\n',a-b,'\n',a*b,'\n',a//b,'\n',a%b,'\n',format(a/b,".2f"),sep='')

#sep='' 공백제거(단어 사이 간격의 문자(공백)을 재설정함)