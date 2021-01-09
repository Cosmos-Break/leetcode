#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_list = s.split()
        if len(split_list) >= 1:
            return len(split_list[-1])
        else:
            return 0
            
# @lc code=end

