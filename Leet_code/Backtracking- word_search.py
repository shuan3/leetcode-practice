from typing import List
class Solution:
    def check_around(self,board:List[List[str]],word:str,i:int,j:int,idx:int,visited:List[List[str]]):
        if idx==len(word)-1:
            return True
        visited[i][j]=True
#         print(visited,i,j)
#         print("run")
        if i>0:
#             print(f"why you come to here {i}")
            if not visited[i-1][j] and board[i-1][j]==word[idx+1] and self.check_around(board,word,i-1,j,idx+1,visited):
                return True
#         print("run 1") remember to add rextriction on index before calling them in the same if statement

        if j>0 and not visited[i][j-1] and board[i][j-1]==word[idx+1] and self.check_around(board,word,i,j-1,idx+1,visited):
            return True
#         print("run 2")
        if i<len(board)-1 and not visited[i+1][j] and board[i+1][j]==word[idx+1] and self.check_around(board,word,i+1,j,idx+1,visited):
            return True
#         print("run 3")
        if j<len(board[0])-1 and not visited[i][j+1] and board[i][j+1]==word[idx+1] and self.check_around(board,word,i,j+1,idx+1,visited):
            return True
#         print("run 4")
        visited[i][j]=False
        return False
    def exist(self, board: List[List[str]], word: str):
        visited=[ [False]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
#                 print(i,j)
                if board[i][j]==word[0] and self.check_around(board,word,i,j,0,visited):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
Solution().exist(board,word)







class Solution:
    def check_around(self,board:List[List[str]],word:str,i:int,j:int,idx:int):
        if idx==len(word)-1:
            return True
        x=board[i][j]
        board[i][j]=0
#         print(visited,i,j)
#         print("run")
        if i>0 and board[i-1][j]==word[idx+1] and self.check_around(board,word,i-1,j,idx+1):
            return True
#         print("run 1") remember to add rextriction on index before calling them in the same if statement

        if j>0 and board[i][j-1]==word[idx+1] and self.check_around(board,word,i,j-1,idx+1):
            return True
#         print("run 2")
        if i<len(board)-1 and board[i+1][j]==word[idx+1] and self.check_around(board,word,i+1,j,idx+1):
            return True
#         print("run 3")
        if j<len(board[0])-1 and board[i][j+1]==word[idx+1] and self.check_around(board,word,i,j+1,idx+1):
            return True
#         print("run 4")
        board[i][j]=x
        return False
    def exist(self, board: List[List[str]], word: str):
        for i in range(len(board)):
            for j in range(len(board[0])):
#                 print(i,j)
                if board[i][j]==word[0] and self.check_around(board,word,i,j,0):
                    return True
        return False
    # can use chr or ord




class Solution3:
    def exist(self, board, word):
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False