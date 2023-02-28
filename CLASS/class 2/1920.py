#수 찾기
import sys
def binary_search(array,target,start,end):
    if start > end:
        return -1
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array,target,mid+1,end)
    else:
        return binary_search(array,target,start,mid-1)


N=int(sys.stdin.readline())
A=list(map(int,input().split()))
M=int(sys.stdin.readline())
B=list(map(int,input().split()))
A.sort()
for i in B:
    result = binary_search(A,i,0,N-1)
    if result == -1:
        print(0)
    else:
        print(1)