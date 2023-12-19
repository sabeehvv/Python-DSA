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
                return []
            node = node.children[char]
        return self._get_all_words(node, prefix)

    def delete(self, word):
        if not self.search(word):
            return
        node = self.root
        path = []
        for char in word:
            path.append((char, node))
            node = node.children[char]
        node.is_word = False
        if not node.children:
            for char, n in reversed(path):
                del n.children[char]

    def _get_all_words(self, node, prefix):
        words = []
        if node.is_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._get_all_words(child, prefix + char))
        return words


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


trie.delete("apple")
print(trie.search("apple"))
