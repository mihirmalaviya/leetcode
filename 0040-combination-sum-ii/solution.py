class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res=[]
        def dfs(curr, i, target):
            if target<0:
                return
            if target==0:
                res.append(curr[:])
                return
            if i==len(candidates):
                return
            
            
            curr.append(candidates[i])
            dfs(curr,i+1,target-candidates[i])

            x=curr.pop()
            while i<len(candidates) and candidates[i]==x:
                i+=1

            dfs(curr,i,target)
        
        dfs([],0,target)

        return res

