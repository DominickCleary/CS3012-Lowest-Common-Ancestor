from BinaryTree import bst_root


# def lca(root, a, b):
#     if not root:
#         return None
#     if root.value == a or root.value == b:
#         return root
#     left = lca(root.left, a, b)
#     right = lca(root.right, a, b)
#     if left and right:
#         return root
#     else:
#         return right if right else left


# def lca_parent(node_a, node_b):
#     height_a = get_height(node_a)
#     height_b = get_height(node_b)
#     if height_b > height_a:
#         node_a, node_b = node_b, node_a
#     for _ in range(height_b - height_a):
#         node_b = node_b.parent
#     while node_a != node_b:
#         node_a = node_a.parent
#         node_b = node_b.parent
#     return node_a
#
#
# def get_height(node):
#     height = 0
#     while node:
#         node = node.parent
#         height += 1
#     return height


def lca_bst(root, a, b):
    while root:
        if a <= root.value <= b:
            return root
        elif min(a, b) < root.value:
            root = root.left
        elif max(a, b) > root.value:
            root = root.right
    return None


if __name__ == '__main__':
    print(lca_bst(bst_root, 5, 4))
    # print(lca_bst(bst_root, 49, 19))
