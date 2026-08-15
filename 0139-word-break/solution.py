class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp=[False]*(len(s)+1)
        dp[-1]=True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if not i+len(word)>len(s) and s[i:i+len(word)]==word and dp[i+len(word)]:
                    dp[i]=True
                    break

        return dp[0]
'''
        @cache
        def dp(i):
            if i==len(s):
                return True
            
            res=False
            for word in wordDict:
                if i+len(word)>len(s):
                    pass
                else:
                    if s[i:i+len(word)]==word:
                        res |= dp(i+len(word))
            
            return res
        
        return dp(0)
'''
