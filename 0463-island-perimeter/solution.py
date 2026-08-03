class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        s=[]
        m,n=len(grid),len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x]==1:
                    grid[y][x]=-1
                    s.append((y,x))
                    break
            if s:break
        
        res=0
        def valid(y,x):
            nonlocal res
            if y>=0 and x>=0 and y<m and x<n:
                if grid[y][x]==1:
                    grid[y][x]=-1
                    return True
                if grid[y][x]==0:
                    res+=1
                    return False
                return False
            else:
                res+=1
                return False

        dirs= [(1,0),(0,1), (-1,0), (0,-1)]

        while s:
            y,x=s.pop()

            for yy,xx in dirs:
                if valid(y+yy,x+xx):
                    s.append((y+yy,x+xx))

        return res

