"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def contains_duplicate(nums):
    unique = set()
    for element in nums:
        if element in unique:
            return True 
        unique.add(element)
    return False


if __name__ == "__main__":
    nums = [1,2,3,4] 
    print(contains_duplicate(nums))
