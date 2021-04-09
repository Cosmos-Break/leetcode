#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt_dict = Counter(nums)
        dup = 0
        missing = 0
        for i in range(1, len(nums)+ 1):
            cnt = cnt_dict.get(i)
            if cnt == 2:
                dup = i
            elif cnt is None:
                missing = i
        return [dup, missing]
# @lc code=end

