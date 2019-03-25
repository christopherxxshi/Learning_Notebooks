#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.46%)
# Total Accepted:    340.4K
# Total Submissions: 661K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        result = []
        self.helper(nums, 0, [], result)
        return result
    
    def helper(self, nums, idx, curset, result):
        if idx >= len(nums):
            result.append(curset[:])
            return
        
        self.helper(nums, idx+1, curset, result)
        curset.append(nums[idx])
        self.helper(nums, idx+1, curset, result)
        curset.pop()
        return 

