"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""
from collections import Counter

def first_unique(string):
    counter = Counter(string)

    for idx, char in enumerate(string):
        if counter[char] == 1:
            return idx 
    
    return -1

def first_unique_naive(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    for idx, value in enumerate(list(char_count.values())):
        if value == 1:
            return idx 
    return -1

print(first_unique_naive("loveleetcode"))