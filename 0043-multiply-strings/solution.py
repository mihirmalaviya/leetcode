class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"
        
        n1,n2=len(num1),len(num2)
        res=[0]*(n1+n2)

        for i in reversed(range(n1)):
            for j in reversed(range(n2)):
                p=int(num1[i])*int(num2[j])
                s=res[i+j+1]+p

                res[i+j+1]=s%10
                res[i+j]+=s//10

        i=0
        while res[i]==0:
            i+=1

        return ''.join([str(n) for n in res[i:]])
