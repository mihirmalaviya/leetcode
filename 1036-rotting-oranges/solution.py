class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q=deque()
        fresh=set()

        h,w=len(grid),len(grid[0])
        for y in range(h):
            for x in range(w):
                if grid[y][x]==2:
                    q.append((y,x))
                elif grid[y][x]==1:
                    fresh.add((y,x))
            
        
        # print(fresh,q)
        res=0
        while q and fresh:
            for _ in range(len(q)):
                y,x=q.popleft()
                if (y-1,x) in fresh:
                    q.append((y-1,x))
                    fresh.discard(q[-1])
                if (y,x-1) in fresh:
                    q.append((y,x-1))
                    fresh.discard(q[-1])
                if (y+1,x) in fresh:
                    q.append((y+1,x))
                    fresh.discard(q[-1])
                if (y,x+1) in fresh:
                    q.append((y,x+1))
                    fresh.discard(q[-1])
            res+=1

        return res if not fresh else -1


