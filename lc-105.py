# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preo, pstart, pend, ino, istart, iend):
            if pstart==pend:
                return None
            root = TreeNode(preo[pstart])
            if pstart+1 == pend:
                return root
        
            for i in range(0, iend-istart):
                if ino[istart+i]==root.val:
                    root.left=build(preo, pstart+1, pstart+i+1, ino, istart, istart+i)
                    root.right=build(preo, pstart+i+1, pend, ino, istart+i+1, iend)
                    return root

        return build(preorder, 0, len(preorder), inorder, 0, len(inorder))

class Better:
    def buildTree(self, preorder, inorder):
        if not preorder or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        preidx = 1
        inidx = 0
        stack=[root] 
        while preidx < len(preorder):
            prev=None
            while stack and stack[-1].val == inorder[inidx]:
                prev=stack.pop()
                inidx +=1
            node = TreeNode(preorder[preidx])
            preidx += 1    
            if prev:
                prev.right = node
            else:
                stack[-1].left = node
            stack.append(node)
        return root

class BetterRecursion:
    def buildTree(self, preorder, inorder):
        def build(inord):
            if not inord or not preorder:
                return None
            mid = inord.index(preorder.pop())
            root = TreeNode(inord[mid])
            root.left = build(inord[:mid])
            root.right = build(inord[mid+1:])
            return root
        preorder.reverse()
        return build(inorder)
            
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print (BetterRecursion().buildTree(preorder, inorder))