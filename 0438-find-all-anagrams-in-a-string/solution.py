class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p)>len(s):
            return []
        target=Counter(p)
        curr=Counter()

        res=[]
        for i,ch in enumerate(s):
            curr[ch]+=1

            if i-len(p)>=0:
                curr[s[i-len(p)]]-=1

            if +curr==+target:
                res.append(i-len(p)+1)
        
        return res


