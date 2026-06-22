class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # tokens = re.findall(r'([A-Z][a-z]*|\d+|[()])', formula)
        i=0
        n=len(formula)
        tokens = []
        while i<n:
            if formula[i] == "(":
                tokens.append("(")
                i+=1
            elif formula[i] == ")":
                tokens.append(")")
                i+=1
            elif formula[i].isupper():
                start=i
                i+=1
                while i<n and formula[i].islower():
                    i+=1
                tokens.append(formula[start:i])
            else:
                start=i
                i+=1
                while i<n and formula[i].isdigit():
                    i+=1
                tokens.append(int(formula[start:i]))


        print(tokens)

        stack=[defaultdict(int)]
        i=0
        n=len(tokens)

        while i<n:
        # if open paren
        #     push defaultdict to stack
            if tokens[i] == "(":
                stack.append(defaultdict(int))
                i+=1

        # if closing paren
        #     mult =1
        #     if next token is a multiplier
        #         mult=that
        #     pop s and merge it with s[-1] while applying mult
            elif tokens[i] == ")":
                mult=1
                if i+1<n and type(tokens[i+1]) is int:
                    mult=tokens[i+1]
                    i+=1
                curr=stack.pop()
                for a in curr:
                    stack[-1][a]+=curr[a]*mult
                i+=1
        
        # else
        #     parse the atom into s[-1], use +=
            else:
                name=tokens[i]
                count=1
                if i+1<n and type(tokens[i+1]) is int:
                    count=tokens[i+1]
                    i+=1
                stack[-1][name]+=count
                i+=1
                
        print(stack)
        res=stack[-1]
        return ''.join([key+("" if res[key]==1 else str(res[key])) for key in sorted(res.keys())])
        

