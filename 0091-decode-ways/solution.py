class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        memo=[-1]*(len(s)+1)

        def dfs(p,memo=memo):
            if memo[p]!=-1:
                return memo[p]

            n=len(s)
            if p==n: return 1
            if s[p]=='0': return 0

            res=dfs(p+1)
            if p<n-1 and (s[p]=='1' or (s[p]=='2'and s[p+1]<'7')): 
                res+=dfs(p+2)

            memo[p]=res
            return res

        return dfs(0)
