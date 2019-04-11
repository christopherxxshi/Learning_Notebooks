#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (53.86%)
# Total Accepted:    358.7K
# Total Submissions: 660.8K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        self.helper(nums, 0, result)
        return result
    
    def helper(self, nums, idx, result):
        if idx >= len(nums) - 1:
            result.append(nums[:])
            return 
        
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.helper(nums, idx + 1, result)
            nums[i], nums[idx] = nums[idx], nums[i]
            
    def permute(self, nums):
        
        if not nums:
            return []
        result = []
        visited = {i:False for i in range(len(nums))}
        self.helper(nums, [], result, visited)
        return result
    
    def helper(self, nums, subset, result, visited):
        if len(nums) == len(subset):
            result.append(subset[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            subset.append(nums[i])
            visited[i] = True
            self.helper(nums, subset, result, visited)
            visited[i] = False
            subset.pop()
        

