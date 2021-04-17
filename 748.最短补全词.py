#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lic = [i.lower() for i in licensePlate if i.isalpha()]
        d = Counter(lic)
        words.sort(key=len)
        for word in words:
            if not d - Counter(word):
                return word


# @lc code=end

