class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        s=1
        if x<0:
            x*=-1
            s=-1

        res=0
        while x:
            res=res*10
            res+=x%10
            x=x//10


        res*=s
        return res if -(2**31) <= res <= (2**31 - 1) else 0
