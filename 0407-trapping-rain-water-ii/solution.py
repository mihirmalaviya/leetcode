class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        n,m=len(heightMap),len(heightMap[0])
        seen = [[False]*m for _ in range(n)] 
        res=0
        heap=[]
        def cell(y,x,H=0):
            h=heightMap[y][x]
            if h<H: 
                h=H
            return (h,y,x)
        def valid(y,x):
            return y>=0 and x>=0 and y<n and x<m and not seen[y][x]

        for x in range(m):
            heappush(heap, cell(0,x))
            heappush(heap, cell(n-1,x))
            seen[0][x]=True
            seen[n-1][x]=True
        for y in range(1,n-1):
            heappush(heap, cell(y,0))
            heappush(heap, cell(y,m-1))
            seen[y][0]=True
            seen[y][m-1]=True
        
        # print(heap)

        while heap:
            h,y,x = heappop(heap)
            # if seen[y][x]: continue
            res+=h-heightMap[y][x]
            # print(res)
            if valid(y,x-1):
                heappush(heap,cell(y,x-1,h))
                seen[y][x-1]=True
            if valid(y,x+1):
                heappush(heap,cell(y,x+1,h))
                seen[y][x+1]=True
            if valid(y-1,x):
                heappush(heap,cell(y-1,x,h))
                seen[y-1][x]=True
            if valid(y+1,x):
                heappush(heap,cell(y+1,x,h))
                seen[y+1][x]=True
        
        return res


