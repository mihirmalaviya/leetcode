class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # memo=[-1]*(len(cost)+1)
        # memo[0]=cost[0]
        # memo[1]=cost[1]
        # cost.append(0)

        # def dfs(i,memo=memo):
        #     if memo[i]!=-1:
        #         return memo[i]
            
        #     memo[i]=min(dfs(i-1),dfs(i-2))+cost[i]
        #     return memo[i]
    
        # return dfs(len(cost)-1)

        cost.append(0)
        a,b=cost[0],cost[1]

        for i in range(2,len(cost)):
            a,b=b,a
            b=min(a,b)+cost[i]

        return b

            


            
