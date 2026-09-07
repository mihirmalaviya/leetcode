class Solution:
    def countGroups(self, pos: list[int], vel: list[int], distance: int) -> int:
        
        tv=vel[-1]
        tp=pos[-1]
        n=len(pos)
        
        groups=n
        for i in reversed(range(n-1)):
            
            p=pos[i]
            v=vel[i]
            
            if v>tv:
                groups-=1
            elif tp-p<=distance:
                groups-=1
            else:
                tv=v
            tp=p
        return groups
            
