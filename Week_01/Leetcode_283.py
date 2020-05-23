# 283. Move Zeroes.
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# My solution: using two pointers, i.e., fast pointer and slow pointer to traverse the array.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # My method: using fast pointer and slow pointer to remove zeroes.
        # i = 0
        # for num in nums:
        #     if num != 0:
        #         nums[i] = num
        #         i += 1
        # for j in range(i,len(nums)):
        #     nums[j] = 0

        # Optimal method: swapping.
        slow_p = 0
        for fast_p in range(len(nums)):
            if nums[fast_p]!=0:
              # Swap a and b in python.
              nums[slow_p], nums[fast_p] = nums[fast_p], nums[slow_p]
              slow_p += 1