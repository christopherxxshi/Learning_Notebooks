#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (42.27%)
# Total Accepted:    266.8K
# Total Submissions: 631K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        lmax, rmax, cnt = 0, 0, 0
        
        while left <= right:
            if lmax < rmax:
                cnt += max(0, lmax - height[left])
                if lmax < height[left]:
                    lmax = height[left]
                left += 1
            else:
                cnt += max(0, rmax - height[right])
                if rmax < height[right]:
                    rmax = height[right]
                right -= 1
                
        return cnt
        

