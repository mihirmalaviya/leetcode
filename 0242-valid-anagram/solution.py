class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t): return False

        counts = [0]*26
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')] += 1
            counts[ord(t[i])-ord('a')] -= 1
        
        return counts == [0]*26
        
