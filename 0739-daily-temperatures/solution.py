class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res=[0]*len(temps)
        s=[] # monotonic incresing stack

        for i,t in enumerate(temps):
            while s and s[-1][1]<t:
                j=s.pop()[0]
                res[j]=i-j
            s.append([i,t])

        return res
