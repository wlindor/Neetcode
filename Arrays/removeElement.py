"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

def remove_element(nums, val):
    n = len(nums)
    insert_index = 0 

    for index in range(n):
        if nums[index] != val:
            nums[insert_index] = nums[index]
            insert_index += 1
    return insert_index

# Test Case 1:
print(remove_element([3, 2, 2, 3], 3))  # Expected: 2

# Test Case 2:
print(remove_element([1, 2, 3, 4, 5], 6))  # Expected: 5

# Test Case 3:
print(remove_element([2, 2, 2, 2], 2))  # Expected: 0

# Test Case 4:
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Expected: 5

# Test Case 5:
print(remove_element([], 0))  # Expected: 0

# Test Case 6:
print(remove_element([5], 1))  # Expected: 1

# Test Case 7:
print(remove_element([5], 5))  # Expected: 0

# Test Case 8:
print(remove_element([i % 2 for i in range(100)], 1))  # Expected: 50

