class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.map=defaultdict(list)
        for i,n in enumerate(arr):
            self.map[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        a=self.map[value]
        return bisect_right(a,right)-bisect_left(a,left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
