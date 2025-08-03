package com.itheima;

import java.util.Scanner;
import java.util.HashSet;
import java.util.Set;

public class PreferredCharacters {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 题目要求处理多个测试用例
        while (in.hasNextInt()) {
            int n = in.nextInt();   // n表示字符串s的长度
            int m = in.nextInt();   // m表示偏爱字符的个数

            // 1. 数据读取与准备
            // 使用 Set 存储偏爱字符，便于 O(1) 查询
            Set<Character> preferredChars = new HashSet<>();
            for (int i = 0; i < m; i++) {
                preferredChars.add(in.next().charAt(0));    // 循环添加偏爱字符到 preferredChars
            }
            String s = in.next();   // 用String s 存储输入的字符串

            // 2. 第一次扫描：从左到右，计算 left 数组
            int[] left = new int[n];
            int lastPreferredIndex = -1; // -1 表示左侧没有偏爱字符
            for (int i = 0; i < n; i++) {
                if (preferredChars.contains(s.charAt(i))) {
                    lastPreferredIndex = i;     // 从左往右遍历，lastPreferredIndex 表示当前字符的左侧最近偏爱字符的索引
                }
                left[i] = lastPreferredIndex;
            }

            // 3. 第二次扫描：从右到左，计算 right 数组
            int[] right = new int[n];
            lastPreferredIndex = -1; // -1 表示右侧没有偏爱字符
            for (int i = n - 1; i >= 0; i--) {
                if (preferredChars.contains(s.charAt(i))) {
                    lastPreferredIndex = i;     // 从右往左遍历，lastPreferredIndex 表示当前字符的右侧最近偏爱字符的索引
                }
                right[i] = lastPreferredIndex;
            }

            // 4. 第三次扫描：构建结果字符串
            StringBuilder result = new StringBuilder(n);
            for (int i = 0; i < n; i++) {
                char currentChar = s.charAt(i);
                if (preferredChars.contains(currentChar)) {
                    // 如果当前字符是偏爱字符，直接添加
                    result.append(currentChar);
                } else {
                    // 如果是非偏爱字符，进行替换决策
                    int leftIdx = left[i];
                    int rightIdx = right[i];
                    char replacementChar;

                    // 处理边界情况和常规情况
                    if (leftIdx == -1) { // 左边没有偏爱字符
                        replacementChar = s.charAt(rightIdx);
                    } else if (rightIdx == -1) { // 右边没有偏爱字符
                        replacementChar = s.charAt(leftIdx);
                    } else {
                        // 左右都有，比较距离
                        int distLeft = i - leftIdx;
                        int distRight = rightIdx - i;

                        // 平局规则：距离相等时，选左边的
                        if (distLeft <= distRight) {
                            replacementChar = s.charAt(leftIdx);
                        } else {
                            replacementChar = s.charAt(rightIdx);
                        }
                    }
                    result.append(replacementChar);
                }
            }
            // 5. 输出结果
            System.out.println(result.toString());
        }
        in.close();
    }
}