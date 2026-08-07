class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        s=deque([("(",1,0)])
        for i in range(n*2):
            for _ in range(len(s)):
                seq,openings,closings=s.popleft()
                if len(seq)==n*2:
                    res.append(seq)

                if openings<n:
                    s.append((seq+"(", openings+1, closings))
                if closings<openings:
                    s.append((seq+")", openings, closings+1))
                    
        return res
                

