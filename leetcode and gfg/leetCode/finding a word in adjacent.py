def main (board , word) :
        def dfs (i,j,x):
            if x >= len(word) : return 1
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) :
                if board[i][j] == word[x] : 
                    temp = board[i][j]
                    board[i][j] = '0'
                    if dfs(i-1,j,x+1) or dfs(i+1,j,x+1) or dfs(i,j-1,x+1) or dfs(i,j+1,x+1) : return 1
                    board[i][j] = temp
                    return 0 
                else : return 0

        if len(word) == 0 : return 1
        for i in range(0,len(board)) : 
            for j in range(0 , len(board[0])) : 
                if board[i][j] == word[0]: 
                    if dfs(i,j,0) : return 1
        
        return 0




board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(main(board,word))





def test_func1() :
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    assert main(board,word) == 1


def test_func2():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    assert main(board,word) == 0

