class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        

        res = []
        s = deque([('',0)])
        for i in range(n):
            m=len(s)
            for _ in range(m):
                t,c = s.popleft()
                
                s.append((t+'0',c))

                c+=i
                if (not t or t[-1] != '1') and c <= k:
                    s.append((t+'1',c))
        
        return [s for s,c in s]
        
        
