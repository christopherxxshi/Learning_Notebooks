#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (28.70%)
# Total Accepted:    196.2K
# Total Submissions: 682.7K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxm = nums[:]
        minm = nums[:]
        result = nums[0]
        
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num > 0:
                maxm[i] = max(maxm[i], maxm[i-1]*num)
                minm[i] = min(minm[i], minm[i-1]*num)
            elif num < 0:
                maxm[i] = max(maxm[i], minm[i-1]*num)
                minm[i] = min(minm[i], maxm[i-1]*num)
                
            result = max(result, maxm[i])
        
        return result

