#수 정렬하기 3
import sys
N = int(sys.stdin.readline())
L = [0]*10001
for i in range(N):
    a = int(sys.stdin.readline())
    L[a] += 1

for i in range(10001):
    if L[i] != 0:
        for j in range(L[i]):
            print(i)