#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
        return res

# @lc code=end

