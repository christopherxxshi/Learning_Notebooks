#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (41.67%)
# Total Accepted:    192.5K
# Total Submissions: 461.7K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        nums.sort()
        result = []
        self.helper(nums, 0, [], result)
        return result
    
    def helper(self, nums, idx, curset, result):
        result.append(curset[:])
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            curset.append(nums[i])
            self.helper(nums, i+1, curset, result)
            curset.pop()
        return 
        
        

