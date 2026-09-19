class Solution:
    def intToRoman(self, num: int) -> str:
        
        res=""
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        temp=num
        while temp>0:
            for s,v in zip(sym,val):
                if temp-v>=0:
                    res+=s
                    temp=temp-v
                    break

        return res
