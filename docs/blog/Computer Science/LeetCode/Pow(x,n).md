# [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/)

实现 [pow(*x*, *n*)](https://www.cplusplus.com/reference/valarray/pow/) ，即计算 `x` 的整数 `n` 次幂函数（即，`xn` ）。

**示例 1：**

```
输入：x = 2.00000, n = 10
输出：1024.00000
```

**示例 2：**

```
输入：x = 2.10000, n = 3
输出：9.26100
```

**示例 3：**

```
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
```



**提示：**

- `-100.0 < x < 100.0`
- `-231 <= n <= 231-1`
- `n` 是一个整数
- 要么 `x` 不为零，要么 `n > 0` 。
- `-104 <= xn <= 104`

思路：使用快速幂算法，

我的尝试：

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        long double res = 1.0;
        long long N = n;
        if (N > 0) {
            while (N > 0) {
                if (n & 1)
                    res = res * x;
                x = x * x;
                N >>= 1;
            }
        }
        if (N < 0) {
            return 1 / myPow(x, -N);
        }

        return res;
    }
};
```

没有通过，

输入 x = 2.00000，n = 10

输出，1.00000	预期结果 1024.0

### **方法一：快速幂递归实现**

以计算 2 的 10 次方为例，递归快速幂实现过程如下，调用 `fastPow(2,10)`，刚开始不满足递归终止条件，递归调用 `fastPow(2,5)` 函数，采用分治思想，将 2 的 10 次方分解为 2 的 5 次方 *2 的 5 次方，然后继续递归，直到递归调用 `fastPow(2,2)、fastPow(2,1)、fastPow(2,0)`，然后达到终止条件，递归逐层退出，`half=fastPow(2,0)` 返回 1，`half=fastPow(2,1)` 返回 half * half * x 等于 2，`half=fastPow(2,2)` 返回 hafl * half 等于 4，`half=fastPow(2,5)` 返回 half * half * x 等于 32，`half=fastPow(2,10)` 返回 half * half 等于 1024

```cpp
class Solution {  
public:  
    double myPow(double x, int n) {  
        // 处理负数指数和边界情况  
        if (n == 0) return 1.0;  
        
        // long long 处理 INT_MIN 转正数溢出问题  
        long long N = n;  
        
        // 负数指数转换  
        if (N < 0) {  
            x = 1 / x;  
            N = -N;  
        }  
        
        // 递归快速幂  
        return fastPow(x, N);  
    }  
    
private:  
    double fastPow(double x, long long n) {  
        // 递归终止条件  
        if (n == 0) return 1.0;  
        
        // 分治思想  
        double half = fastPow(x, n / 2);  
        
        // 奇数/偶数分类处理  
        return (n % 2 == 0) ? half * half : half * half * x;  
    }  
};  
```

### **方法二：快速幂迭代实现**

```cpp
cppclass Solution {  
public:  
    double myPow(double x, int n) {  
        // long long 处理 INT_MIN  
        long long N = n;  
        
        // 负数指数处理  
        if (N < 0) {  
            x = 1 / x;  
            N = -N;  
        }  
        
        double result = 1.0;  
        
        // 迭代快速幂  
        while (N > 0) {  
            // 当前位为1，乘入结果  
            if (N & 1) {  
                result *= x;  
            }  
            
            // 底数平方  
            x *= x;  
            
            // 指数右移  
            N >>= 1;  
        }  
        
        return result;  
    }  
};  
```

### **方法三：标准库实现**

```cpp
cppclass Solution {  
public:  
    double myPow(double x, int n) {  
        return pow(x, n);  
    }  
};  
```

### **方法四：暴力解法（不推荐）**

```cpp
cppclass Solution {  
public:  
    double myPow(double x, int n) {  
        // long long 处理负数指数  
        long long N = n;  
        
        // 负数指数处理  
        if (N < 0) {  
            x = 1 / x;  
            N = -N;  
        }  
        
        double result = 1.0;  
        
        // 线性计算（时间复杂度O(n)）  
        for (long long i = 0; i < N; ++i) {  
            result *= x;  
        }  
        
        return result;  
    }  
};  
```

### 详细解析

#### 1. 快速幂核心思想

- 时间复杂度：O(log n)
- 空间复杂度：O(1)
- 通过二进制分解指数，减少乘法次数

#### 2. 关键处理点

- INT_MIN 绝对值溢出问题
- 负数指数转换
- 奇偶指数不同处理

#### 3. 复杂度分析

- 递归：空间 O(log n)
- 迭代：空间 O(1)

### 边界情况处理

1. n = 0：返回 1
2. x = 0：特殊处理
3. n 为负数：转换底数
4. INT_MIN 转正数问题

### 推荐实践

1. 优先选择迭代快速幂
2. 使用 long long 处理边界
3. 考虑代码健壮性







### **基础知识：**

```cpp
long long binpow(long long a, long long b) {
  long long res = 1;
  while (b > 0) {
    if (b & 1) res = res * a;
    a = a * a;
    b >>= 1;
  }
  return res;
}
```

在这个代码片段中，`&` 是 **按位与 (bitwise AND)** 运算符。 具体来说，`b & 1` 用于 **检查 `b` 的二进制表示的最低位是否为 1**。

- 如果 `b` 的最低位是 1，则 `b & 1` 的结果是 1 (真)。
- 如果 `b` 的最低位是 0，则 `b & 1` 的结果是 0 (假)。

因此，`if (b & 1)` 这行代码的作用是： **如果 `b` 是奇数，则执行 `res = res * a;`**。 因为奇数的二进制表示的最低位一定是 1。

**按位逻辑运算符：**

|  运算符  | 符号 |            描述            |     示例     |
| :------: | :--: | :------------------------: | :----------: |
|  按位与  | `&`  |    两个位都为 1 时结果为 1    | `5 & 3 = 1`  |
|  按位或  | `|`  |    只要有一个位为 1 就为 1    | `5 \| 3 = 7` |
| 按位异或 | `^`  | 两个位不同时为 1，相同时为 0 | `5 ^ 3 = 6`  |
| 按位取反 | `~`  |         0 变 1，1 变 0         |  `~5 = -6`   |

**移位运算符：**

| 运算符 | 符号 |       描述        |     示例      |
| :----: | :--: | :---------------: | :-----------: |
|  左移  | `<<` | 向左移动，右侧补 0 | `5 << 1 = 10` |
|  右移  | `>>` |     向右移动      | `5 >> 1 = 2`  |

### 常见按位操作技巧

```cpp
cpp// 判断奇偶数  
bool isEven(int x) { return !(x & 1); }  

