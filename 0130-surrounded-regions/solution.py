class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h,w=len(board),len(board[0])
        
        def dfs(y,x):
            if y<0 or x<0 or y>=h or x>=w:
                return
                
            if board[y][x]=="X" or board[y][x]=="#":
                return

            board[y][x]="#"
            dfs(y-1,x)
            dfs(y+1,x)
            dfs(y,x-1)
            dfs(y,x+1)
            

        for y in range(h):
            dfs(y,0)
            dfs(y,w-1)
        for x in range(w):
            dfs(0,x)
            dfs(h-1,x) 
        
        for y in range(h):
            for x in range(w):
                if board[y][x]=="O":
                    board[y][x]="X"

                if board[y][x]=="#":
                    board[y][x]="O"
        
                    
