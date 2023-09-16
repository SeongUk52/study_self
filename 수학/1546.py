n = int(input())
nums = list(map(int,input().split()))
sum = 0
max = 0
for i in nums:
    if i > max: max=i
for i in nums:
    sum+=100*(i/max)
print(sum/n)