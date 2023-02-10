class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        curr = self.root
        while True:
            if value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(value)
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(value)
                    return

    def lookup(self, value):
        curr = self.root
        while curr:
            if value == curr.value:
                return curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return None


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)


def print_tree_indent(node, level=0):
    if node is None:
        return
    print_tree_indent(node.right, level + 1)
    print(' ' * 4 * level + '->', node.value)
    print_tree_indent(node.left, level + 1)


print_tree_indent(tree.root)
# print_tree_indent(tree.lookup(170))
# print_tree_indent(tree.lookup(122))

# print_tree_indent(tree.root)
