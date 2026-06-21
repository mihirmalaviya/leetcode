class Solution:
    def maxDistance(self, moves: str) -> int:

        cts=Counter(moves)
        print(cts)

        u,r=0,0
        x=0
        if 'R' in cts:
            r+=cts['R']
        if 'L' in cts:
            r-=cts['L']
        if 'U' in cts:
            u+=cts['U']
        if 'D' in cts:
            u-=cts['D']
        if '_' in cts:
            x+=cts['_']

        u=abs(u)
        r=abs(r)
        return u+r+x
