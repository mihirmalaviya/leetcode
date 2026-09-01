class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not len(hand)%groupSize==0:
            return False

        counts=Counter(hand)
        
        for key in sorted(counts.keys()):
            cnt=counts[key]
            if cnt>0:
                for x in range(key,key+groupSize):
                    if counts[x]<cnt:
                        return False
                    counts[x]-=cnt
            
        return True




