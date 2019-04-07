from collections import deque

class Node:
    def __init__(self, key, left=None, right=None):
        self.val = key
        self.left = left
        self.right = right

def printTree(root):
    queue = deque([root])
    while queue:
        item = queue.popleft()
        print(item.val, end='-')
        if item.left:
            queue.append(item.left)
        if item.right:
            queue.append(item.right)
    print()

def printTreeII(root):
    queue = [root]
    level = 1
    while queue:
        queue1=[]
        print( "level is: ", level)
        for item in queue:
            print(item.val, end="-")
            if item.left:
                queue1.append(item.left)
            if item.right:
                queue1.append(item.right)
        print()
        level += 1
        queue = queue1

a4 = Node(4)
a5 = Node(5)
a2 = Node(2, a4, a5)
a6 = Node(6)
a7 = Node(7)
a3 = Node(3, a6, a7)
a1 = Node(1, a2, a3)

printTree(a1)
printTreeII(a1)