#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = dict(collections.Counter(ransomNote))
        for k, v in a.items():
            if magazine.count(k) < v:
                return False
        return True


# @lc code=end

