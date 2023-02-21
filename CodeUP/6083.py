#6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

r,g,b = map(int,input().split())
result = r*g*b
for rr in range(r):
    for gg in range(g):
        for bb in range(b):
            print(rr,gg,bb)
print(result)