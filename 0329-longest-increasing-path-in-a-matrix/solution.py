class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n,m=len(matrix),len(matrix[0])
        seen=[[0]*m for _ in range(n)]

        res=0
        for y in range(n):
            for x in range(m):
                if seen[y][x]==0:
                    res = max(res,self.dfs(matrix,seen,y,x))

        return res

    def dfs(self, matrix, seen,y,x):
        if seen[y][x]>0: return seen[y][x]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        n,m=len(matrix),len(matrix[0])

        res=1
        for j,i in dirs:
            X=x+i
            Y=y+j
            if X<0 or Y<0 or X>=m or Y>=n:
                continue
            if matrix[Y][X]>matrix[y][x]:
                res=max(res,self.dfs(matrix,seen,Y,X)+1)

        seen[y][x] = res
        return res



