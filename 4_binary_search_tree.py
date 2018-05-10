class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def _insert(self, node, val):
        if node.value < val:
            if node.left is None:
                node.left = Node(value=val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(value=val)
            else:
                self._insert(node.right, val)

    def insert(self, new_val):
        self._insert(self.root, new_val)

    def _search(self, node, val):
        if node is None:
            return False
        elif node.value == val:
            return True
        elif node.value <= val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def search(self, find_val):
        return self._search(self.root, find_val)

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)