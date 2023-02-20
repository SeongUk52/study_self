#6079 : [기초-종합] 언제까지 더해야 할까?(py)

cnt = 0
a = int(input())
while 1:
    s = 0
    cnt += 1
    for i in range(cnt+1):
        s += i
    if s>=a:
        break
print(cnt)