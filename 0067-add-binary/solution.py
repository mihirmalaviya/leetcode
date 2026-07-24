class Solution:
    def addBinary(self, a: str, b: str) -> str:
        

        res=""

        if len(b)>len(a): a,b=b,a
        while len(b)<len(a): b="0"+b
        carry=0

        for i in reversed(range(len(a))):
            if a[i]=="1" and b[i]=="1":
                if not carry:
                    res="0"+res
                    carry=1
                else:
                    res="1"+res
                
            elif a[i]=="0" and b[i]=="0":
                if not carry:
                    res="0"+res
                else:
                    res="1"+res
                carry=0
            
            else:
                if not carry:
                    res="1"+res
                else:
                    res="0"+res

        if carry:
            res="1"+res
        return res

