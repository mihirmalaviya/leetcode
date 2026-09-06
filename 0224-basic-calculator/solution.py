class Solution:
    def calculate(self, s: str) -> int:
        
        res=0
        cur=0
        sign=1
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif ch==")":
                res+=cur*sign
                res*=stack.pop()
                res+=stack.pop()
                cur=0
                sign=1
            elif ch=="+":
                res+=sign*cur
                sign=1
                cur=0
            elif ch=="-":
                res+=sign*cur
                sign=-1
                cur=0
            elif ch.isdigit():
                cur=10*cur+int(ch)
        
        res += sign*cur
        
        return res
