def rec(N, r, c):
    if N == 0:
        return 0

    if r < (2 ** (N - 1)):
        if c < (2 ** (N - 1)):
            return rec(N - 1, r, c)
        else:
            return (2 ** (2*(N-1))) + rec(N - 1, r, c-(2 ** (N - 1)))
    else:
        if c < (2 ** (N - 1)):
            return (2 * (2 ** (2*(N-1)))) + rec(N - 1, r-(2 ** (N - 1)), c)
        else:
            return (3 * (2 ** (2*(N-1)))) + rec(N - 1, r-(2 ** (N - 1)), c-(2 ** (N - 1)))


N,r,c=map(int,input().split())
print(rec(N,r,c))


