class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        n,k=len(s),len(words[0])
        wordset=Counter(words)

        res=[]
        for offset in range(k):
            l=offset
            seen=defaultdict(int)
            total=0
            for r in range(offset+k,n+1,k):
                curr=s[r-k:r]
                if curr in wordset:
                    seen[curr] += 1
                    total += 1
                    while seen[curr] > wordset[curr]:
                        left_word = s[l:l + k]
                        seen[left_word] -= 1
                        total -= 1
                        l+=k
                    if total == len(words):
                        res.append(l)
                else:
                    seen.clear()
                    total = 0
                    l = r
        return res
