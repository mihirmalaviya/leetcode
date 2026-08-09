class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        @cache
        def dp(i,x):
            if i==len(coins):
                return 0 if x==0 else float('inf')
            
            take=float('inf')
            skip = dp(i+1,x)
            if coins[i]<=x:
                take = 1+dp(i,x-coins[i])

            return min(take, skip)

        res=dp(0,amount)
        return -1 if res==float('inf') else res

