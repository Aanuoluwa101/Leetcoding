def is_balanced(root):
    def check_height(root):
        if not root:
            return 0 
           
        left_height = check_height(root.left)
        if left_height == -1:
            return -1 
        
        right_height = check_height(root.right)
        if right_height == -1:
            return -1 
        
        if abs(left_height - right_height) > 1:
            return -1 
        
        return max(left_height, right_height) + 1
    
    return check_height(root) != -1
        
        