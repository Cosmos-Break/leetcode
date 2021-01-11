#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0
        j = 0
        n = len(s)
        for i in range(n):
            if i != 0:
                window.remove(s[i-1])
            while j < n and s[j] not in window:
                window.add(s[j])
                j += 1
            max_len = max(max_len, len(window))
        return max_len


# @lc code=end
# s = Solution()
# print(s.lengthOfLongestSubstring("pwwkew"))
# 滑动窗口, 左右指针, 遍历左指针 找到最长的j
# 如果当前i>0 表示要进入下一个循环, 在window中删除i-1位置的词.