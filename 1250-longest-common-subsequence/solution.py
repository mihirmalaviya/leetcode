class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        h,w=len(text1),len(text2)
        dp=[[0]*(w+1) for _ in range(h+1)]

        for y in range(1,h+1):
            for x in range(1,w+1):
                if text1[y-1]==text2[x-1]:
                    dp[y][x] = 1+dp[y-1][x-1]
                    
                dp[y][x] = max(dp[y][x],dp[y-1][x])
                dp[y][x] = max(dp[y][x],dp[y][x-1])
        
        return dp[h][w]
