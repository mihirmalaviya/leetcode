class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        for token in tokens:
            # print(stack)
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b,a=stack.pop(),stack.pop()
                if   token=="+": stack.append(a+b)
                elif token=="-": stack.append(a-b)
                elif token=="*": stack.append(a*b)
                else:
                    # print(a,b,a/b) 
                    stack.append(int(float(a)/b))

        return stack[0]
