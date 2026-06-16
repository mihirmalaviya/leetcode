class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        s,t=[ch for ch in s],[ch for ch in t]
        
        looking=s[-1]
        while s and t:
            if t.pop()==looking:
                s.pop()
                if not s:
                    return True
                else:
                    looking=s[-1]

        return False


