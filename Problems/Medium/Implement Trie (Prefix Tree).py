class Trie_Node:
    def __init__(self):
        self.children = [None] * 26
        self.terminal = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return Trie_Node()

    def char_to_index(self, ch):
        return ord(ch) - ord("a")

    def insert(self, word: str) -> None:

        current_node = self.root
        for level in range(len(word)):
            index = self.char_to_index(word[level])

            if not current_node.children[index]:
                current_node.children[index] = self.get_node()
            current_node = current_node.children[index]
        current_node.terminal = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for level in range(len(word)):
            index = self.char_to_index(word[level])
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return current_node.terminal

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for level in range(len(prefix)):
            index = self.char_to_index(prefix[level])
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
