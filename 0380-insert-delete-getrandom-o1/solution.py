class RandomizedSet:

    def __init__(self):
        self.s={}
        self.l=[]

    def insert(self, val: int) -> bool:
        res=not val in self.s # val isnt in set

        if res:
            self.l.append(val)
            self.s[val]=len(self.l)-1

        return res

    def remove(self, val: int) -> bool:
        res=val in self.s

        if res:
            if self.s[val]==len(self.s)-1:
                self.l.pop()
            else:
                oldidx=self.s[val]
                self.l[-1],self.l[oldidx]=self.l[oldidx],self.l[-1]
                self.l.pop()

                self.s[self.l[oldidx]]=oldidx

            del self.s[val]

        return res

    def getRandom(self) -> int:
        return random.choice(self.l)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
