class Node:
    def __init__(self):
        self.children = {}
        self.value = ""

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.value = value

    def load_dictionary_to_trie(self, filepath):
        with open(filepath, 'r', encoding="utf-8-sig") as file:
            for line in file:
                tokens = line.strip().split("=")
                key = tokens[0]
                value = tokens[1].split("/")[0]
                self.insert(key, value)