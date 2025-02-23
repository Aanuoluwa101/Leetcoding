from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 


def max_depth(root: Node):
    q = deque()

    if not root:
        return 0 
    q.append(root)
    max_height =  1
    while q: 
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        if node.right or node.left:
            max_height += 1
    return max_height

root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(6)
root.right.right = Node(9)

print(max_depth(root))