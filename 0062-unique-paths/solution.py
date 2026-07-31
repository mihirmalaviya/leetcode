class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def isValid(y,x):
            if y>=m: return 0
            if x>=n: return 0
            return 1

        dp=[[0]*n for _ in range(m)]
        dp[m-1][n-1]=1
        for y in reversed(range(m)):
            for x in reversed(range(n)):
                if isValid(y+1,x):
                    dp[y][x]+=dp[y+1][x]
                if isValid(y,x+1):
                    dp[y][x]+=dp[y][x+1]
        
        # print(dp)
        return dp[0][0]
