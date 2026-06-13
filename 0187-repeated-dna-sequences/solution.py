class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        
        seen=set()
        res=set()
        for i in range(len(s)-10+1):
            subseq=s[i:i+10]
            if subseq in seen:
                res.add(subseq)
            seen.add(subseq)

        return list(res)
        

