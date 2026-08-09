class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dp = [[0]*(amount+1) for _ in range(len(coins)+1)]


        dp=[0]*(amount+1)
        dp[0]=1

        for i in reversed(range(len(coins))):
            for x in range(coins[i],amount+1):
                dp[x]+=dp[x-coins[i]]

        return dp[amount]
        # @cache
        # def ways(i,x):
        #     if i==len(coins):
        #         return 1 if x==0 else 0
            
        #     take=0
        #     skip=ways(i+1,x)
        #     if coins[i]<=x:
        #         take=ways(i,x-coins[i])
            
        #     return skip+take
        
        # return ways(0,amount)
