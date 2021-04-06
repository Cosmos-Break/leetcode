#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())

# @lc code=end

