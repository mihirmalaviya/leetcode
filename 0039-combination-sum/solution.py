class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res=[]

        def dfs(curr,i,target):
            if target<0:
                return
            if target==0:
                res.append(curr[:])
                return
            if i==len(candidates):
                return

            curr.append(candidates[i])
            dfs(curr,i,target-candidates[i])

            curr.pop()
            dfs(curr,i+1,target)
        
        dfs([],0,target)
        return res


