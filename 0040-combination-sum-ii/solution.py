class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res=[]
        curr=[]

        def b(i,x):
            if i==len(candidates):
                if x==0:
                    res.append(curr[:])
                return
            
            if candidates[i]<=x:
                curr.append(candidates[i])
                b(i+1,x-candidates[i])
                curr.pop()
            
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
                
            b(i+1,x)
        
        b(0,target)
        return res


