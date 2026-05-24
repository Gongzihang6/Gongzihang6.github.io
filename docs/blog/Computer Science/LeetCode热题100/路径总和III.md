# [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)

给定一个二叉树的根节点 `root` ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 **路径** 的数目。

**路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。



**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

```
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
```

**示例 2：**

```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
```

 

**提示:**

-   二叉树的节点个数的范围是 `[0,1000]`
-   `-109 <= Node.val <= 109` 
-   `-1000 <= targetSum <= 1000` 

## 解法一

```cpp
/**
 * @brief 路径总和 III (LeetCode 437)
 * 
 * 作用：计算二叉树中节点值之和等于 targetSum 的向下路径的数目。
 * 
 * 功能实现了什么：
 * 将一维数组的“前缀和+哈希表”思想扩展到了二叉树的 DFS 遍历中。
 * 能够在 O(N) 的时间复杂度内解决问题，避免了传统暴力双重 DFS 带来的 O(N^2) 耗时。
 * 
 * 怎么实现的：
 * 1. 维护一个哈希表 prefix_map，用于记录【前缀和】及其【出现的次数】。
 * 2. 初始化 prefix_map[0] = 1，代表一条空路径，目的是为了处理恰好从根节点开始、和就等于 targetSum 的情况。
 * 3. 使用 DFS 遍历二叉树：
 *    a. 累加当前节点的值到 curr_sum（当前路径的前缀和）。
 *    b. 在哈希表中查找是否存在前缀和为 (curr_sum - targetSum) 的历史节点。
 *       如果存在，其对应的次数就是当前能拼凑出 targetSum 的路径数，累加到结果中。
 *    c. 将当前的 curr_sum 记录到哈希表中，次数 +1，供接下来的子节点去匹配。
 *    d. 继续递归处理左子树和右子树，将左右子树找到的满足条件的路径数累加。
 *    e. 【关键回溯】：当前节点的子树处理完毕，准备返回上一层去遍历其他分支时，
 *       必须将当前节点的 curr_sum 在哈希表中的次数减 1。因为这条路径不能与其他平行的分支共享。
 */
#include <unordered_map>

// Definition for a binary tree node.
/*
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
*/

class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        // key: 前缀和, value: 该前缀和出现的次数
        std::unordered_map<long long, int> prefix_map;
        
        // 初始化，前缀和为0的路径有一条
        prefix_map[0] = 1; 
        
        return dfs(root, 0, targetSum, prefix_map);
    }

private:
    int dfs(TreeNode* node, long long curr_sum, int targetSum, std::unordered_map<long long, int>& prefix_map) {
        if (!node) {
            return 0;
        }
        
        int res = 0;
        
        // 1. 更新当前路径的前缀和（注意题目节点值较大，这里 curr_sum 使用 long long 防溢出）
        curr_sum += node->val;
        
        // 2. 检查是否存在能够满足条件的历史前缀和
        if (prefix_map.count(curr_sum - targetSum)) {
            res += prefix_map[curr_sum - targetSum];
        }
        
        // 3. 将当前前缀和加入 map，供接下来的子树节点使用
        prefix_map[curr_sum]++;
        
        // 4. 继续 DFS 遍历左右子树
        res += dfs(node->left, curr_sum, targetSum, prefix_map);
        res += dfs(node->right, curr_sum, targetSum, prefix_map);
        
        // 5. 【回溯】恢复状态
        // 离开当前节点去往其他分支时，当前节点的前缀和必须撤销
        prefix_map[curr_sum]--;
        
        return res;
    }
};
```

