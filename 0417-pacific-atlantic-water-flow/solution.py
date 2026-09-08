class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        h,w=len(heights),len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(y,x,visited):
            visited[y][x]=True
            
            for i,j in dirs:
                if y+i<0 or x+j<0 or y+i>=h or x+j>=w:
                    continue
                if visited[y+i][x+j]:
                    continue
                if heights[y][x]>heights[y+i][x+j]:
                    continue
                dfs(y+i,x+j,visited)

        pacific=[[False]*w for _ in range(h)]
        atlantic=[[False]*w for _ in range(h)]

        for i in range(h): dfs(i,0,pacific)
        for i in range(w): dfs(0,i,pacific)

        for i in range(h): dfs(i,w-1,atlantic)
        for i in range(w): dfs(h-1,i,atlantic)

        res=[]
        for y in range(h):
            for x in range(w):
                if pacific[y][x] and atlantic[y][x]:
                    res.append([y,x])
        return res



