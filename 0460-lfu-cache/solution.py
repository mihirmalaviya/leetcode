class ListNode:
    def __init__(self,key=-1, val=-1,freq=1):
        self.key=key
        self.val=val
        self.freq=freq
        self.next=None
        self.prev=None

class List:
    def __init__(self):
        self.size=0

        self.head=ListNode()
        self.tail=ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, node):
        node.next=self.head.next
        node.prev=self.head

        self.head.next.prev=node
        self.head.next=node

        self.size+=1

    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

        self.size-=1

    def pop(self):
        if self.size==0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.size=0
        self.minfreq=0
        self.map={}
        self.freqlist={}

    def updatefreq(self,n):
        self.freqlist[n.freq].remove(n)

        if n.freq==self.minfreq and self.freqlist[n.freq].size==0:
            self.minfreq+=1
        n.freq+=1

        if n.freq not in self.freqlist:
            self.freqlist[n.freq]=List()
        
        self.freqlist[n.freq].push(n)

    def get(self, key: int) -> int:
        if not key in self.map:
            return -1
        
        n=self.map[key]
        self.updatefreq(n)
        
        return n.val

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return

        if key in self.map:
            n=self.map[key]
            n.val=value

            self.updatefreq(n)
            return
        
        if self.size == self.cap:
            n=self.freqlist[self.minfreq].pop()

            del self.map[n.key]
            
            self.size-=1
        
        n=ListNode(key,value)
        self.minfreq=1
        if 1 not in self.freqlist:
            self.freqlist[1]=List()
        
        self.freqlist[1].push(n)

        self.map[key]=n
        self.size+=1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''

init

map  (key:node) 
head
capacity


get

pop from LL and put on head
return val


put

pop from ll and put on head







'''

