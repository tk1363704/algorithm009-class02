# 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

class Solution:
    @staticmethod
    def findIndex(nums):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        low = 0
        high = len(nums) - 1
        while nums[low] >= nums[high]:
            if high - low == 1:
                return low if nums[low] <= nums[high] else high
            mid = low + (high - low) // 2
            if nums[low] == nums[mid] and nums[low] == nums[high]:
                return Solution.find_in_sequence(nums[low: high + 1])
            elif nums[low] <= nums[mid]:
                low = mid
            elif nums[low] > nums[mid]:
                high = mid
        return 0

    @staticmethod
    def find_in_sequence(nums):
        min_num = nums[0]
        min_index = 0
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_index = i
                min_num = nums[i]
        return min_index

if __name__=="__main__":
    test_list = [3, 4, 5, 1, 2]
    print('3:' + str(Solution.findIndex(test_list)))
    test_list = [3, 4, 5, 1, 1, 2]
    print('3:' + str(Solution.findIndex(test_list)))
    test_list = [3, 4, 5, 1, 2, 2]
    print('3:' + str(Solution.findIndex(test_list)))
    test_list = [4, 5, 6, 7, 0, 1, 2]
    print('4:' + str(Solution.findIndex(test_list)))
    test_list = [2]
    print('0:' + str(Solution.findIndex(test_list)))
    test_list = [1, 0, 1, 1, 1]
    print('1:' + str(Solution.findIndex(test_list)))
    test_list = [2, 3, 1, 2]
    print('2:' + str(Solution.findIndex(test_list)))
    test_list = [4, 5, 1, 2, 3]
    print('2:' + str(Solution.findIndex(test_list)))
    test_list = [3, 4, 1, 2, 2]
    print('2:' + str(Solution.findIndex(test_list)))
    test_list = [1, 2, 3, 4, 6]
    print('0:' + str(Solution.findIndex(test_list)))
    test_list = [1, 1, 1, 1, 1]
    print('0:' + str(Solution.findIndex(test_list)))
