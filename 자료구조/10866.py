import sys
from collections import deque
q = deque()
n = int(input())
for _ in range(n):
    commands = sys.stdin.readline().split()
    if commands[0] == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif commands[0] == "pop_back":
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif commands[0] == 'size':
        print(len(q))
    elif commands[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif commands[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif commands[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif commands[0] == 'push_front':
        q.appendleft(int(commands[1]))
    elif commands[0] == 'push_back':
        q.append(int(commands[1]))