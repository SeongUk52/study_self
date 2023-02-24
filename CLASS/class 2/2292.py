#벌집

result = 1
cnt = 1

N = int(input())
while N > cnt:
    cnt += 6*result
    result += 1

print(result)
