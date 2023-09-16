import sys

def bt(n, k, visited, comb, result, nums):
    if len(comb) == k:
        result.append(comb[:])
        return

    for i in range(n):
        if not visited[i]:
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:  # 중복 처리
                continue
            visited[i] = True
            comb.append(nums[i])
            bt(n, k, visited, comb, result, nums)
            comb.pop()
            visited[i] = False

def btcomb(n, k, nums):
    result = []
    bt(n, k, [False] * n, [], result, nums)
    return result

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
combs = btcomb(N, M, nums)
for comb in combs:
    for num in comb:
        print(num, end=' ')
    print()
