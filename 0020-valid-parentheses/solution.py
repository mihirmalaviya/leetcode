class Solution:
    def isValid(self, s: str) -> bool:

        closing={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        stack=[]
        for ch in s:
            if not ch in closing:
                stack.append(ch)
            else:
                if not stack: 
                    return False
                if closing[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()

        return not bool(stack)
                
