class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])

        seen=[[False]*cols for _ in range(rows)]
        res=0

        for y in range(rows):
            for x in range(cols):
                if seen[y][x] or grid[y][x]=='0': continue
                res+=1
                seen[y][x]=True
                q=deque([(y,x)])
                while q:
                    yy,xx=q.popleft()
                    for dy,dx in ((-1,0),(1,0),(0,-1),(0,1)):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<rows and 0<=nx<cols and not seen[ny][nx] and grid[ny][nx]=='1':
                            seen[ny][nx]=True
                            q.append((ny,nx))
        return res

