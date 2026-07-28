class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x: x[0])

        res=[]
        prev=intervals[0]

        for i in range(1,len(intervals)):
            interval=intervals[i]
            if interval[0]<=prev[1]:
                prev[1] = max(prev[1],interval[1])
            else:
                res.append(prev)
                prev=interval

        res.append(prev)
        return res

