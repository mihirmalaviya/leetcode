class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

        c=defaultdict(int)

        for b in bills:
            if b==20:
                if c[10]:
                    c[10]-=1
                    c[5]-=1
                else:
                    c[5]-=3
                    
                if c[10]<0 or c[5]<0:
                    return False
            elif b==10:
                c[5]-=1
                if c[5]<0:
                    return False

            c[b]+=1
            
        return True
