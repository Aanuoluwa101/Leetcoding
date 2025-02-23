"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

def binary_search(nums, target):
    if not nums:
        return -1

    start = 0 
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return - 1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]   
    target = 9

    print(binary_search(nums, target))