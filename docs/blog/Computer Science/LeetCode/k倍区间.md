---
typora-copy-images-to: upload
---

# k 倍区间

**题目描述**

给定一个长度为 $N$ 的数列，$A_1, A_2, \cdots A_N$，如果其中一段连续的子序列 $A_i, A_i + 1, \cdots A_j \ (i \leq j)$ 之和是 $K$ 的倍数，我们就称这个区间 $[i, j]$ 是 $K$ 倍区间。

你能求出数列中总共有多少个 $K$ 倍区间吗？

**输入描述**

第一行包含两个整数 $N$ 和 $K (1 \leq N, K \leq 10^5)$。

以下 $N$ 行每行包含一个整数 $A_i \ (1 \leq A_i \leq 10^5)$

**输出描述**

输出一个整数，代表 $K$ 倍区间的数目。

**输入输出样例**

示例输入

```
5 2
1
2
3
4
5
```

输出

```
6
```

**运行限制**

- 最大运行时间：2s
- 最大运行内存: 256M

### 关键思路：

1. **前缀和数组**：`PrefixSum[i]` 表示数组前 i 个元素的和。连续子序列 `A[j..i]` 的和可以表示为 `PrefixSum[i] - PrefixSum[j-1]`。
2. **模运算性质**：如果 `(PrefixSum[i] - PrefixSum[j]) % K == 0`，那么 `PrefixSum[i] % K == PrefixSum[j] % K`。也就是说，两个前缀和对 K 取模的结果相同，那么它们之间的子序列和一定能被 K 整除。
3. **哈希表记录余数**：我们使用一个哈希表 `remainderCount` 来记录之前出现过某个余数的次数。这样，当我们计算当前前缀和的余数时，可以直接查找哈希表，看之前有多少次相同的余数出现，从而知道有多少个有效的子序列。

```cpp
#include <iostream>  
#include <vector>  
#include <unordered_map>  
using namespace std;  

int main() {  
    int N, K;  
    cin >> N >> K;  
    
    vector<long long> PrefixSum(N + 1, 0);  
    long long cnt = 0;  
    // 记录每个长度的连续子序列的和对K的余数
    unordered_map<long long, long long> remainderCount;  
    
    remainderCount[0] = 1;  // 初始化余数0出现1次  
    
    for (int i = 1; i <= N; i++) {  
        int x;  
        cin >> x;  
        
        // 计算前缀和  通过一次遍历就可以实现所有长度的连续子序列的和
        PrefixSum[i] = PrefixSum[i-1] + x;  
        
        // 计算当前前缀和的余数  
        long long remainder = ((PrefixSum[i] % K) + K) % K;  // 确保余数为非负数
        
        // 查找之前是否有相同余数的前缀和  
        cnt += remainderCount[remainder];  // 模运算性质
        
        // 更新当前余数的计数  
        remainderCount[remainder]++;  // 同一个余数第一次出现时不会增加cnt，只有第二次出现时才会cnt++
    }  
    
    cout << cnt << endl;  
    return 0;  
}  
```

1. 第一次出现 r 时：
   - `remainderCount[r]` 的初始值为 0（假设之前没有出现过）。
   - `cnt += 0`（因为还没有其他相同余数的前缀和可以配对）。
   - `remainderCount[r]` 更新为 1。
2. 第二次出现 r 时：
   - `remainderCount[r]` 的值为 1。
   - `cnt += 1`（表示当前前缀和可以和之前 1 个相同余数的前缀和配对，形成 1 个新的满足条件的子序列）。
   - `remainderCount[r]` 更新为 2。
3. 第三次出现 r 时：
   - `remainderCount[r]` 的值为 2。
   - `cnt += 2`（表示当前前缀和可以和之前 2 个相同余数的前缀和配对，形成 2 个新的满足条件的子序列）。
   - `remainderCount[r]` 更新为 3。
