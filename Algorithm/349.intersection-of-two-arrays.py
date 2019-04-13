#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (53.37%)
# Total Accepted:    208.7K
# Total Submissions: 387.5K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        
        p1, p2 = 0, 0 
        result = []
        
        while p1 < len(nums1) and p2 < len(nums2):
            while 0 < p1 < len(nums1) and nums1[p1] == nums1[p1-1]:
                p1 += 1
            while 0 < p2 < len(nums2) and nums2[p2] == nums2[p2-1]:
                p2 += 1
                
            if p1 >= len(nums1) or p2 >= len(nums2):
                break
                
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return result

