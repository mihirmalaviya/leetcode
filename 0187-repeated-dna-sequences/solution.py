class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10: return []
        
        res=set()
        seen = set()
        for i in range(len(s)-9):
            sub=s[i:i+10:]
            if sub in seen: res.add(sub)
            seen.add(sub)

        return list(res)
        

