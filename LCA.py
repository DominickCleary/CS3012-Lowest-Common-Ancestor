from BinaryTree import is_valid_node, Node


def lca(node, a, b):
    if is_valid_node(bst, a) and is_valid_node(bst, b):
        while node:
            if a < node.value < b:
                return node.value
            elif a == node.value:
                return a
            elif b == node.value:
                return b
            elif min(a, b) < node.value:
                node = node.left
            elif max(a, b) > node.value:
                node = node.right
    return None


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


if __name__ == '__main__':
    print(lca(bst, 10, 7))
