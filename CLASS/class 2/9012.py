def main():
    for i in range(0,int(input())):
        vps = 0
        ck = 0
        ps = input()
        for j in ps:
            if (j == '('):
                vps += 1
            elif(j == ')'):
                vps -= 1

            if (vps<0):
                print("NO")
                ck = 1
                break

        if(ck==0 and vps!=0):
            print("NO")
        elif(vps==0):
            print("YES")
            
if __name__=="__main__":
    main()