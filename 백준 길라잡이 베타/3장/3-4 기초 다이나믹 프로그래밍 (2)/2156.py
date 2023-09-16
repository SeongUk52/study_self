def dpm(wines,n):
    dp = [0] * (n+1)
    dp[1] = wines[0]
    if n == 1:
        return wines[0]
    dp[2] = wines[1] + dp[1]
    if n == 2:
        return dp[2]
    for i in range(3,n+1):
        dp[i] = max(dp[i-1],dp[i-2]+wines[i-1],dp[i-3]+wines[i-2]+wines[i-1])
    return dp[-1]

n = int(input())
wines = []
for i in range(n):
    wines.append(int(input()))
print(dpm(wines,n))