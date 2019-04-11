#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (39.49%)
# Total Accepted:    231.6K
# Total Submissions: 582.2K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return  []
        
        result = []
        visited = {i: False for i in range(len(nums))}
        self.helper(sorted(nums), result, visited, [])
        return result
    
    def helper(self, nums, result, visited, subset):
        if len(subset) == len(nums):
            result.append(subset[:])
            return 
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            if i + 1 < len(nums) and nums[i] == nums[i+1] and visited[i+1]:
                continue
            
            visited[i] = True
            subset.append(nums[i])
            self.helper(nums, result, visited, subset)
            subset.pop()
            visited[i] = False

