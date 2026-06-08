class MyQueue:

    def __init__(self):
        self.i, self.o = [],[]
        self.size=0
        
    def push(self, x: int) -> None:
        self.size+=1
        self.i.append(x)

    def pop(self) -> int:
        if not self.o:
            self.peek()
        self.size-=1
        return self.o.pop()


    def peek(self) -> int:
        if not self.o:
            while self.i:
                self.o.append(self.i.pop())
        return self.o[-1]

    def empty(self) -> bool:
        return self.size==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
