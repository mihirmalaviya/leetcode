class ListNode:
    def __init__(self, key, val=0):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.head=None
        self.tail=None
        self.map={}

    def get(self, key: int) -> int:
        if not key in self.map:
            return -1

        n=self.map[key]
        if n is not self.head:
            if n.prev: n.prev.next=n.next
            if n.next: n.next.prev=n.prev 
            if n is self.tail:
                self.tail=n.prev

            n.next=self.head
            n.prev=None

            self.head.prev=n
            self.head=n

        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val=value
            self.get(key)
            return

        temp=ListNode(key,value)
        if not self.head:
            self.head = temp
            self.tail = temp
        else:
            temp.next=self.head
            temp.prev=None
            self.head.prev=temp
            self.head=temp
            if len(self.map)>=self.c:
                n=self.tail
                self.tail=self.tail.prev
                self.tail.next=None
                del self.map[n.key]
        
        self.map[key]=temp
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
