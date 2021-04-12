#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution(object):
    def toGoatLatin(self, S):

        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(word) + 'a' * i
                        for i, word in enumerate(S.split(), 1))

# @lc code=end

