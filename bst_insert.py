from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def getHeight(root):
    if root is None:
        return -1
    return 1 + max(getHeight(root.left), getHeight(root.right))

def levelOrder(root):
    if not root:
        return
    
    queue = deque([(root, 0)])
    height = getHeight(root)
    lastLevel = 0
    
    while queue:
        node, lvl = queue.popleft()
        
        if lvl > lastLevel:
            print()
            lastLevel = lvl
            
        if lvl > height:
            break
            
        print("N" if node.data == -1 else node.data, end=" ")
        
        if node.data == -1:
            if lvl < height:
                queue.append((Node(-1), lvl + 1))
                queue.append((Node(-1), lvl + 1))
            continue

        if node.left:
            queue.append((node.left, lvl + 1))
        elif lvl < height:
            queue.append((Node(-1), lvl + 1))
            
        if node.right:
            queue.append((node.right, lvl + 1))
        elif lvl < height:
            queue.append((Node(-1), lvl + 1))

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root

root = None
for val in [22, 12, 30, 8, 20, 30, 15]:
    root = insert(root, val)

levelOrder(root)
