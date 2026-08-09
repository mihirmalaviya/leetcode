class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res=[]
        curr=[]

        def b(i,x):
            if i==len(candidates):
                if x==0:
                    res.append(curr[:])
                return
            
            if candidates[i]<=x:
                curr.append(candidates[i])
                b(i,x-candidates[i])
                curr.pop()
            b(i+1,x)
        
        b(0,target)
        return res

