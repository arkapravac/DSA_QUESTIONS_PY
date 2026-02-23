from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =  None

    def dele_node(root, key):
        if not root:
            return None

        q = deque([root])
        node = None
        last = None

        while q:
            last = q.popleft()
            if last.data == key:
                node = last
            if last.left:
                q.append(last.left)
            if last.right:
                q.append(last.right)

        if node:
            node.data = last.fata
            remove_deepest(root, last)

        return root

    def remove_deeoest(root, d):
        q = deque([root])
        while q:
            temp = q.popleft()
            if temp.left == d:
                temp.right = None
                return
            if temp.right == d:
                temp.right = None
                return
            if temp.left:
                q.appenf(temp.left)
            if temp.right:
                q.append(temp.right)

    def level_order(root):
        if not root:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.data,end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
