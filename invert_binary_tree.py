"""
Given the root of a binary tree, invert the tree, and return its root.
Input: root = [4,2,7,1,3,6,9]   # preorder traversal
Output: [4,7,2,9,6,3,1]
"""


from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 



def preorder_traversal(root: Node):   # root-left-right
    if not root:
        return 
    
    queue = deque() 
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.value, end=", ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def inorder_traversal(root: Node):
    if not root:
        return 

    if root.left:
        inorder_traversal(root.left)
    
    print(root.value, end=", ")

    if root.right:
        inorder_traversal(root.right)

def postorder_traversal(root: Node):
    if not root:
        return 
    if root.left:
        postorder_traversal(root.left)
    if root.right:
        postorder_traversal(root.right)
    print(root.value, end=", ")


def invert(root: Node):
    if not root:
        return root 
    
    root.left, root.right = root.right, root.left
    if root.left:
        invert(root.left)
    if root.right:
        invert(root.right)
    return root        


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)

    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right.left = Node(6)
    root.right.right = Node(9)

    preorder_traversal(root)
    # print()
    # root = invert(root)
    # preorder_traversal(root)

    # root2 = Node(2)
    # root2.left = Node(1)
    # root2.right = Node(3)

    # print()
    # preorder_traversal(root2)
    # print()
    # root2 = invert(root2)
    # preorder_traversal(root2)

    # root3 = None 
    # root3 = invert(root3)
    # print() 
    # preorder_traversal(root3)

    
