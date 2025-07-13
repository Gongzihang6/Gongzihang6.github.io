# [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

**示例 1:**

```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

**示例 2:**

```
输入: nums = [1], k = 1
输出: [1]
```

**提示：**

- `1 <= nums.length <= 105`
- `k` 的取值范围是 `[1, 数组中不相同的元素的个数]`
- 题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的

**进阶：** 你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n` 是数组大小。



**思路：** 首先使用哈希表记录 nums 中每个数出现的频率，格式为 <num, freq>，然后使用最小堆优先队列维护前 K 个频率最大的数和对应的频率，只要队列中元素超过 k 个，就删除堆顶元素（小顶堆中堆顶元素为当前堆中的最小元素，每次进入新元素都删除当下最小元素，遍历结束，剩下的 k 个就是前 k 个最大的。

时间复杂度：$O(n\log(n))$，其中 $n$ 为 nums 中元素个数，其中哈希表统计频率复杂度为 $O(n)$，小顶堆保留 topK 时间复杂度为 $O(n\log(n))$，主要是遍历数组 nums（$O(n)$）然后插入到小顶堆中（$O(\log(n)$）

空间复杂度：$O(n)$

```cpp
class Solution {
public:
    // TopK问题
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 统计频率
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // 小顶堆保留TopK，按照升序排列，队头元素最小，队尾元素最大，pair默认根据第一个元素大小来排序
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        
        for (auto& [num, count] : freq) {
            pq.push({count, num});
            if (pq.size() > k) {	// 只要队列中元素超过k个，就删除堆顶元素（小顶堆中堆顶元素为当前堆中的最小元素，每次进入新元素都删除当下最小元素，遍历结束，剩下的k个就是前k个最大的
                pq.pop();	// 删除堆顶元素
            }
        }
        
        vector<int> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);	// 按照频率升序输出前k个频率最大的元素
            pq.pop();
        }
        
        return result;
    }
};
```

思路：使用快速选择算法优化，快速选择算法的核心思想与快速排序类似，通过选择一个“基准值”（pivot），将数组分为两部分：左边部分：所有元素小于或等于基准值。右边部分：所有元素大于基准值。然后根据基准值的位置与目标位置 k 的关系，递归地在左半部分或右半部分继续查找，直到找到第 k 小的元素。

```cpp
class Solution {
public:
    // 快速选择算法求TopK
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 统计频率
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // 转换为频率数组
        vector<pair<int, int>> freqArr;
        for (auto& [num, count] : freq) {
            freqArr.push_back({count, num});
        }
        
        // 快速选择找TopK
        int n = freqArr.size();
        // 最后一个参数是n-k，quickSelect将数组中第n-k+1小、第k大的元素放到按升序排列下正确的位置，并且左边的都比第k大的元素小，右边的都比第k大的元素大，因此直接从第k大开始往后遍历就可以得到前k大的所有频率
        quickSelect(freqArr, 0, n - 1, n - k);
        
        // 收集结果
        vector<int> result;
        for (int i = n - k; i < n; i++) {
            result.push_back(freqArr[i].second);
        }
        
        return result;
    }
    
private:
    // 快速选择的划分函数
    int partition(vector<pair<int, int>>& arr, int left, int right) {
        // 选择最右元素作为pivot
        auto pivot = arr[right];
        int i = left - 1;	// -1
        
        for (int j = left; j < right; j++) {
            // 按频率比较
            if (arr[j].first < pivot.first) {
                i++;
                swap(arr[i], arr[j]);	// i从第一个位置开始从左往右遍历，j遍历arr中每一个元素，判断当前元素和pivot大小关系，如果比pivot小，则i增加，同时arr[j]和arr[i]交换位置，也就是将当前元素arr[j]换到左半部分，剩下的比pivot大的元素自然就被移到了右半部分；
            }
        }
        // i+1可以表示数组中元素比pivot小的个数，arr[i+1]表示的是右半部分第一个比pivot大的元素，arr[right]是pivot，这一步将pivot移动到中间，左边比pivot小，右边比pivot大
        swap(arr[i + 1], arr[right]);
        return i + 1;	// 返回pivot在数组中的索引，也就是按照从小到大的排序规则，pivot排序后的正确位置，也就是说，pivot是数组中第i+2小、第n-i-1大的元素，比它大的有n-i-2个，比它小的有i+1个,因此返回的就是数组中最右边的元素在数组中是第n-{多少}大的
    }
    
    // 快速选择算法，执行结果是将arr中第k+1小的元素放在按照升序排列的正确的位置
    void quickSelect(vector<pair<int, int>>& arr, int left, int right, int k) {
        if (left >= right) return;
        
        int pivotIndex = partition(arr, left, right);	// 返回最右边的元素按升序排列后在数组中的索引
        
        if (pivotIndex == k) {	// 如果当前选择出来的元素是数组中第k+1小，也就是左边有k个比它小的元素，右边有n-k-1个比它大的元素，如果k取n-k，当前元素就是第k大的元素
            return;
        } else if (pivotIndex < k) {
            // 右半部分
            quickSelect(arr, pivotIndex + 1, right, k);
        } else {
            // 左半部分
            quickSelect(arr, left, pivotIndex - 1, k);
        }
    }
};
```

**思路：**桶排序（Bucket Sort）是一种分布式排序算法，它通过将数据分到有限数量的“桶”中，然后对每个桶中的数据进行排序，最后按顺序合并所有桶中的数据，从而完成排序。桶排序的核心思想是将数据均匀分布到多个区间（桶）中，利用其他排序算法（如插入排序、快速排序等）对每个桶进行排序，最终合并结果。

```cpp
// 桶排序方案（另一种高效解法）
class Solution2 {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 统计频率
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // 桶排序
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [num, count] : freq) {
            buckets[count].push_back(num);	// 按照频率将数num放到buckets的第count+1个桶中，也就是buckets中第count+1个桶中存放的是频率为count的数num
        }
        
        // 收集TopK
        vector<int> result;
        // 倒序遍历桶，也就是按照频率降序遍历，依次将对应的num加入到result中
        for (int i = buckets.size() - 1; i >= 0 && result.size() < k; i--) {
            for (int num : buckets[i]) {	// 这里buckets[i]中都只有一个元素，这里循环只会执行一次
                result.push_back(num);
                if (result.size() == k) break;
            }
        }
        
        return result;
    }
};
```

