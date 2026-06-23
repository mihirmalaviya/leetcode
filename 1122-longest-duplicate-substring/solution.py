class Solution:
    def longestDupSubstring(self, s: str) -> str:
        lo,hi=0,len(s)
        res=""

        while lo<=hi:
            m=lo+(hi-lo)//2
            print(m)
            found=False
            seen=set()
            # seen_indexes=[]
            for r in range(m,len(s)+1):
                curr=s[r-m:r]
                # print(curr)
                if curr in seen:
                    # print(curr)
                    found=True
                    # seen_indexes.append(r-m)
                    if m>len(res):
                        res=curr
                seen.add(curr)
            if found:
                lo=m+1
            else:
                hi=m-1
                
        return res


