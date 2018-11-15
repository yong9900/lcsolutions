# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        
        level = 0
        stack=[root]
        while stack:
            result.append(list(map(lambda n: n.val, stack)))
            temp = []
            while stack:
                p = stack.pop()
                if level % 2:
                    if p.left:
                        temp.append(p.left)
                    if p.right:
                        temp.append(p.right)
                else:
                    if p.right:
                        temp.append(p.right)
                    if p.left:
                        temp.append(p.left)
            stack=temp
            level += 1

        return result