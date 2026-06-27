class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        target=Counter(t)
        total=len(t)
        l=0
        res=""
        minlen=float('inf')
        for r in range(len(s)):
            if s[r] in target:
                if target[s[r]]>0:
                    total-=1
                target[s[r]]-=1

            while total<=0: 
                if r-l<minlen:
                    minlen=r-l
                    res=s[l:r+1]
                if s[l] in target:
                    if target[s[l]]>=0:
                        total+=1
                    target[s[l]]+=1
                l+=1

        return res

