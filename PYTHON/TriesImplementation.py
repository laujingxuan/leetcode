# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TriesNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        self.triesNode = TriesNode()

    def insert(self, word: str) -> None:
        currentTriesNode = self.triesNode
        i = 0
        while i < len(word):
            currentIndex = self.convertCharToIndex(word[i])
            if currentTriesNode.children[currentIndex] == None:
                currentTriesNode.children[currentIndex] = TriesNode()
            currentTriesNode = currentTriesNode.children[currentIndex]
            i += 1
        currentTriesNode.isEnd = True
        return

    def convertCharToIndex(self, char):
        return ord(char) - ord("a")

    def search(self, word: str) -> bool:
        currentTriesNode = self.triesNode
        i = 0
        while i < len(word):
            currentIndex = self.convertCharToIndex(word[i])
            if currentTriesNode.children[currentIndex] == None:
                return False
            currentTriesNode = currentTriesNode.children[currentIndex]
            i += 1
        return currentTriesNode.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        currentTriesNode = self.triesNode
        i = 0
        while i < len(prefix):
            currentIndex = self.convertCharToIndex(prefix[i])
            if currentTriesNode.children[currentIndex] == None:
                return False
            currentTriesNode = currentTriesNode.children[currentIndex]
            i += 1
        return True



