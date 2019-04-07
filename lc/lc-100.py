class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
                return False
        if not self.isSameTree(p.right, q.right):
                return False
        return True
        