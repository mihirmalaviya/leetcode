class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        rows=[[] for _ in range(numRows)]

        h=0
        d=1
        for ch in s:
            rows[h].append(ch)
            if h==0:
                d=1
            if h==numRows-1:
                d=-1
            h+=d
        
        return ''.join([''.join(r) for r in rows])
            
                

