def getgcd(p, q):
    if(q==0):
        return p
    return getgcd(q, p % q)
    #유클리드 호재법
def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if b<a :
        temp = a
        a = b
        b = temp
    gcd = getgcd(a, b)
    print(gcd)
    print(int(a*b / gcd))

if __name__=="__main__":
    main()