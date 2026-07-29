class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        maxfreq=0
        res=0

        l=0
        for r in range(len(s)):
            freq[s[r]]+=1
            maxfreq=max(freq[s[r]], maxfreq)

            while (r-l+1)-maxfreq>k:
                freq[s[l]]-=1
                l+=1

            res=max(res,r-l+1)
        return res


