# [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 *该数组中和为 `k` 的子数组的个数* 。

子数组是数组中元素的连续非空序列。

**示例 1：**

```
输入：nums = [1,1,1], k = 2
输出：2
```

**示例 2：**

```
输入：nums = [1,2,3], k = 3
输出：2 
```

**提示：**

-   `1 <= nums.length <= 2 * 104`
-   `-1000 <= nums[i] <= 1000`
-   `-107 <= k <= 107`

## 我的解法

有误，无法通过全部用例，仅用作记录和批判。基本思路是根据提示计算给定数组 `nums` 的前缀和数组，然后想到如果前缀和数组中存在两个元素，它们的差等于 `k`，则找到一个满足条件的子数组；如果数组 `nums` 中第一个元素刚好等于 `k`，也算作一个满足条件的子数组；（或者在前缀和数组中添加一个元素为 0 的首项，这样也可以把 `nums` 中第一个元素考虑在内）

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int result = 0; // 记录该数组中和为 k 的子数组的个数
        List<Integer> qianzhuihe = new ArrayList<>();
        qianzhuihe.add(nums[0]); // 初始化第一个前缀和
        if (nums[0] == k) {
            result++;
        }
        if(nums.length==1){
            return result;
        }
        // 计算前缀和
        for (int i = 1; i < nums.length; i++) {
            int currentSum = qianzhuihe.get(i - 1) + nums[i];
            qianzhuihe.add(currentSum);
        }
        // 遍历前缀和数组，计算满足条件的子数组
        for (int i = 0; i < qianzhuihe.size(); i++) {
            if(qianzhuihe.get(i)==k){
                result++;
            }
            for (int j = i + 1; j < qianzhuihe.size(); j++) {
                if (qianzhuihe.get(j) - qianzhuihe.get(i) == k) {
                    result++;
                }
            }
        }
        return result;
    }
}
```

<img src="../../../../../../software/Typora/images/image-20250903093650035.png" alt="image-20250903093650035" style="zoom: 67%;" />

1.  **前缀和计算问题**：在计算前缀和时，使用了 `qianzhuihe.get(i - 1) + nums[i]`，这本身是正确的，但在后续的遍历中，你只检查了 `qianzhuihe.get(j) - qianzhuihe.get(i) == k`，这会导致遗漏一些情况。
2.  **时间复杂度问题**：算法使用了双重循环遍历前缀和数组，时间复杂度为 `O(n^2)`，这在最坏情况下会导致超时，尤其是当 `nums.length` 接近 `2 * 10^4` 时。

## 正确思路

1.  **初始化**：创建一个哈希表 `prefixSumCount`，用于存储前缀和及其出现的次数。初始化 `prefixSumCount.put(0, 1)`，表示前缀和为 `0` 的情况出现了 `1` 次。
2.  **遍历数组**：遍历数组 `nums`，计算当前的前缀和 `currentSum`。
3.  **统计符合条件的子数组**：检查 `currentSum - k` 是否在哈希表中。如果存在，说明存在一个子数组的和为 `k`，将对应的次数累加到 `result` 中。
4.  **更新哈希表**：将当前的前缀和 `currentSum` 存入哈希表，并更新其出现的次数。

核心在于用一个 hashmap 存储前缀和的值及其出现次数，这样只需要检查 `currentSum - k` 是否在哈希表中，如果在哈希表中，即存在两个前缀和元素，它们的差等于 k，就找到满足条件的子数组，`currentSum - k` 对应的出现次数，就是满足条件的子数组的个数，就可以累加到结果 `result` 中。

其实这里用 hashmap 来搜索 `currentSum - k` 是否在哈希表中，来搜索满足条件的子数组，将 $O(n^2)$ 复杂度优化到 $O(n)$，本质上和两数之和的思想是一样的，只不过前面嵌套了一个前缀和。

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int result = 0;
        int currentSum = 0;
        Map<Integer, Integer> prefixSumCount = new HashMap<>();
        prefixSumCount.put(0, 1); // 初始化前缀和为0的情况

        for (int num : nums) {
            currentSum += num;
            // 如果存在前缀和为 currentSum - k，说明存在子数组和为 k
            if (prefixSumCount.containsKey(currentSum - k)) {
                result += prefixSumCount.get(currentSum - k);
            }
            // 更新当前前缀和的出现次数
            prefixSumCount.put(currentSum, prefixSumCount.getOrDefault(currentSum, 0) + 1);
        }

        return result;
    }
}
```

