import sys
if __name__=="__main__":
    N = int(sys.stdin.readline())
    B = [int(i)for i in input().split()]
    M = int(sys.stdin.readline())
    for i in range(M):
        S , E = input().split()
        S = int(S)-1
        E = int(E)-1
        state = 1
        z=0
        for j in range(S,E//2):
            if S == E//2:
                break
            if B[j] != B[E-z]:
                state = 0
                break
            z += 1
        print(state)
