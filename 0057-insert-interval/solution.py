class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        nl,nr=newInterval
        res=[]

        i=0
        intervals=intervals[::-1]
        while intervals:
            l,r = intervals[-1]
            if r<nl:
                res.append([l,r])
                intervals.pop()
                i+=1
            elif l>nr:
                break
            else:
                nl=min(l,nl)
                nr=max(r,nr)
                intervals.pop()

        res.append([nl,nr])
        res.extend(intervals[::-1])
        return res

        

            
