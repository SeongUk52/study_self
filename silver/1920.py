N = input()
A = list(map(int, input().split()))
M = input()
B = list(map(int, input().split()))
for i in B:
    for j in A:
        C = 0
        if j == i:
            C = 1
            print("1")
            break
    if C == 0:
        print("0")

        