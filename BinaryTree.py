class Node(object):
    def __init__(self, value=0,
                 left=None, right=None,
                 key=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

# Simple print statement, will try to add a pretty print method
    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return '%s (%s, %s)' % (
                str(self.value),
                str(self.left),
                str(self.right))


# Hardcoded for now, will add customisable tree later if possible
BST = Node(value=5,
           left=Node(value=2,
                     left=Node(value=1,
                               right=Node(value=2,
                                          left=Node(value=6))),
                     right=Node(value=3)
                     ),
           right=Node(value=9,
                      left=Node(value=7),
                      right=Node(value=15,
                                 right=Node(value=16)
                                 )
                      )
           )
