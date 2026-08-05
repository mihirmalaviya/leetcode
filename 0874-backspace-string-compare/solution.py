class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stk=[]
        stk2=[]
        for ch in s:
            if ch!="#":
                stk.append(ch)
            else:
                if stk:
                    stk.pop()
        for ch in t:
            if ch!="#":
                stk2.append(ch)
            else:
                if stk2:
                    stk2.pop()
        return "".join(stk)=="".join(stk2)
