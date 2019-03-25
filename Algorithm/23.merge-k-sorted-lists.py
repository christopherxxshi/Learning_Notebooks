#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (33.37%)
# Total Accepted:    355.3K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        head = ListNode(None)
        p = head
        
        minheap = []
        
        for lst in lists:
            if not lst:
                continue
            heapq.heappush(minheap, (lst.val, lst))
        
        while minheap:
            val, node = heapq.heappop(minheap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, node.next))
        
        return head.next
        

