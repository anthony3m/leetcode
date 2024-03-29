class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True      
        return False

    # Check whether can find word, start at (i, j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # All the characters are checked
            return True

        if (
            i < 0 
            or i >= len(board) 
            or j < 0 
            or j >= len(board[0]) 
            or word[0] != board[i][j]
        ):
            return False

        tmp = board[i][j] # First character is found, check the remaining part
        board[i][j] = "#" # Avoid visit again 
        # Check whether can find "word" along one direction
        res = (
            self.dfs(board, i + 1, j, word[1:]) 
            or self.dfs(board, i - 1, j, word[1:]) 
            or self.dfs(board, i, j + 1, word[1:]) 
            or self.dfs(board, i, j - 1, word[1:])
        )
        board[i][j] = tmp
        return res