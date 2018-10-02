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


bst_root = Node(11)
bst_root.insert(6)
bst_root.insert(4)
bst_root.insert(5)
bst_root.insert(8)
bst_root.insert(10)
bst_root.insert(19)
bst_root.insert(17)
bst_root.insert(43)
bst_root.insert(31)
bst_root.insert(49)


# if __name__ == '__main__':
#     #test