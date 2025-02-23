from collections import Counter


"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def valid_anagram(s, t):
    i = j = 0 
    letters = {}
    letters2 = {}
    while i < len(s) and j < len(t):
        letters[s[i]] = letters.get(s[i], 0) + 1 
        letters2[t[j]] = letters2.get(t[j], 0) + 1 

        i += 1 
        j += 1
    
    if i != j:
        return False
    
    for letter, count in letters.items():
        if count != letters2.get(letter):
            return False 
    return True 


def isAnagram(s: str, t: str) -> bool:
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False

    # Use Counter to count frequencies of characters in both strings
    return Counter(s) == Counter(t)



if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    print(valid_anagram(s, t))

    s = "rat"
    t = "cat"

    print(valid_anagram(s, t))
        # print(Counter(s))