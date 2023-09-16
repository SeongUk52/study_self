from collections import deque
# def bfs(node,end):
#     visited = deque([node])
#     q = deque([node,1])
#     while q:
#         v = q.popleft()
#         ct = q.popleft()
#         if(v==end):
#             return ct
#         ct += 1
#         if v*2 <= end:
#             if (visited.count(v*2)==0):
#                 q.append(v*2)
#                 q.append(ct)
#                 visited.append(v*2)
#         if v * 10 + 1 <= end:
#             if (visited.count(v * 10 + 1)==0):
#                 q.append(v * 10 + 1)
#                 q.append(ct)
#                 visited.append(v * 10 + 1)
# result = bfs(A,B)
# print(result if result is not None else '-1')

A,B = map(int,input().split())
cnt = 1
while B!=A:
    cnt += 1
    tmp = B
    if B%10==1:
        B//=10
    elif B%2==0:
        B//=2
    if tmp==B:
        cnt = -1
        break
print(cnt)