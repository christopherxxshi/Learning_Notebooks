#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.65%)
# Total Accepted:    162.1K
# Total Submissions: 583.5K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return True
        
        
        n = len(nums)
        if n == 1:
            return 0
        
        step = 0
        idx = 0
        
        while idx < n - 1:
            step += 1
            longest = 0
            if idx + nums[idx] >= n - 1:
                return step
            for i in range(idx + 1, idx + nums[idx] + 1):
                if nums[i] + i >= longest:
                    longest = nums[i] + i
                    idx = i
        return step
        

