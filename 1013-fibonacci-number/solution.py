class Solution(object):
    def fib(self, n,memo=[]):
        """
        :type n: int
        :rtype: int
        """

        if n<2:return n

        memo=[-1]*(n+1)

        memo[0]=0
        memo[1]=1

        def dfs(n,memo):
            if memo[n]!=-1:
                return memo[n]
            
            memo[n] = dfs(n-1,memo)+dfs(n-2,memo)
            return memo[n]
        
        return dfs(n,memo)

