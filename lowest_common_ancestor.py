from collections import deque
from invert_binary_tree import Node, preorder_traversal


def lca(root, p, q):
    queue = deque() 
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node is p and (node.right is q or node.left is q):
            return node 
        elif node is q and (node.right is p or node.left is p):
            return node    
        elif (node.right is p and node.left is q) or (node.left is p and node.right is q):
            return node 
        
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)


def lowestCommonAncestor(root, p, q):
    # Base case: if the root is None, or if root is one of the nodes p or q
    if not root or root == p or root == q:
        return root

    # Search left and right subtrees for p and q
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both sides return non-None, the current root is the LCA
    if left and right:
        return root

    # Otherwise, return the side that is non-None
    return left if left else right


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    root.right.left = Node(0)
    root.right.right = Node(8)

    # preorder_traversal(root)
    p = root.left
    q = root.left.right.right
    ancestor = lca(root, p, q)
    print(ancestor.value)
