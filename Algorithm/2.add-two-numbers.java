/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (30.76%)
 * Total Accepted:    816.8K
 * Total Submissions: 2.6M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * Example:
 * 
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = new ListNode(0);
        ListNode p = head;
        while(l1 != null || l2 != null || carry != 0){
            int val  = carry;
            val += (l1 == null)? 0 : l1.val;
            val += (l2 == null)? 0 : l2.val;
            p.next = new ListNode(val%10);
            p = p.next;
            carry = val/10;
            
            l1 = (l1 != null)?l1.next : null;
            l2 = (l2 != null)?l2.next : null;
        }
        return head.next;
    }
}

