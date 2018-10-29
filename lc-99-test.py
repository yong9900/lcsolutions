class Solution:
    def recoverTree(self, root):
        swap1 = swap2 = smaller = None
        while root:
            if not root.left:
                # same code before pop up a node
                if smaller and smaller.val >= root.val:
                    if not swap1:
                        # swap 1 is the one that suppose to be small
                        # but actually big
                        # it's the one swap forward
                        swap1 = smaller

                    #swap2 is the one suppose to be big
                    #but actually small
                    #it's the one swap backward
                    swap2 = root
                smaller = root
                root = root.right
            else:
                # when has left, link the last node on the left side
                # to the parent node, then start from left to 
                # repeat the logic
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    # same code before pop up a node
                    if smaller and smaller.val >= root.val:
                        if not swap1:
                            swap1 = smaller
                        swap2 = root
                    smaller = root
                    root = root.right
        if swap1:
            swap1.val, swap2.val = swap2.val, swap1.val


