n = int(input())
card_prices = [0] + list(map(int, input().split()))

# dp[i]는 i개의 카드를 살 때 얻을 수 있는 최대 가치를 나타냄
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + card_prices[j])

print(dp[n])
