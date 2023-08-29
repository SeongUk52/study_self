def soe(m, n):
    n+=1
    sieve = [True] * (n)
    sieve[0] = sieve[1] = False
    mm = int(n ** 0.5)
    for i in range(2, mm + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(m,n) if sieve[i]]

m, n = map(int, input().split())
ll = soe(m, n)
for i in ll:
    print(i)