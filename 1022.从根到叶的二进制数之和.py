#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ret = []
        def dfs(node, path):
            if node:
                if not node.left and not node.right:
                    self.ret.append(path+str(node.val))
                dfs(node.left, path + str(node.val))
                dfs(node.right, path + str(node.val))
        dfs(root, "")
        ans = 0
        for i in self.ret:
            ans += int(i, 2)
        return ans
# @lc code=end

