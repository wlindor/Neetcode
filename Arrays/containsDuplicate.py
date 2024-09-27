"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

def has_duplicate(nums: list[int]) -> bool:
    # edge case
    if not nums:
        return False
    
    hash_set = set()

    for num in nums:
        if num in hash_set:
            return True
        hash_set.add(num)
    return False

print(has_duplicate([1,2,3,4,5])) #False
print(has_duplicate([1,2,3,3,5])) #True
print(has_duplicate([1])) #False
print(has_duplicate([2,2])) #True
print(has_duplicate([])) #False
