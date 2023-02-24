#달팽이는 올라가고 싶다

A, B, V = map(int,input().split())
n = ((V-B)/(A-B))
if n%1!=0:
    n = int(n) + 1
else:
    n = int(n)
print(n)