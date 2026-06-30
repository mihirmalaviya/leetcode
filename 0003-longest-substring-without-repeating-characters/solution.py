class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        res=0
        l=0
        counter=defaultdict(int)
        for r in range(len(s)):
            ch=s[r]
            while counter[ch]>=1:
                counter[s[l]]-=1
                l+=1
            counter[ch]+=1
            # print(counter)
            res=max(res,r-l+1)
        return res
            
