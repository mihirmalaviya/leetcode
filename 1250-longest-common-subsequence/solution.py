class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n=len(text1)
        m=len(text2)

        dpi_1=[0]*(m+1)

        for i in range(1,n+1):
            dpi=[0]*(m+1)
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dpi[j] = 1+dpi_1[j-1]

                else:
                    dpi[j] = max(dpi_1[j], dpi[j-1])
            dpi_1=dpi

        return dpi[-1]

'''

        @cache
        def dp(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return 1+dp(i-1,j-1)
            else:
                return max(\
                    dp(i-1,j),
                    dp(i,j-1)
                )
            
        return dp(len(text1)-1, len(text2)-1)

'''
