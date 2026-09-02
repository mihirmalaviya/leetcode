class TimeMap:

    def __init__(self):
        self.vmap=defaultdict(list)
        self.tmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vmap[key].append(value)
        self.tmap[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.vmap:
            return ""
        i=bisect_right(self.tmap[key],timestamp)-1
        return self.vmap[key][i] if i>=0 else ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
