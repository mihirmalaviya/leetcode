class MinStack:

    def __init__(self):
        self.pastmins=[]
        self.s=[]
        

    def push(self, value: int) -> None:
        if not self.pastmins:
            self.pastmins.append(value)
        elif self.pastmins[-1] >= value:
            self.pastmins.append(value)
        
        self.s.append(value)
        
        
    def pop(self) -> None:
        x=self.s.pop()
        if x==self.getMin():
            self.pastmins.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.pastmins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
