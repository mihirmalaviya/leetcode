class Solution:
    def countPrimes(self, n: int) -> int:

        if n<=1: return 0

        primes=[True for _ in range(n)]
        primes[0]=False
        primes[1]=False

        res=0
        for p in range(2,n):
            if not primes[p]:
                continue
            res+=1
            for i in range(p*2,n,p):
                primes[i]=False
                
        return res
        
