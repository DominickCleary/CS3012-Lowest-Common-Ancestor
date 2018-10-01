class Node(object):
    def __init__(self, value=0,
                 left=None, right=None,
                 id=None, parent=None):
        self.id = id
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return '%s (%s, %s)' % (
                str(self.value),
                str(self.left),
                str(self.right))

    def __repr__(self):
        s = 'TreeNode Object (id=' + str(self.id) + \
            ' value=' + str(self.value) + ')'
        return s


root = Node(value=5,
            left=Node(value=4,
                      left=Node(value=1,
                                right=Node(value=2))
                      ),
            right=Node(value=8,
                       left=Node(value=3),
                       right=Node(value=4,
                                  left=Node(value=9),
                                  right=Node(value=1))
                       )
            )

BST = Node(value=5,
           left=Node(value=2,
                     left=Node(value=1,
                               right=Node(value=1.5,
                                          left=Node(value=1.2))),
                     right=Node(value=3)
                     ),
           right=Node(value=9,
                      left=Node(value=7),
                      right=Node(value=15,
                                 right=Node(value=16)
                                 )
                      )
           )
