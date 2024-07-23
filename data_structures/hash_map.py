class HashMap:

    def __init__(self) -> None:
        self.num_buckets = 10000
        self.buckets = []
        for _ in range(self.num_buckets):
            self.buckets.append([])
    
    def add(self, key, val):
        idx = hash(key) % self.num_buckets
        for i, tup in enumerate(self.buckets[idx]):
            if tup[0] == key:
                self.buckets[idx][i] = (key, val)
                return
        self.buckets[idx].append((key, val))
    
    def find(self, key):
        idx = hash(key) % self.num_buckets
        for i, tup in enumerate(self.buckets[idx]):
            if tup[0] == key:
                return tup[1]
        return -1