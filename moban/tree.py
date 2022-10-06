import random

class Node:
    def __init__(self, val:int):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0
        self.have = 0

class TreeSet:
    def __init__(self):
        self.root = None

    def _insert(self, val:int, sta:Node):
        if sta.val == val:
            sta.have += 1
            sta.count += 1
            return
        if val < sta.val:
            if not sta.left: sta.left = Node(val)
            self._insert(val, sta.left)
            sta.count += 1
        if val > sta.val:
            if not sta.right: sta.right = Node(val)
            self._insert(val, sta.right)
            sta.count += 1
        
    def insert(self, val:int):
        if not self.root: self.root = Node(val)
        self._insert(val, self.root)

    def _remove(self, val:int, sta:Node)->bool:
        if sta.val == val:
            if sta.have < 1:return False
            sta.have -= 1
            sta.count -= 1
            return True
        if val < sta.val:
            if not sta.left: sta.left = Node(val)
            succe = self._remove(val, sta.left)
            if succe: sta.count -= 1
        if val > sta.val:
            if not sta.right: sta.right = Node(val)
            succe = self._remove(val, sta.right)
            if succe: sta.count -= 1
        return succe

    def remove(self, val:int)->bool:
        if not self.root: return False
        return self._remove(val, self.root)

    def toList(self):
        ans = []
        def bianli(node:Node):
            if node is None: return
            bianli(node.left)
            for _ in range(node.have):
                ans.append(node.val)
            bianli(node.right)
        if self.root: bianli(self.root)
        return ans

    def _at(self, val, sta:Node, num=0):
        if sta is None: return num
        if sta.val == val:
            return num + self._len(sta.left)
        if val < sta.val:
            return self._at(val, sta.left, num)
        if val > sta.val:
            return self._at(val, sta.right, num+sta.have+self._len(sta.left))
    
    def at(self, val):
        return self._at(val, self.root)

    def _len(self, node:Node):
        return node.count if node else 0

    def len(self):
        return self._len(self.root)

    def max(self):
        if self.len() == 0: return None
        node = self.root
        while self._len(node.right) > 0:
            node = node.right
        return node.val

    def min(self):
        if self.len() == 0: return None
        node = self.root
        while self._len(node.left) > 0:
            node = node.left
        return node.val

    def _get(self, i:int, node:Node):
        if i < self._len(node.left): return self._get(i, node.left)
        elif i < self._len(node.left) + node.have: return node.val
        else: return self._get(i-self._len(node.left)-node.have,node.right)

    def get(self, i:int):
        if i < 0 or i >= self.len(): return None
        return self._get(i, self.root)


if __name__ == '__main__':
    t = TreeSet()
    lis = list(range(100))
    random.shuffle(lis)
    for i in lis: t.insert(i)
    # print(t.toList())
    t.remove(99)
    t.remove(71)
    print(t.at(10))
    print(t.at(10.1))
    print(t.at(11))
    print(t.len())
    t.insert(999)
    print(t.max())
    print(t.remove(11))
    print(t.remove(11))
    print(t.get(88))