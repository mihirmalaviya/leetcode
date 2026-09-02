class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l=max(weights)
        r=sum(weights)
        
        def can(cap):
            i=1
            c=0
            for w in weights:
                c+=w
                if c>cap:
                    c=w
                    i+=1
            print(cap,i)
            return i<=days

        return l+bisect_left(range(l,r), True, key=can)


