class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a,b,c=0,1,1
        if n<2:
            return n
        if n==2:
            return 1

        for i in range(2,n):
            a=a+b+c
            a,b,c=b,c,a

        return c
