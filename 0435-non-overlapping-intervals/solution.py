class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[1],x[0]))
        
        res=0
        l=0
        for r in range(1,len(intervals)):
            a,b=intervals[l],intervals[r]
            if b[0]<a[1]:
                res+=1
            else:
                l=r
        return res
        




'''
sort


'''
