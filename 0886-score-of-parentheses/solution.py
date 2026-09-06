class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        cur=0
        for ch in s:
            if ch=="(":
                stack.append(cur)
                cur=0
            else:
                cur=stack.pop()+max(2*cur,1)
        return cur
