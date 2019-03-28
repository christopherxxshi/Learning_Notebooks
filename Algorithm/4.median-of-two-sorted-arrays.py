#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.41%)
# Total Accepted:    379K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1) + len(nums2)
        if k % 2 != 0:
            return self.helper(nums1, 0, nums2, 0, k/2 + 1 )
        else:
            a = self.helper(nums1, 0, nums2, 0, k/2 )
            b = self.helper(nums1, 0, nums2, 0, k/2 + 1 )
            return (a + b) * 1.0 / 2
    
    def helper(self, nums1, idx1, nums2, idx2, k):
        if idx1 >= len(nums1):
            return nums2[idx2 + k - 1]
        if idx2 >= len(nums2):
            return nums1[idx1 + k - 1]
        
        if k == 1:
            return min(nums1[idx1], nums2[idx2])
        
        a = nums1[idx1 + k/2 - 1] if idx1 + k/2 <= len(nums1) else None
        b = nums2[idx2 + k/2 - 1] if idx2 + k/2 <= len(nums2) else None
        
        if b is None or (a is not None and a < b):
            return self.helper(nums1, idx1 + k/2, nums2, idx2, k - k/2)
        return self.helper(nums1, idx1, nums2, idx2 + k/2, k - k/2)

