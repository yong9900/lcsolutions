class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        if not root:
            return
        cur = root
        stack = []

        prev = TreeNode(-sys.maxsize)
        first = None
        second = None

        while (stack or cur):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                item = stack.pop()
                if item.val < prev.val:
                    if not first:
                        first = prev
                    second = item
                prev = item
                cur = item.right

        tmp = first.val
        first.val = second.val
        second.val = tmp                
