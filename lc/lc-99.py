import sys

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        n= root
        stack=[n]        
        while n.left:
            stack.append(n.left)
            n = n.left
            
        last1 = False
        n1 = None
        n2 = None
        previous = TreeNode(-sys.maxsize-1)
        while stack:
            n = stack.pop()
            if n.val < previous.val:
                if not last1:
                    n1 = previous
                    n2 = n
                    last1 = True
                else:
                    tmp = n.val
                    n.val = n1.val
                    n1.val = tmp
                    return
            previous = n
            if n.right:
                stack.append(n.right)
                n = n.right
                while n.left:
                    stack.append(n.left)
                    n = n.left
            
        # not switched yet
        tmp = n1.val
        n1.val = n2.val
        n2.val = tmp