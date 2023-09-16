n = int(input())
ll = list(map(int, input().split()))

dp = [0] * n
dp[0] = ll[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + ll[i], ll[i])  # 현재 수열값까지의 연속된 부분 수열의 최대 합 계산

print(max(dp))