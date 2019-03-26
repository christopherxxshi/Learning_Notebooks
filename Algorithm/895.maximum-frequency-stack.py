#
# @lc app=leetcode id=895 lang=python
#
# [895] Maximum Frequency Stack
#
# https://leetcode.com/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (53.23%)
# Total Accepted:    9.1K
# Total Submissions: 17.1K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# Implement FreqStack, a class which simulates the operation of a stack-like
# data structure.
# 
# FreqStack has two functions:
# 
# 
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the
# stack.
# 
# If there is a tie for most frequent element, the element closest to the top
# of the stack is removed and returned.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to
# top.  Then:
# 
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
# 
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the
# top.
# The stack becomes [5,7,5,4].
# 
# pop() -> returns 5.
# The stack becomes [5,7,4].
# 
# pop() -> returns 4.
# The stack becomes [5,7].
# 
# 
# 
# 
# Note:
# 
# 
# Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
# It is guaranteed that FreqStack.pop() won't be called if the stack has zero
# elements.
# The total number of FreqStack.push calls will not exceed 10000 in a single
# test case.
# The total number of FreqStack.pop calls will not exceed 10000 in a single
# test case.
# The total number of FreqStack.push and FreqStack.pop calls will not exceed
# 150000 across all test cases.
# 
# 
# 
# 
# 
# 
#
import collections
class FreqStack(object):

    def __init__(self):
        self.cnts = collections.Counter()
        self.stack = collections.defaultdict(list)
        self.maxf = 0
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.cnts[x] += 1
        self.stack[self.cnts[x]].append(x)
        self.maxf = max(self.maxf, self.cnts[x])

    def pop(self):
        """
        :rtype: int
        """
        val = self.stack[self.maxf].pop()
        if not self.stack[self.maxf]:
            self.maxf -= 1
        self.cnts[val] -= 1
        return val 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

