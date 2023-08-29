import sys


def soe(mini, maxi):
    sieve = [True] * (maxi + 1 - mini)
    m = int(maxi ** 0.5)
    for i in range(2, m + 1):
        square = i ** 2
        for j in range(- (mini % square), maxi + 1 - mini, square):
            if j >= 0:
                sieve[j] = False
    return sieve


mini, maxi = map(int, sys.stdin.readline().split())
deci = soe(mini, maxi)
cnt = 0
for i in range(maxi + 1 - mini):
    if deci[i]:
        cnt += 1
print(cnt)
