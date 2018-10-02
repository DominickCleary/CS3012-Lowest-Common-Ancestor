from BinaryTree import bst_root


def lca_bst(root, a, b):
    while root:
        if a < root.value < b:
            return root.value
        elif a == root.value:
            return a
        elif b == root.value:
            return b
        elif min(a, b) < root.value:
            root = root.left
        elif max(a, b) > root.value:
            root = root.right
    return None


if __name__ == '__main__':
    # print(lca_bst(bst_root, 5, 4))
    print(lca_bst(bst_root, 49, 19))
