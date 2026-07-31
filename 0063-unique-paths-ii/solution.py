class Solution:
    def uniquePathsWithObstacles(self, dp: List[List[int]]) -> int:
        m,n=len(dp),len(dp[0])

        if dp[m-1][n-1]==1:return 0
        if dp[0][0]==1:return 0

        def isValid(y,x):
            if y>=m: return 0
            if x>=n: return 0
            if dp[y][x]>0: return 0
            return 1

        dp[m-1][n-1]=-1
        for y in reversed(range(m)):
            for x in reversed(range(n)):
                if dp[y][x]==1:
                    continue
                if isValid(y+1,x):
                    dp[y][x]+=dp[y+1][x]
                if isValid(y,x+1):
                    dp[y][x]+=dp[y][x+1]
        
        # print(dp)
        return -dp[0][0]
        
