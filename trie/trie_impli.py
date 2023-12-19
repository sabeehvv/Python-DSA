class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()

trie.insert("apple")
trie.insert("banana")
trie.insert("app")
trie.insert("bat")


print(trie.search("apple"))  
print(trie.search("app"))    
print(trie.search("bat"))    
print(trie.search("ball"))   

print(trie.starts_with("app"))  
print(trie.starts_with("ba"))   
print(trie.starts_with("xyz")) 