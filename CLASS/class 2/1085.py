#직사각형에서 탈출

x, y, w, h = map(int,input().split())

ll = []
ll.append(x)
ll.append(y)
ll.append(w-x)
ll.append(h-y)

ll.sort()
print(ll[0])