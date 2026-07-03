class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        baskets = {} 
        l= 0
        res = 0
        
        for r, f in enumerate(fruits):
            baskets[f] = r
            
            if len(baskets) > 2:
                d= min(baskets, key=baskets.get)
                l= baskets[d]+1
                del baskets[d]
                
            res = max(res, r-l+1)
            
        return res 

            
                

