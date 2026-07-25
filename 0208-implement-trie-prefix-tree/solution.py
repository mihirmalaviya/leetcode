class Node:
    def __init__(self):
        self.children={}
        self.end=False


class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        # traverse till u get there and add

        curr=self.root
        for ch in word:
            if not ch in curr.children:
                curr.children[ch]=Node()
            
            curr=curr.children[ch]
        curr.end=True


    def search(self, word: str) -> bool:
        # traverse till u get there and return
        curr=self.root
        for ch in word:
            if ch in curr.children:
                curr=curr.children[ch]
            else: 
                return False
            
        return curr.end
                
        
    def startsWith(self, prefix: str) -> bool:
        # traverse till u get there and return

        curr=self.root
        for ch in prefix:
            if ch in curr.children:
                curr=curr.children[ch]
            else: 
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
