from BinaryTree import bst, is_valid_node


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


if __name__ == '__main__':
    print(lca(bst, 10, 7))
