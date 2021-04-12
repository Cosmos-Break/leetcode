# @before-stub-for-debug-begin
from python3problem872 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = []
        leaf2 = []
        def dfs(node, leaf):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
                return
            dfs(node.left, leaf)
            dfs(node.right, leaf)
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2
# @lc code=end

