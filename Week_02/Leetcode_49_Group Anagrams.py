# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 示例:
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
from collections import defaultdict

class Solution:
    # # My solution: using hash.
    # @staticmethod
    # def groupAnagrams(strs):
    #     token_hash = {}
    #     for temp_str in strs:
    #         # We could use sorted() to sort string directly.
    #         sort_token = ''.join(sorted(temp_str))
    #         # get() 函数返回指定键的值，如果值不在字典中返回默认值。
    #         # Note:append() has no return value!
    #         # token_hash[sorted_tokens] = token_hash[sorted_tokens].append(temp_str)
    #         # Note: [1, 2, 3] + [4, 5, 6] = [1,2,3,4,5,6]
    #         token_hash[sort_token] = token_hash.get(sort_token, []) + [temp_str]
    #     # Python 字典 values() 方法,以列表形式，返回字典中所有的值。
    #     return list(token_hash.values())

    # # Official solution: using collections.defaultdict(list).
    # @staticmethod
    # def groupAnagrams(strs):
    #     token_hash = defaultdict(list)
    #     for s in strs:
    #         # 注意，这里token_hash[s]可以直接进行赋值操作，并记录在字典中。
    #         token_hash[tuple(sorted(s))].append(s)
    #     return list(token_hash.values())

    # Official solution: using count of the characters as key.
    @staticmethod
    def groupAnagrams(strs):
        token_hash = defaultdict(list)
        for s in strs:
            count_list = [0] * 26
            # ord(): 返回字符对应的 ASCII 数值，或者 Unicode 数值。
            for i in range(len(s)):
                count_list[ord(s[i]) - ord('a')] += 1
            token_hash[tuple(count_list)].append(s)
        return list(token_hash.values())

if __name__=="__main__":
    print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))