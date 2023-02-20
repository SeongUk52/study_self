#6077 : [기초-종합] 짝수 합 구하기(설명)(py)

s=0
for i in range(1,int(input())+1):
    if i%2==0:
        s+=i

print(s)