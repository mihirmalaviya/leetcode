class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        memo={}
        def find_lowest(i,a,memo=memo):
            if i>=len(coins) or a<=0:
                if a==0:
                    return 0
                else:
                    return float('inf')
            
            if (i,a) in memo:
                return memo[(i,a)]

            w=1+find_lowest(i,a-coins[i])
            wo=find_lowest(i+1,a)
            memo[(i,a)]=min(w,wo)
            return memo[(i,a)]
            
        res=find_lowest(0,amount)
        return res if res!=float('inf') else -1

