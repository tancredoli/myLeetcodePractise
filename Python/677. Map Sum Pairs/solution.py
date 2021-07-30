from collections import defaultdict


class Node:
    def __init__(self):
        self.dic = defaultdict(Node)
        self.val = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, key: str, val: int) -> None:
        curr = self.trie
        for c in key:
            if c not in curr.dic:
                curr.dic[c] = Node()
            curr = curr.dic[c]
        curr.val = val

    def sum(self, prefix: str) -> int:
        curr = self.trie
        for c in prefix:
            if c not in curr.dic:
                return 0
            curr = curr.dic[c]

        def dfs(node):
            if not node.dic:
                return node.val

            res = node.val
            for child in node.dic.values():
                res += dfs(child)
            return res

        return dfs(curr)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)