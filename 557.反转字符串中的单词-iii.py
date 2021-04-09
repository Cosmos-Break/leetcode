#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        for i in range(len(str_list)):
            str_list[i] = str_list[i][::-1]
        return ' '.join(str_list)
# @lc code=end

