class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for y in range(1,len(grid)):
            grid[y][0]+=grid[y-1][0]
        for x in range(1,len(grid[0])):
            grid[0][x]+=grid[0][x-1]
        
        for y in (range(1,len(grid))):
            for x in (range(1,len(grid[0]))):
                grid[y][x]+=min(grid[y-1][x],grid[y][x-1])
            
        return grid[-1][-1]
