class Node:
    def __init__(self,val):
        self.val = val
        self.chi = [None]*26
        self.have = 0

class Dict:
    def __init__(self):
        self.root = Node(None)

    def _find(self, word):
        node = self.root
        for w in word:
            if node.chi[ord(w)-65] is None:
                node.chi[ord(w)-65] = Node(w)
            node = node.chi[ord(w)-65]
        return node

    def input(self, word):
        node = self._find(word)
        node.have += 1
    
    def remove(self, word):
        node = self._find(word)
        if node.have > 0: node.have -= 1

    def contain(self, word):
        node = self._find(word)
        return node.have > 0

    def toList(self):
        tore = []
        stk = []
        def bianli(node):
            if node is None: return
            stk.append(node.val)
            for i in range(node.have):
                # print(stk)
                tore.append(''.join(stk[1:]))
            for c in node.chi:
                bianli(c)
            stk.pop()
        bianli(self.root)
        return tore