// 交换两个数（不使用临时变量）  
void swap(int &a, int &b) {  
    a = a ^ b;  
    b = a ^ b;  
    a = a ^ b;  
}  

// 清除最低位的1  
int clearLowestOne(int x) { return x & (x - 1); }  

// 获取最低位的1  
int getLowestOne(int x) { return x & -x; } 
```

### 标准库位操作

C++20 引入了一些新的位操作函数：

- `std::popcount()`: 计算 1 的个数
- `std::bit_width()`: 计算最高位 1 的位置
- `std::countl_zero()`: 计算前导 0 的个数

### 注意事项

1. 位运算通常比算术运算更快
2. 小心处理负数和符号位
3. 注意整数溢出风险

### 实用代码片段

```
cpp// 判断是否是2的幂  
bool isPowerOfTwo(int x) {  
    return x > 0 && !(x & (x - 1));  
}  

// 找出出现奇数次的数字  
int findOddOccurrence(vector<int>& arr) {  
    int result = 0;  
    for (int num : arr) {  
        result ^= num;  
    }  
    return result;  
}  
```

### 建议

1. 位运算虽然高效，但可读性较差
2. 在使用时添加注释说明意图
3. 优先考虑代码可读性





# 快速幂

## 定义

快速幂，二进制取幂（Binary Exponentiation，也称平方法），是一个在 $$\Theta(\log n)$$ 的时间内计算 $$a^n$$ 的小技巧，而暴力的计算需要 $$\Theta(n)$$ 的时间。

这个技巧也常常用在非计算的场景，因为它可以应用在任何具有结合律的运算中。其中显然的是它可以应用于模意义下取幂、矩阵幂等运算，我们接下来会讨论。

## 解释

计算 $$a$$ 的 $$n$$ 次方表示将 $$n$$ 个 $$a$$ 乘在一起：$$a^n = a \times a \cdots \times a$$，然而当 $$a, n$$ 太大的时候，这种方法就不太适用了。不过我们知道：$$a^{b+c} = a^b \cdot a^c$$，$$a^{2b} = (a^b)^2$$。二进制取幂的想法是，我们将取幂的任务按照指数的二进制表示来分割成更小的任务。

## 过程

### 迭代版本

首先我们将 $$n$$ 表示为 2 进制，举一个例子：

因为 $$n$$ 有 $$\lfloor \log_2 n \rfloor + 1$$ 个二进制位，因此当我们知道了 $$a^1, a^2, a^4, a^8, \ldots, a^{2^{\lfloor \log_2 n \rfloor}}$$ 后，我们只用计算 $$\Theta(\log n)$$ 次乘法就可以计算出 $$a^n$$。

于是我们只需要知道一个快速的方法来计算上述 3 的 $$2^k$$ 次幂的序列。这个问题很简单，因为序列中（除第一个）任意一个元素就是其前一个元素的平方。举一个例子：

$$
\begin{align*}
3^1 & = 3 \\
3^2 & = (3^1)^2 = 3^2 = 9 \\
3^4 & = (3^2)^2 = 9^2 = 81 \\
3^8 & = (3^4)^2 = 81^2 = 6561 \\
\end{align*}
$$

因此为了计算 $$3^{13}$$，我们只需要将对应二进制位为 1 的整系数幂乘起来就行了：

$$
3^{13} = 6561 \cdot 81 \cdot 3 = 1594323
$$

将上述过程说得形式化一些，如果把 $$n$$ 写作二进制为 $$(n_t n_{t-1} \cdots n_1 n_0)_2$$，那么有：

$$
n = n_t 2^t + n_{t-1} 2^{t-1} + n_{t-2} 2^{t-2} + \cdots + n_1 2^1 + n_0 2^0
$$

其中 $$n_i \in \{0, 1\}$$。那么就有

$$
\begin{align*}
a^n & = (a^{n_t 2^t + \cdots + n_0 2^0}) \\
& = a^{n_t 2^t} \times a^{n_{t-1} 2^{t-1}} \times \cdots \times a^{n_1 2^1} \times a^{n_0 2^0}
\end{align*}
$$

根据上式我们发现，原问题被我们转化成了形式相同的子问题的乘积，并且我们可以在常数时间内从 2^i 项推出 2^{i+1} 项。

这个算法的复杂度是 $$\Theta(\log n)$$ 的，我们计算了 $$\Theta(\log n)$$ 个 $$2^k$$ 次幂的数，然后花费 $$\Theta(\log n)$$ 的时间选择二进制为 1 对应的幂来相乘。

### 递归版本

上述迭代版本中，由于 $$2^{i+1}$$ 项依赖于 2^i，使得其转换为递归版本比较困难（一方面需要返回一个额外的 $$a^{2^i}$$，对函数来说无法实现一个只返回计算结果的接口；另一方面则是必须从低位往高位计算，即从高位往低位调用，这也造成了递归实现的困难），下面则提供递归版本的思路。

给定形式 $$n_{t...i} = (n_t n_{t-1} \cdots n_i)_2$$，则 $$n_{t...i}$$ 表示将 $$n$$ 的前 $$t-i+1$$ 位二进制位当作一个二进制数，则有如下变换：

$$
\begin{align*}
n & = n_{t...0} \\
& = 2 \times n_{t...1} + n_0 \\
& = 2 \times (2 \times n_{t...2} + n_1) + n_0 \\
& \cdots \\
\end{align*}
$$

那么有：

$$
\begin{align*}
a^n & = a^{n_{t...0}} \\
& = a^{2 \times n_{t...1} + n_0} = (a^{n_{t...1}})^2 a^{n_0} \\
& = (a^{2 \times n_{t...2} + n_1})^2 a^{n_0} = \left((a^{n_{t...2}})^2 a^{n_1}\right)^2 a^{n_0} \\
& \cdots \\
\end{align*}
$$

如上所述，在递归时，对于不同的递归深度是相同的处理：$$a^{n_{t...i}} = (a^{n_{t...(i+1)}})^2 a^{n_i}$$，即将当前递归的二进制数拆成两部分：最低位在递归出来时乘上去，其余部分则变成新的二进制数递归进入更深一层作相同的处理。

可以观察到，每递归深入一层则二进制位减少一位，所以该算法的时间复杂度也为 $$\Theta(\log n)$$。

## 实现

首先我们可以直接按照上述递归方法实现：

```cpp
long long binpow(long long a, long long b) {
    if (b == 0) return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
}
```

第二种实现方法是非递归式的。它在循环的过程中将二进制位为 1 时对应的幂累乘到答案中。尽管两者的理论复杂度是相同的，但第二种在实践过程中的速度是比第一种更快的，因为递归会花费一定的开销。



```cpp
long long binpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1) res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}
```