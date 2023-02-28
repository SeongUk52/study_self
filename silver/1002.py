#터렛
import sys

TC = int(sys.stdin.readline())
LL = []
for _ in range(TC):
    x1, y1, r1, x2, y2, r2=map(int, input().split())
    distance = (((x1-x2)**2)+((y1-y2)**2))**0.5
    LL.append([r1,r2,distance])
for i in LL:
    if i[2] == 0 and i[0] == i[1]:
        print('-1')
    elif i[2] < i[0] or i[2] < i[1]:
        if i[0]>i[1]+i[2] or i[1]>i[0]+i[2]:
            print('0')
        elif i[0] == (i[1] + i[2]) or i[1] == (i[0] + i[2]):
            print('1')
        else:
            print('2')
    else:
        if i[2] < i[0]+i[1]:
            print('2')
        elif i[2] == i[0] + i[1]:
            print('1')
        else:
            print('0')