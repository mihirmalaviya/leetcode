class FreqStack:

    def __init__(self):
        self.freq=defaultdict(int)
        self.m=defaultdict(list)
        self.max=0

    def push(self, val: int) -> None:
        self.freq[val]+=1
        self.max=max(self.max,self.freq[val])
        self.m[self.freq[val]].append(val)

        
    def pop(self) -> int:
        x=self.m[self.max].pop()
        self.freq[x]-=1
        if not self.m[self.max]:
            self.max-=1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
