#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_p1, pre_p2, in_p1, in_p2):
            if pre_p1 > pre_p2:
                return None
            pre_root = pre_p1
            in_root = index[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            size_left = in_root - in_p1
            root.left = helper(pre_root + 1, pre_root + size_left, in_p1, in_root - 1)
            root.right = helper(pre_root + size_left + 1, pre_p2, in_root + 1, in_p2)
            return root
            

        n = len(preorder)
        index = {val: index for index, val in enumerate(inorder)}
        return helper(0, n - 1, 0, n - 1)
        
# @lc code=end

