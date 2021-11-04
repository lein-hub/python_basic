class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def search(self, data):
        return self._search_value(self.root, data)

    def _search_value(self, node, data):
        if node.data == data or node is None:
            return node is not None
        elif node.data > data:
            return self._search_value(node.left, data)
        else:
            return self._search_value(node.right, data)

    def delete(self, data):
        self.root = self._delete_value(self.root, data)

    def _delete_value(self, node, data):
        if node is None:
            return node

        if node.data == data:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
        elif node.data > data:
            node.left = self._delete_value(node.left, data)
        else:
            node.right = self._delete_value(node.right, data)
        return node


n10 = Node()
n4 = Node()
n11 = Node()
n2 = Node()
n7 = Node()
n1 = Node()
n3 = Node()
n5 = Node()
n6 = Node()

n10.left = n4
n10.right = n11
n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3
n7.left = n5
n5.right = n6


def pre_order(node):
    print(node.data)

    if (node.left):
        pre_order(node.left)

    if (node.right):
        pre_order(node.right)


def in_order(node):
    if (node.left):
        in_order(node.left)

    print(node.data)

    if (node.right):
        in_order(node.right)


def post_order(node):
    if (node.left):
        post_order(node.left)

    if (node.right):
        post_order(node.right)

    print(node.data)

# pre_order(n0)


lst = [10, 11, 4, 7, 2, 3, 1, 5, 6]
# lst = [2, 1, 3]

bst = BinarySearchTree()

for i in lst:
    bst.insert(i)

bst.delete(4)

pre_order(bst.root)
