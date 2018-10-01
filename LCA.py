from BinaryTree import Node, BST, root


# ## We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its
# parent. The parent would then test its left and right subtree if each contain one of the two nodes. If yes,
# then the parent must be the LCA and we pass its parent up to the root. If not, we pass the lower node which
# contains either one of the two nodes (if the left or right subtree contains either p or q), or NULL (if both the
# left and right subtree does not contain either p or q) up. O(n)
def lca(root, a, b):
    if not root: return None
    if root.value == a or root.value == b: return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left and right: return root
    else: return right if right else left


def lcaParent(root, nodeA, nodeB):
    heightA = getHeight(root, nodeA)
    heightB = getHeight(root, nodeB)
    if heightB > heightA:
        temp = nodeA
        nodeA = nodeB
        nodeB = temp
    for _ in range(heightB - heightA):
        nodeB = nodeB.parent
    while nodeA != nodeB:
        nodeA = nodeA.parent
        nodeB = nodeB.parent
    return nodeA


def getHeight(root, node):
    height = 0
    while node:
        node = node.parent
        height += 1
    return height


def lcaBST(root, a, b):
    while root:
        if a <= root.value <= b:
            return root
        elif min(a, b) < root.value:
            root = root.left
        elif max(a, b) > root.value:
            root = root.left
    return None