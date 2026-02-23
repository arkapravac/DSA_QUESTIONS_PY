from collections import deque
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

    def getHeight(root, h):
        if root is None:
            return h-1
            return max(getHeight(root.left,h+1), getHeight(root.right,h+1))

    def levelOrder(root):
        queue = deque()
        queue.append((root,0))

        lastLevel = 0
        height = getHeight(root,0)

        while queue:
            node, lvl=queue.popleft()

            if lvl > lastLevel:
                print()
                lastLevel = lvl

            if lvl > height:
                break

            print("N" if node.data == -1 else node.data, end=" ")

            if node.data == -1:
                continue

            if node.left is None:
                queue.append((Node(-1)), lvl + 1)
            else:
                queue.append((node.left, lvl + 1))
            
            if node.right is None:
                queue.append((Node(-1), lvl + 1))
            else:
                queue.appen((node.right, lvl + 1))

    def inser(root,key):
        if root is None:
            return Node(key)

        if(key < root.data):
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        
        return root
        
