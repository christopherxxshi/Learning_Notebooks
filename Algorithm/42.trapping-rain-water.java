/*
 * @lc app=leetcode id=42 lang=java
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (42.27%)
 * Total Accepted:    266.8K
 * Total Submissions: 631K
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it is able to trap after raining.
 * 
 * 
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water (blue section) are being trapped. Thanks
 * Marcos for contributing this image!
 * 
 * Example:
 * 
 * 
 * Input: [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * 
 */
class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }
        int i  = 0;
        int j = height.length - 1;
        int trappedWater = 0;
        int leftmax = 0, rightmax = 0;
        while(i <= j){
            if(leftmax < rightmax){
                if(leftmax < height[i]){
                    leftmax =  height[i];
                }else{
                    trappedWater += (leftmax - height[i]);
                }
                i++;
            }else{
                if(rightmax < height[j]){
                    rightmax =  height[j];
                }else{
                    trappedWater += (rightmax - height[j]);
                }
                j--;
            }
        }
        return trappedWater;
    }
}

