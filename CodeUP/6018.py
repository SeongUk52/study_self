#6018 : [기초-입출력] 시간 입력받아 그대로 출력하기(설명)(py)

h, m = input().split(':')
print(h,m,sep=':')

# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.