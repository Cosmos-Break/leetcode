# @before-stub-for-debug-begin
from python3problem113 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ret = []
        def dfs(node, path, target):
            if not node:
                return
            if node.val != target:
                path.append(node.val)
                dfs(node.left, list(path), target - node.val)
                dfs(node.right, list(path), target - node.val)
            else:
                if not node.left and not node.right:
                    path.append(node.val)
                    ret.append(list(path))
        
        dfs(root, [], target)
        return ret
# @lc code=end

