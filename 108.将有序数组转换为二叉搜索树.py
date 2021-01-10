#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums) - 1)
        
        
# @lc code=end
# 一个有序数组转化为一个二叉搜索树/平衡二叉树
# 子函数可以叫helper
# 取数组中间的值, 造一个节点当做root, 数组分为左数组和右数组,
# 递归下去, 左数组构造一个二叉搜索树, 右数组构造一个二叉搜索树,
# 分别接到root节点的左边和右边
# 终止条件:当left>right时