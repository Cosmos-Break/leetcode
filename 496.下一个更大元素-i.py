#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashtable = {}
        for i in range(len(nums2)):
            while len(stack) != 0 and nums2[i] > stack[-1]:
                hashtable[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        ret = []
        for num in nums1:
            if num in hashtable:
                ret.append(hashtable[num])
            else:
                ret.append(-1)
        return ret
# @lc code=end

