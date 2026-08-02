class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for y in range(1,len(triangle)):
            for x in range(len(triangle[y])):
                if x>0 and x<len(triangle[y-1]):
                    triangle[y][x]+=min(triangle[y-1][x],triangle[y-1][x-1])
                elif x>0:
                    triangle[y][x]+=triangle[y-1][x-1]
                else:
                    triangle[y][x]+=triangle[y-1][x]
                    
        return min(triangle[-1])
            
            
