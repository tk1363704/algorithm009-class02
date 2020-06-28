# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 示例 1:
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".

# 示例 2:
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 注意:
# 输入的字符串长度不会超过1000。

# "回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。
class Solution:
    # # Extending sub-strings from the center to the two sides
    # def countSubstrings(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     length = len(s)
    #     count = 0
    #     # Note: why is 2*len-1?
    #     # For 'ab', we have three centers as: a, ab, b. The range for center should be: 0 ≤ center < 3.
    #     # For 'abc', we have centers: a, ab, b, bc, c. The range is: 0 ≤ center < 5.
    #     for center in range(2*length-1):
    #         left = center // 2
    #         # If center % 2 == 0, then the string is a character at the beginning.
    #         # Otherwise the string has two same characters at the first place.
    #         right = left + center % 2
    #         while left >= 0 and right < length and s[left] == s[right]:
    #             count += 1
    #             left -= 1
    #             right += 1
    #     return count

    # Dynammic programming.
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        dp = [[False for i in range(length)] for i in range(length)]
        count = length
        for i in range(length):
            dp[i][i] = True
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    # Consider the situation that i and j are neighbours.
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    count += 1
        return count