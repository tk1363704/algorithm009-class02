学习笔记
===============

## 学习总结 
本周学习了BFS、DFS、贪心算法与二分查找。
其中，贪心算法是比较难的部分。

### 1. 贪心算法
贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。
也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。
贪心算法不是对所有问题都能得到整体最优解，关键是贪心策略的选择，选择的贪心策略必须具备无后效性，即某个状态以前的过程不会影响以后的状态，只与当前状态有关。

#### 思想
贪心算法的基本思路是从问题的某一个初始解出发一步一步地进行，根据某个优化测度，每一步都要确保能获得局部最优解。
每一步只考虑一个数据，他的选取应该满足局部优化的条件。
若下一个数据和部分最优解连在一起不再是可行解时，就不把该数据添加到部分解中，直到把所有数据枚举完，或者不能再添加算法停止。

#### 过程
- 建立数学模型来描述问题；
- 把求解的问题分成若干个子问题；
- 对每一子问题求解，得到子问题的局部最优解；
- 把子问题的解局部最优解合成原来解问题的一个解。

假设山洞中有 n 种宝物，每种宝物有一定重量 w 和相应的价值 v，毛驴运载能力有限，只能运走 m 重量的宝物，一种宝物只能拿一样，宝物可以分割。那么怎么才能使毛驴运走宝物的价值最大呢？
我们可以尝试贪心策略：
- 每次挑选价值最大的宝物装入背包，得到的结果是否最优？
- 每次挑选重量最小的宝物装入，能否得到最优解？
- 每次选取单位重量价值最大的宝物，能否使价值最高？

思考一下，如果选价值最大的宝物，但重量非常大，也是不行的，因为运载能力是有限的，所以第 1 种策略舍弃；如果选重量最小的物品装入，那么其价值不一定高，所以不能在总重限制的情况下保证价值最大，第 2 种策略舍弃；而第 3 种是每次选取单位重量价值最大的宝物，也就是说每次选择性价比（价值/重量）最高的宝物，如果可以达到运载重量 m，那么一定能得到价值最大。

因此采用第 3 种贪心策略，每次从剩下的宝物中选择性价比最高的宝物。

算法设计：
- 数据结构及初始化。将 n 种宝物的重量和价值存储在结构体 three（包含重量、价值、性价比 3 个成员）中，同时求出每种宝物的性价比也存储在对应的结构体 three 中，将其按照性价比从高到低排序。采用 sum 来存储毛驴能够运走的最大价值，初始化为 0。
- 根据贪心策略，按照性价比从大到小选取宝物，直到达到毛驴的运载能力。每次选择性价比高的物品，判断是否小于 m（毛驴运载能力），如果小于 m，则放入，sum（已放入物品的价值）加上当前宝物的价值，m 减去放入宝物的重量；如果不小于 m，则取该宝物的一部分 m * p[i]，m=0，程序结束。m 减少到 0，则 sum 得到最大值。

### 2. 二分查找算法题
使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方。
思想：
    有序，还要查找。
    找到这两个关键字，我们不免会想到我们的二分查找法，但这个数组旋转后已经不是一个真正的有序数组了，倒像是两个递增的数组组合而成的，我们可以这样思考。

　　我们可以设定两个下标 low 和 high，并设定 mid = （low + high）/2（写法一)(这里有一个小点需要注意，mid=low+（high-low）/2（写法二）,这个写法是更加合适的，因为在两个数都很大的情况下，low+high有存在数组越界的可能性，写法二则不会越界)，下面的代码中还是按照写法一进行编程的。替换成二的话更优。
　　
　　我们自然就可以找到数组中间的元素 array[mid]，如果中间的元素位于前面的递增数组，那么它应该大于或者等于 low 下标对应的元素，此时数组中最小的元素应该位于该元素的后面，我们可以把 low 下标指向该中间元素，这样可以缩小查找的范围。
　　同样，如果中间元素位于后面的递增子数组，那么它应该小于或者等于 high 下标对应的元素。此时该数组中最小的元素应该位于该中间元素的前面。我们就可以把 high 下标更新到中位数的下标，这样也可以缩小查找的范围，移动之后的 high 下标对应的元素仍然在后面的递增子数组中。

　　因为是有序数组的旋转，所以数组最后的元素一定不大于最初的元素。，所以我们的比较可以只选其中一个，代码中统一选择low所对应的元素进行比较。
　　不管是更新 low 还是 high，我们的查找范围都会缩小为原来的一半，接下来我们再用更新的下标去重复新一轮的查找。直到最后两个下标相邻，也就是我们的循环结束条件。

代码如下：
```
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
```