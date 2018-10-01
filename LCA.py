from BinaryTree import BST


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


if __name__ == '__main__':
    print(lcaBST(BST, 1, 3))
    # print(lcaBST(BST, 9,16))



