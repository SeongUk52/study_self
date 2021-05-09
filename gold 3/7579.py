#https://www.acmicpc.net/problem/7579
#배낭문제
def main():
    global N,M,m,c
    N, M = input().split()
    N = int(N)
    M = int(M)
    m = [int(i) for i in input().split()]   #메모리
    c = [int(i) for i in input().split()]   #비활성화 비용
    maxc=sum(c)+1   #비활성화 최대비용
    dp=[-1]*maxc
    dp[0]=0
    for i in range(N):
        for j in range(maxc-c[i]-1,-1,-1):
            if dp[j]!=-1:
                dp[j+c[i]]=max(dp[j+c[i]],dp[j]+m[i])

    for i in dp:
        if i>=M:
            print(dp.index(i))
            break



if __name__ == "__main__":
    main()