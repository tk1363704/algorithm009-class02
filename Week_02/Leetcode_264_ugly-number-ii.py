# 面试题49. 丑数
# 我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
# 示例:
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  
# 1 是丑数。
# n 不超过1690。
# 本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/

from queue import PriorityQueue
class Solution:
    # @staticmethod
    # # PriorityQueue: very slow
    # def nthUglyNumber(n):
    #     if n == 1:
    #         return 1
    #     output_list = []
    #     q = PriorityQueue()
    #     q.put(1)
    #     value_set = set()
    #     while len(output_list) < n:
    #         current_value = q.get()
    #         if current_value not in value_set:
    #             q.put(current_value * 2)
    #             q.put(current_value * 3)
    #             q.put(current_value * 5)
    #             output_list.append(current_value)
    #             value_set.add(current_value)
    #     return output_list[-1]

    @staticmethod
    # Three pointers & dynamic programming: very fast.
    def nthUglyNumber(n):
        if n == 1:
            return 1
        output_list = [1] * n
        index_2 = index_3 = index_5 = 0
        i = 1
        while i < n:
            value_multiply_2 = output_list[index_2] * 2
            value_multiply_3 = output_list[index_3] * 3
            value_multiply_5 = output_list[index_5] * 5
            min_value = min(value_multiply_2, value_multiply_3, value_multiply_5)
            output_list[i] = min_value
            i += 1
            if min_value == value_multiply_2:
                index_2 += 1
            # Using if nut bot elif to make the same value_multiply (2*3 and 3*2) move forward simutaneously.
            if min_value == value_multiply_3:
                index_3 += 1
            if min_value == value_multiply_5:
                index_5 += 1
        return output_list[-1]

if __name__ == "__main__":
    print(Solution.nthUglyNumber(111))
