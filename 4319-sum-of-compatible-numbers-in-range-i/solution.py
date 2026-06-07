class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        for x in range(max(0,-k+n), k+n+1):
            if not x&n:
                res+=x
        return res

'''
x must be positive

n-x = k
x = -k+n

n-x = -k
x = k+n

'''
