class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        if len(self.max)==len(self.min):
            heappush(self.max, -num)
            heappush(self.min, -heappop(self.max))
        else:
            heappush(self.min, num)
            heappush(self.max, -heappop(self.min))

        
    def findMedian(self) -> float:
        if len(self.max)==len(self.min):
            return (self.min[0]-self.max[0])/2
        else:
            return self.min[0]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
