class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        
        res=0
        for x in range(max(0,-k+n),k+n+1):
            if n&x==0:
                res+=x
        return res

'''
x
n-x = k
n-x = -k

x = max(0,-k+n)
x = k+n
'''
