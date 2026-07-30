class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo=[-1]*(n+1)
        memo[0]=1
        memo[1]=1
        def dfs(n,memo=memo):
            if memo[n]!=-1:
                return memo[n]

            memo[n]=dfs(n-1)+dfs(n-2)
            
            return memo[n]

        return dfs(n)
            

            

        
