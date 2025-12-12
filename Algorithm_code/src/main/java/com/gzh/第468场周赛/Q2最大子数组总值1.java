package com.gzh.第468场周赛;

public class Q2最大子数组总值1 {
    public static long maxTotalValue(int[] nums, int k) {
        // int n = nums.length;
        // long max = 0;
        // for(int i=0;i<n-1;i++){
        //     for(int j=i+1;j<n;j++){
        //         max = Math.max(max, Math.abs(nums[i]-nums[j]));
        //     }
        // }
        // return k*max;

        int n = nums.length;
        long min_value = -1;  // 理论最小值
        long min = nums[0];    // 数组中的最小值
        long max_value = (long)(1e9) + 1;
        long max = nums[0];
        for(int i=0;i<n-1;i++){
            if((min-min_value)>=(nums[i+1]-min_value)){
                min = nums[i+1];
            }
            else{
                min = nums[i];
            }
            if((max_value-max)>=(max_value-nums[i+1])){
                max = nums[i+1];
            }
            else{
                max = nums[i];
            }
        }
        long range = max - min;
        return k*range;
    }
}
