def bt (n,comb,result):
    if sum(comb) >n:
        return
    if sum(comb) == n:
        result[0] += 1
        return
    for i in range(1,4):
        comb.append(i)
        bt(n,comb,result)
        comb.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    result = [0]
    bt(n,[],result)
    print(result[0])