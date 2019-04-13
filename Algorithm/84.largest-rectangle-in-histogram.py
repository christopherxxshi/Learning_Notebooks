#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (30.47%)
# Total Accepted:    166.1K
# Total Submissions: 541.4K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        stack = [-1]
        self.maxm = 0
        heights.append(-1)
        for idx, h in enumerate(heights):
            if stack[-1] != -1 and heights[stack[-1]] > h:
                self.helper(heights, stack, idx, h)
            stack.append(idx)
        return self.maxm
        
    
    def helper(self, heights,stack, idx, h):
        while stack[-1] != -1:
            if heights[stack[-1]] <= h:
                break 
            curidx = stack.pop()
            curh = heights[curidx]
            length = idx - stack[-1] - 1
            self.maxm = max(self.maxm, curh*length)
        return 

