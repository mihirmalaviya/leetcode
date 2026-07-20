class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2): return False

        l=0
        target=Counter(s1)
        curr=Counter()
        for r in range(len(s2)):
            ch=s2[r]
            curr[ch]+=1

            if r>=len(s1):
                curr[s2[l]]-=1
                if curr[s2[l]]==0:
                    del curr[s2[l]]
                l+=1

            if r+1>=len(s1):
                # print(target,curr)
                if curr==target:
                    return True

        # print(target,curr)
        # if curr==target:
        #     return True

        return False

