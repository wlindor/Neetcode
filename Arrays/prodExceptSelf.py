"""
Products of Array Discluding Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Follow-up: Could you solve it in 
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

def prod_except_self(nums):
    prod_array = [1] * len(nums)
    prod = 1

    for i in range(len(nums)):
        prod_array[i] *= prod
        prod *= nums[i]

    prod = 1

    for i in range(len(nums)-1, -1, -1):
        prod_array[i] *= prod
        prod *= nums[i]

    return prod_array

print(prod_except_self([1,2,4,6])) #[48, 24, 12, 8]¸
print(prod_except_self([-1,0,1,2,3])) #[0,-6,0,0,0]
