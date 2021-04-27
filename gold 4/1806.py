def main():
    N, S = input().split()
    N = int(N)
    S = int(S)
    num = [] * N
    minLen = 0
    num = [int(i) for i in input().split()]
    for i in range(N):
        j=i
        sum = 0
        while(sum<S):
            sum += num[j]
            j += 1
            if(j>=N):
                break
        if(sum>=S):
            if(minLen>j-i or minLen==0):
                minLen=j-i

    print(minLen)

if __name__=="__main__":
    main()