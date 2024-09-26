def removeDuplicates(nums):
    n = len(nums)
    insert_index = 1

    for right_index in range(1, n):
        if nums[right_index] != nums[right_index - 1]:
            nums[insert_index] = nums[right_index]
            insert_index += 1
            
    return insert_index

