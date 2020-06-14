# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
    # # My solution.
    # def findMin(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     low = 0
    #     high = len(nums) - 1
    #     while nums[low] >= nums[high]:
    #         if high - low == 1:
    #             return nums[high] if nums[high] <= nums[low] else nums[low]
    #         mid = low + (high - low) // 2
    #         if nums[low] <= nums[mid]:
    #             low = mid
    #         else:
    #             high = mid
    #     return nums[low]

    # Updated solution.
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]