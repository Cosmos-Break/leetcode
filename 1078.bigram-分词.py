#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        word_lst = text.split()
        res = []
        for i in range(1,len(word_lst)):
            if word_lst[i-1] == first  and word_lst[i] == second and i+1<len(word_lst):
                res.append(word_lst[i+1])
        
        return res

# @lc code=end

