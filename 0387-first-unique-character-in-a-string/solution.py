class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        q=deque()
        seen=set()
        repeated=set()
        for i in range(len(s)):
            ch = s[i]
            if ch not in seen:
                q.append((ch,i))
                seen.add(ch)
            else:
                repeated.add(ch)
            
        while q and q[0][0] in repeated:
            q.popleft()

        return -1 if not q else q[0][1]

