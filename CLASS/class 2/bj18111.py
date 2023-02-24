import math

def main():
    N,M,B = input().split()
    N=int(N)
    M=int(M)
    B = int(B)
    max = 0
    min = 255
    field = [[0]*M]*N
    for i in range(0,N):
        field[i] = list(map(int,input().split()))
        #x = [int(x) for x in input("Enter multiple value: ").split(",")]
        for j in field[i] :
            if(j<min):
                min = j
            if(j>max):
                max = j
    bestCase = max
    testCase = [0]*(max-min+1)
    caseCost = [0]*(max-min+1)
    for x in range(0, max+1-min):
        for i in field:
            for j in i:
                if(j>x+min):
                    testCase[x]+=2*(j-x-min)
                    caseCost[x]+=(j-x-min)
                elif(x+min>j):
                    testCase[x]+=x+min-j
                    caseCost[x]-=x+min-j

    for x in range(0, max+1-min):
        if(B+caseCost[x]<0):
            testCase[x] = math.inf
    
    for x in range(0, max+1-min):
        
        if(testCase[x]<testCase[bestCase-min]):
            bestCase=x+min
    print(testCase[bestCase-min], bestCase)


if __name__ == "__main__":
    main()