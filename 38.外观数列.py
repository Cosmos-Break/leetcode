#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start


class Solution:
    def say(self, string):
        count_list = []
        num_list = []
        from itertools import groupby
        for k, v in groupby(string):
            num_list.append(k)
            count_list.append(len(list(v)))
        result = ''
        for count, num in zip(count_list, num_list):
            result += str(count) + str(num)
        return result


    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            return self.say(self.countAndSay(n - 1))
# @lc code=end
# if __name__ == "__main__":
#     s = Solution()
#     print(s.countAndSay(6))
#     a = [1, 2, 3, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 3, 1, 1, 2, 1]
#     # a.sort()
#     from itertools import groupby
#     items, counts = [], []
#     for k, v in groupby(a):
#         items.append(k)
#         counts.append(len(list(v)))
#     print(counts)
#     print(items)
    
