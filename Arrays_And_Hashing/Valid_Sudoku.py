import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #only filled in cells need to be validated
        """Rules:
            1. Each row and 2. col 1-9 with no repition
            3. each 3 X 3 sub box is 1-9 no repetition
        """
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3, c/3) (note: (0,0) represents top left box. (0,1) is first box row  second box col) (col 4 is in box 2)
        #Three hashsets= O(9^2)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue  
                #check duplicates
                if(board[r][c] in rows[r] or #1 
                   board[r][c] in cols[c] or #2
                   board[r][c] in squares[(r//3, c//3)]): #3 sub-box
                   return False   
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])     
                
        return True