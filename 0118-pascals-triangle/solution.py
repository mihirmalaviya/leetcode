class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res=[]
        prev=[1]
        for i in range(numRows):
            curr=[1]*(i+1)

            for j in range(1,i):
                curr[j]=prev[j-1]+prev[j]
            res.append(curr)
            prev=res[-1]

        return res
