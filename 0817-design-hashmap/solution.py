class Node:
    def __init__(self,val=-1,key=-1):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class List:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def push(self,n):
        n.prev=self.tail.prev
        n.next=self.tail
        self.tail.prev.next=n
        self.tail.prev=n

    def remove(self,n):
        n.next.prev=n.prev
        n.prev.next=n.next


class MyHashMap:

    def __init__(self):
        self.buckets=[None for _ in range(1000)]
    
    def b(self,key):
        x=self.buckets[key%len(self.buckets)]
        if not x:
            x=List()
            self.buckets[key%len(self.buckets)]=x

        return x


    def find(self,key):
        b=self.b(key)

        curr=b.head
        while curr:
            if curr.key==key:
                return curr
            curr=curr.next

        return None


    def put(self, key: int, value: int) -> None:
        b=self.b(key)

        x=self.find(key)
        if x:
            x.val=value
        else:
            b.push(Node(value,key))


    def get(self, key: int) -> int:
        x=self.find(key)
        return x.val if x else -1


    def remove(self, key: int) -> None:
        b=self.b(key)

        x=self.find(key)
        if x:
            b.remove(x)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
