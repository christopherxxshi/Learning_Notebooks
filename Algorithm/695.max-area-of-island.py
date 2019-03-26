#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (56.29%)
# Total Accepted:    74.3K
# Total Submissions: 131.9K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# 
# Example 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# 
# Example 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# Note: The length of each dimension in the given grid does not exceed 50.
# 
#
import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        maxm = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                visited.add((i,j))
                maxm = max(maxm, self.bfs(grid, i, j, visited))
        
        return maxm
    
    def bfs(self, grid, x, y, visited):
        area = 1
        q = collections.deque([(x, y)])
        n, m = len(grid), len(grid[0])
        while q:
            cx, cy = q.popleft()
            for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    area += 1
                    q.append((nx, ny))
        return area

