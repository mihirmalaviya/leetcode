class MyCircularQueue:

    def __init__(self, k: int):
        self.list=[0]*k
        self.size=0
        self.start=0
        self.end=-1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size+=1
        
        self.end+=1
        self.end%=len(self.list)
        self.list[self.end]=value
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start+=1
        self.start%=len(self.list)
        self.size-=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.start]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.end]
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==len(self.list)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
