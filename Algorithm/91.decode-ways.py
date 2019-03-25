#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (21.99%)
# Total Accepted:    244.2K
# Total Submissions: 1.1M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        f = [0] * (len(s) + 1)
        f[0] = 1
        
        for i in range(1, len(s)+1):
            if 0 < int(s[i-1]) <= 9:
                f[i] += f[i-1]
            if i > 1 and s[i-2] == '1':
                f[i] += f[i-2]
            if i > 1 and s[i-2] == '2' and 0 <= int(s[i-1]) <= 6:
                f[i] += f[i-2]
        return f[-1]
        

