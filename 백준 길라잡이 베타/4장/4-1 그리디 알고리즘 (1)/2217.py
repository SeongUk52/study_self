n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)  # 로프 중량을 내림차순으로 정렬
max_weight = 0
for i in range(n):
    weight = ropes[i] * (i + 1)  # i번째로 약한 로프를 포함한 상황에서의 중량 계산
    max_weight = max(max_weight, weight)
print(max_weight)
