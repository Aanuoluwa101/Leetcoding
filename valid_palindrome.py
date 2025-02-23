"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


def is_palindrome(s: str) -> bool:
    start = 0 
    end = len(s) - 1 

    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1 
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1 
            end -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama" #true
    s = "hannah" # true
    s = "race a car" # false
    s = " " # true
    print(is_palindrome(s))