class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        

        m = {}
        for i, ch in enumerate(order):
            m[ch]=i
        
        words = [[m[c] for c in w] for w in words]
        
        return words==sorted(words)

