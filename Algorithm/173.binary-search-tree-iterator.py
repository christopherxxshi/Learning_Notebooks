#
# @lc app=leetcode id=173 lang=python
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (47.50%)
# Total Accepted:    195.9K
# Total Submissions: 409K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.root = root
        node = root
        while node is not None:
            self.stack.append(node)
            node = node.left
        
            

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack[-1]
        if node.right != None:
            p = node.right
            while p is not None:
                self.stack.append(p)
                p = p.left
        else:
            p = self.stack.pop()
            while self.stack and p == self.stack[-1].right:
                p =  self.stack.pop()
        
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return  len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

