#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (40.77%)
# Total Accepted:    201.5K
# Total Submissions: 494.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = [root]
        res = []
        
        while q:
            new_q = []
            level = []
            for node in q:
                level.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            res.append(level)
            q = new_q
        
        for i, lst in enumerate(res):
            if i%2 == 1:
                lst.reverse()
        
        return res

