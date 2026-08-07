class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        curr=[]

        def dfs(x):
            if len(curr)==k:
                res.append(curr[:])
                return

            for i in range(x,n+1):
                curr.append(i)
                dfs(i+1)
                curr.pop()

        dfs(1)
        return res
