class RangeModule:

    def __init__(self):
        self.intervals=[]

    def addRange(self, left: int, right: int) -> None:
        res=[]
        added=False

        for l,r in self.intervals:
            if r<left: # too small just add it
                res.append([l,r])
            elif l>right: # too big, insert and then add
                if not added:
                    res.append([left,right])
                    added=True
                res.append([l,r])
            else: # must overlap, so merge
                left=min(l,left)
                right=max(r,right)
        if not added:
            res.append([left,right])

        self.intervals=res

    def queryRange(self, left: int, right: int) -> bool:
        for l,r in self.intervals:
            if l<=left and right<=r:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        res=[]
        for l,r in self.intervals:
            if r<=left or l>=right:
                res.append([l,r])
            else:
                if l<left:
                    res.append([l,left])
                if r>right:
                    res.append([right,r])

        self.intervals=res

        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
