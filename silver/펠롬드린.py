x = input()
while(x != '0'):
    t = 0
    for i in range(len(x)//2):
        if(x[i]!=x[len(x)-i-1]):
            print("no")
            t = 1
            break
    if t == 0:
        print("yes")

    x = input()

