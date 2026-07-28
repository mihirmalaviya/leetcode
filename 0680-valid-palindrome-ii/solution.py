class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1
        skipped=False
        while l<r:
            if s[l]!=s[r]:
                if not skipped:
                    skipped=True
                    if s[l+1]==s[r]:
                        if self.isPalindrome(s[l+1:r+1]): return True
                    if s[r-1]==s[l]:
                        if self.isPalindrome(s[l:r]): return True
                    return False
                else:
                    return False
            else:
                l+=1
                r-=1
        return True

    def isPalindrome(self,s):
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
