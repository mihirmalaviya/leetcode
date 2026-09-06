class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        i=j=0
        res=[]
        while i<len(l1) and j<len(l2):
            al,ar=l1[i]
            bl,br=l2[j]

            if ar>=bl and br>=al:
                res.append([max(al,bl),min(ar,br)])
            
            if ar<=br:
                i+=1
            else:
                j+=1

        return res
