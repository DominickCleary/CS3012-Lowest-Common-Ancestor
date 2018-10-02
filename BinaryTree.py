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
            return '%s (%s, %s)' % (str(self.value),
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


# def pretty_print(self):
#     # get each levels
#     level = [self]
#     to_prints = [[self.value]]
#     while True:
#         is_all_none = True
#         next_level = []
#         to_print = []
#         for n in level:
#             if n is None:
#                 next_level += [None, None]
#                 to_print += ['#', '#']
#             else:
#                 is_all_none = False
#                 next_level += [n.left, n.right]
#                 left_val = n.left.value if n.left and n.left.value else '#'
#                 right_val = n.right.value if n.right and n.right.value else '#'
#                 to_print += [left_val, right_val]
#         if is_all_none:
#             break
#         level = next_level
#         to_prints.append(to_print)
#
#     to_prints = to_prints[:-1]  # remove the last row with only '#'
#     to_pretty_prints = []
#     to_prints.reverse()
#     for i, row in enumerate(to_prints):
#         row = map(str, row)
#         sep = ' ' * (2 ** (i + 1) - 1)
#         space = ' ' * (2 ** i - 1)
#         to_pretty_prints.insert(0, space + sep.join(row) + space)
#     print('\n'.join(to_pretty_prints))
