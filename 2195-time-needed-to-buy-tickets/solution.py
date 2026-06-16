class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        res=0
        target=tickets[k]
        for i in range(len(tickets)):
            t=tickets[i]
            res+=min(t,target-1)
            if t>target-1 and i<=k:
                res+=1

        return res

