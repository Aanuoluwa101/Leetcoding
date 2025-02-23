"""
Write a function that reverses a string. 
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

def reverse(arr):
    start = 0 
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start] 
        start += 1
        end -= 1

    return arr 


arr = ["H","a","n","n","a","h"]
print(reverse(arr))
