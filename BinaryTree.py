class Node(object):
    def __init__(self, value=0):
        self.left = None
        self.right = None
        self.value = value

    # Simple print statement, will try to add a pretty print method
    def __str__(self):
        return str(self.value)

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def print_tree(self):
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return '%s (%s, %s)' % (str(self.value),
                                    str(self.left),
                                    str(self.right))


def is_valid_node(node, value):
    while node is not None:
        if value == node.value:
            return True
        elif value < node.value:
            node = node.left
        elif value > node.value:
            node = node.right


bst = Node(11)
bst.insert(6)
bst.insert(4)
bst.insert(5)
bst.insert(8)
bst.insert(10)
bst.insert(19)
bst.insert(17)
bst.insert(43)
bst.insert(31)
bst.insert(49)
