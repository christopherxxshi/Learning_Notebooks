#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (29.83%)
# Total Accepted:    216.3K
# Total Submissions: 724.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        up = left = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        dirs = 0
        result = []
        
        while up <= down and left <= right:
            if dirs == 0:
                for i in range(left, right + 1):
                    result.append(matrix[up][i])
                up += 1
            elif dirs == 1:
                for i in range(up, down + 1):
                    result.append(matrix[i][right])
                right -= 1
            elif dirs == 2:
                for i in range(right,  left - 1, -1):
                    result.append(matrix[down][i])
                down -= 1
            else:
                for i in range(down,  up - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            dirs = (dirs + 1)%4
            
        return result

