class Solution:
    def reverseVowels(self, s: str) -> str:

        l,r=0,len(s)-1
        s=[ch for ch in s]
        while r>l:
            while r>0 and s[r].lower() not in "aeiou":
                r-=1
            while l<len(s) and s[l].lower() not in "aeiou":
                l+=1
            if not r>l:
                return ''.join(s)
            
            s[r],s[l]=s[l],s[r]
            r-=1
            l+=1

        return ''.join(s)

