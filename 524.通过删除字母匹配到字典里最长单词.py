#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# from typing import List
# @lc code=start
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ret = ""
        for word in d:
            index = -1
            start = 0
            i = 0
            while i < len(word):
                char = word[i]
                index = s.find(char, start)
                if index == -1:
                    break
                start = index + 1
                i += 1
            if i == len(word):
                if len(word) > len(ret):
                    ret = word
                elif len(word) == len(ret):
                    if word < ret:
                        ret = word
        return ret
            
# @lc code=end
# s = Solution()
# s.findLongestWord("aaa", ["aaa","aa","a"])

