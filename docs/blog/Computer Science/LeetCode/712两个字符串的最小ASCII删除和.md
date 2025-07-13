# [712. 两个字符串的最小 ASCII 删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/)

给定两个字符串 `s1` 和 `s2`，返回 ==使两个字符串相等所需删除字符的 **ASCII** 值的最小和== 。

**示例 1:**

```
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
```

**示例 2:**

```
输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
```

**提示:**

- `0 <= s1.length, s2.length <= 1000`
- `s1` 和 `s2` 由小写英文字母组成

### **解题思路：**

1. 使用动态规划（Dynamic Programming）方法解决
2. 创建一个二维 DP 数组，`dp[i][j]` 表示使 s1 的前 i 个字符和 s2 的前 j 个字符相等所需的最小 ASCII 删除和
3. 状态转移方程：
   - 如果 `s1[i-1] == s2[j-1]`，则 `dp[i][j] = dp[i-1][j-1]`
   - 否则，`dp[i][j] = min(dp[i-1][j] + ASCII(s1[i-1]), dp[i][j-1] + ASCII(s2[j-1]))`
4. 初始化边界条件：
   - 处理 s1 为空的情况：累加 s2 的 ASCII 值
   - 处理 s2 为空的情况：累加 s1 的 ASCII 值
5. 最终结果在 `dp[m][n]` 中

```cpp
class Solution {  
public:  
    int minimumDeleteSum(string s1, string s2) {  
        int m = s1.length(), n = s2.length();  
        
        // 创建DP数组，初始化为0  
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));  
        
        // 处理s1为空的情况：累加s2的ASCII值  
        for (int j = 1; j <= n; j++) {  
            dp[0][j] = dp[0][j-1] + s2[j-1];  
        }  
        
        // 处理s2为空的情况：累加s1的ASCII值  
        for (int i = 1; i <= m; i++) {  
            dp[i][0] = dp[i-1][0] + s1[i-1];  
        }  
        
        // 填充DP数组  
        for (int i = 1; i <= m; i++) {  
            for (int j = 1; j <= n; j++) {  
                if (s1[i-1] == s2[j-1]) {  
                    // 字符相同，不需要删除  
                    dp[i][j] = dp[i-1][j-1];  
                } else {  
                    // 选择删除s1或s2中的字符，取最小ASCII和  
                    dp[i][j] = min(dp[i-1][j] + s1[i-1], dp[i][j-1] + s2[j-1]);  
                }  
            }  
        }  
        
        // 返回最终结果  
        return dp[m][n];  
    }  
};	
```

