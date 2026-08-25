class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return 1
        
        cant=set()
        candidates=[set() for _ in range(n)]
        res=-1

        for a,b in trust:
            cant.add(a)

        for a,b in trust:
            if b not in cant:
                candidates[b-1].add(a)
                if len(candidates[b-1])==n-1:
                    if res!=-1:
                        return -1
                    res=b
        
        return res

        
'''


'''
