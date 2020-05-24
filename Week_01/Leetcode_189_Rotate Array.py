# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space? 
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
    # # My method: Iteratively append the first element in array to the end of the array.
    # def rotate(self, nums: List[int], k: int) -> None:
    #     for i in range(len(nums) - k % (len(nums))):
    #         q = nums.pop(0)
    #         nums.append(q)

    # # Find the expected location for each element.
    # def rotate(self, nums: List[int], k: int) -> None:
    #     length = len(nums)
    #     i , count = 0, 0
    #     k = k % length
    #     while count < length:
    #         current_index = i
    #         swap_value = nums[current_index]
    #         while True:
    #             next_index = (current_index + k) % length
    #             nums[next_index], swap_value = swap_value, nums[next_index]
    #             current_index = next_index
    #             count += 1
    #             if current_index == i:
    #                 break
    #         i += 1

    # Rotation.
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length
        # The operation [::-1] will return the reversed value, so we need to assign the value back to the nums list.
        nums[:] = nums[::-1]
        nums[:] = nums[-(length - k + 1)::-1] + nums[:-(length - k + 1):-1]
        # # The operation reverse has no return value, but reeverse the nums list itself.
        # nums.reverse()
        # a1 = nums[:k]
        # a1.reverse()
        # a2 = nums[k:]
        # a2.reverse()
        # nums[:] = a1 + a2
