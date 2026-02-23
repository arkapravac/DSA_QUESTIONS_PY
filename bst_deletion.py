from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def remove_deepest(root, d_node):
    q = deque([root])
    while q:
        temp = q.popleft()
        if temp is d_node:
            return None
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def delete_node(root, key):
    if not root:
        return None
    if not root.left and not root.right:
        return None if root.data == key else root
        
    q = deque([root])
    key_node = None
    last_node = None
    while q:
        last_node = q.popleft()
        if last_node.data == key:
            key_node = last_node
        if last_node.left:
            q.append(last_node.left)
        if last_node.right:
            q.append(last_node.right)
            
    if key_node:
        deepest_val = last_node.data
        remove_deepest(root, last_node)
        key_node.data = deepest_val
    return root

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

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

print("Before:", end=" ")
level_order(root)

x = int(input("\nEnter element to delete: "))
root = delete_node(root, x)

print("After:", end=" ")
level_order(root)
