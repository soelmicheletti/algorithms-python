# data structure storing prefixes
class Trie:

    def __init__(self):
        self.children = {}
        self.leaf = False
        

    def insert(self, word: str) -> None:
        if not len(word):
            self.leaf = True
        elif word[0] in self.children.keys():
            self.children[word[0]].insert(word[1:])
        else:
            self.children[word[0]] = Trie()
            self.children[word[0]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        if not len(word):
            return self.leaf
        if word[0] not in self.children.keys():
            return False
        return self.children[word[0]].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if not len(prefix):
            return True
        if prefix[0] not in self.children.keys():
            return False
        return self.children[prefix[0]].startsWith(prefix[1:])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)