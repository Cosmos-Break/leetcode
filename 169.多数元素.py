#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dic = {}
        for num in nums:
            if num not in count_dic:
                count_dic[num] = 0
            else:
                count_dic[num] += 1
        max_value, max_count = list(count_dic.items())[0]
        for value, count in count_dic.items():
            if count > max_count:
                max_count = count
                max_value = value
        return max_value
# @lc code=end

