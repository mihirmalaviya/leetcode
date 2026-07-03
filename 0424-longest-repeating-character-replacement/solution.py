class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res=0
        freq = [set() for _ in range(len(s))]
        counts = defaultdict(int)
        maxfreq=0

        l=0
        for r in range(len(s)):
            
            counts[s[r]]+=1
            c=counts[s[r]]
            maxfreq=max(maxfreq,c)
            freq[c-1].add(s[r])

            total=r-l+1
            if k>=total-maxfreq:
                res=max(res,total)
            
            # print(total,maxfreq,freq)

            while l<r and not k>=total-maxfreq:
                # print(total,maxfreq)
                c=counts[s[l]]
                counts[s[l]]-=1

                freq[c-1].discard(s[l])
                if not freq[c-1]:
                    maxfreq-=1

                total=l-r+1
                l+=1

        return res
                    
            
            

'''
keep a sliding counter
k must be <= total-max
we have a freqs array of sets to store freqs
'''
