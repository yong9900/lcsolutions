def subtree(node):
    if not node:
        return []
    res = []
    if node.left:
        res.append(node.left.val)
        res += subtree(node.left)
    if node.right:
        res.append(node.right.val)
        res += subtree(node.right)
    return res

def printsubtree(root):
    if not root:
        return

    stack = []
    cur = root
    


