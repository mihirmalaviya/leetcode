class Solution:
    def countAndSay(self, n: int) -> str:
        
        res="1"
        for _ in range(n-1):
            count=1
            new=[]
            for i in range(1,len(res)):
                if res[i]==res[i-1]:
                    count+=1
                else:
                    new.append(str(count))
                    new.append(res[i-1])
                    count=1
            
            new.append(str(count))
            new.append(res[-1])
                
            res="".join(new)

        return res
