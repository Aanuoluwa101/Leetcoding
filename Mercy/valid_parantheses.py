"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1: 
Input: s = "()[]{}"

Output: true

This solution uses a stack. 
"""


from collections import deque


# time complexity O(n)
def is_valid_parantheses(s):
    stack = deque()
    parantheses = {
    	"]": "[",
    	")": "(",
    	"}": "{"
    }
    for char in s:
        if char in parantheses.values():
            stack.appendleft(char) 
        else:
            if not stack or stack.popleft()!= parantheses[char]:
                return False
    return True


if __name__ == "__main__":
    s = "()[]{]"
    s = "(])"
    # s = "(]"
    print(is_valid_parantheses(s)) 
