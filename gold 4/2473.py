import sys
def main():
    N = int(input())
    l = [int(i)for i in input().split()]
    smallest = 3000000001
    answer = [0]*3
    l.sort()
    for i in range(N-2):
        if i > 0 and l[i]==l[i-1]:
            continue
        min = i+1
        max = N-1

        while(max > min):
            sum=l[max]+l[i]+l[min]
            if(abs(smallest)>abs(sum)):
                smallest=sum
                answer[2]=l[max]
                answer[1]=l[i]
                answer[0]=l[min]
            if(sum>0):
                max-=1
            elif(sum<0):
                min+=1
            elif(sum==0):
                answer[2]=l[max]
                answer[1]=l[i]
                answer[0]=l[min]
                answer.sort()
                print(answer[0],answer[1],answer[2])
                sys.exit(0)
    answer.sort()
    print(answer[0],answer[1],answer[2])

if __name__=="__main__":
    main()