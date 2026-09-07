class MinStack:

    def __init__(self):
        self.mins=[]
        self.s=[]

    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.mins or self.mins[-1]>=value:
            self.mins.append(value)

    def pop(self) -> None:
        x=self.s.pop()
        if self.mins and self.mins[-1]==x:
            self.mins.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
