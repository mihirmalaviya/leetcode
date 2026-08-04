class Solution:
    def isValid(self, s: str) -> bool:
        

        stk=[]
        m={
            '}':'{',
            ')':'(',
            ']':'['
        }
        for ch in s:
            if ch in m:
                if not stk:
                    return False
                    
                if m[ch]==stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(ch)

        return len(stk)==0
