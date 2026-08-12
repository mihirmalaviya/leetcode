class Solution:
    def countBits(self, n: int) -> List[int]:
        

        res=[0]
        i=0
        while i<n:
            for j in range(len(res)):
                res.append(res[j]+1)
                i+=1
                if i>=n:
                    return res
        return res
            


'''

0 1 1 2 1 2 2 3

'''
