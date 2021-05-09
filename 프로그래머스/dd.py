def solution(board, moves):
    arr = []
    answer = 0
    for i in moves:
        j = 0
        while(board[j][i-1]>0 and j<len(board)):
            j+=1
        arr.append(board[j][i-1])
        board[j][i-1] = 0
    
    
    while(len(arr)>=2 and arr[-1] == arr[-2]):
        arr.pop()
        arr.pop()
        answer += 1
        
    return answer

if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4,5,5,5]))