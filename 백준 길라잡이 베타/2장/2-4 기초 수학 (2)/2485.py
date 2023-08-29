import math
from functools import reduce

# 리스트 내의 숫자들의 최대 공약수를 계산하는 함수
def list_gcd(numbers):
    return reduce(math.gcd, numbers)

n = int(input())
ll = []
gap = []
temp = None
result = 0
for _ in range(n):
    ll.append(int(input()))
    if not temp:
        temp = ll[-1]
    else:
        gap.append(ll[-1]-temp)
        temp = ll[-1]
result = ((ll[-1]-ll[0])//list_gcd(gap))-len(ll)+1
print(result)