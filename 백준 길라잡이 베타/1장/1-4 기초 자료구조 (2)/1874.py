
n = int(input())
ll = []
stack = []
cnt = 1
result = []
no = None
for _ in range(n):
    ll.append(int(input()))
for i in ll:
    if no == 'NO':
        break
    if not stack:
        stack.append(cnt)
        cnt+=1
        result.append('+')
    while i != stack[-1]:
        stack.append(cnt)
        cnt+=1
        result.append('+')
        if cnt>n+1:
            no = 'NO'
            break
    if i == stack[-1]:
        stack.pop()
        result.append('-')
if no == 'NO':
    print('NO')
else:
    for i in result:
        print(i)

