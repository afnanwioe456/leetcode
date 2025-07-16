from collections import defaultdict

def TrieNode():
    return defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node[ch]
        node['#'] = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '#' in node

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True