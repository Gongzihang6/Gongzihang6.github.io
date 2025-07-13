![java提高_1751343229650](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fjava%E6%8F%90%E9%AB%98_1751343229650.svg)



[TOC]



# java 提高

## java 中的异常

![Java 的异常体系谱图](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250611182352774.png)

认识运行时异常和编译时异常：

```java
package com.itheima.demo1exception;

import java.io.FileInputStream;
import java.io.InputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ExceptionDemo1 {
    public static void main(String[] args)  {
        // 目标：认识异常的体系，搞清楚异常的基本作用。
        // show();
        // try...catch捕获异常的写法
        try {
            // 监视代码，出现异常，会被catch拦截住这个异常
            show2();
        } catch (Exception e) {
            e.printStackTrace(); // 打印这个异常栈信息，按照程序调用逻辑顺序打印异常信息
        }
    }

    // 定义一个方法认识编译异常。
    // 编译异常直接抛出给方法
    public static void show2() throws Exception {
        System.out.println("==程序开始。。。。==");
        // 编译异常：编译阶段报错，编译不通过。
        String str = "2024-07-09 11:12:13";
        // 把字符串时间解析成Java中的一个日期对象。
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date = sdf.parse(str); // 编译时异常，提醒程序员这里的程序（解析日期时间）很容易出错，请您注意！
        System.out.println(date);

        // InputStream is = new FileInputStream("D:/meinv.png");

        System.out.println("==程序结束。。。。==");
    }

    // 定义一个方法认识运行时异常。
    public static void show(){
        System.out.println("==程序开始。。。。==");
        // 运行时异常的特点：编译阶段不报错，运行时出现的异常，继承自 RuntimeException。
        int[] arr = {1,2,3};
        // System.out.println(arr[3]); // ArrayIndexOutOfBoundsException

        // 出现运行时异常，程序会停止运行，不再运行异常后面的代码
        // System.out.println(10/0); // ArithmeticException

        // 空指针异常
        String str = null;
        System.out.println(str);
        System.out.println(str.length()); // NullPointerException

        System.out.println("==程序结束。。。。==");
    }
}

```

### 异常的基本处理

- **抛出异常（throws）**：在方法上使用 throws 关键字，可以将方法内部出现的异常跑出去给调用者处理；
- **捕获异常（try...catch）**：直接捕获程序出现的异常；

### 异常的作用：

- 用来定位程序 bug 的关键信息；
- 可以作为方法内部的一种特殊返回值，以便通知上层调用者，方法的执行问题；

### 自定义异常：

Java 无法为这个世界上全部的问题都提供异常类来代表， 如果企业自己的某种问题，想通过异常来表示，以便用异常来管理该问题，那就需要自己来定义异常类了。

#### 自定义运行时异常：

- 定义一个异常类型继承 RuntimeException
- 重写构造器
- 通过 throw new 异常类（×××）来创建异常对象并抛出
- 特点：编译阶段不报错，运行时才可能出现！提醒不属于激进型

#### 自定义编译时异常：

- 定义一个异常类继承 Exception
- 重写构造器
- 通过 throw new 异常类（×××）创建异常对象并抛出
- 特点：编译阶段就报错，提醒比较激进



```java
package com.itheima.demo1exception;

public class ExceptionDemo3 {
    public static void main(String[] args) {
        // 目标：认识自定义异常。
        System.out.println("程序开始。。。。");
        try {
            saveAge(300);
            System.out.println("成功了!");
        } catch (ItheimaAgeIllegalException e) {
            e.printStackTrace();
            System.out.println("失败了！");
        }
        System.out.println("程序结束。。。。");
    }

    // 需求：我们公司的系统只要收到了年龄小于1岁或者大于200岁就是一个年龄非法异常。
    public static void saveAge(int age) throws ItheimaAgeIllegalException {
        if(age < 1 || age > 200){
            // 年龄非法；抛出去一个异常。
            throw new ItheimaAgeIllegalException("年龄非法 age 不能低于1岁不能高于200岁");
        }else {
            System.out.println("年龄合法");
            System.out.println("保存年龄：" + age);
        }
    }
}
// 自定义运行时异常，编译正常，运行时可能出错
public class ItheimaAgeIllegalRuntimeException extends RuntimeException{
    public ItheimaAgeIllegalRuntimeException() {
    }

    public ItheimaAgeIllegalRuntimeException(String message) {
        super(message);
    }
}

// 自定义编译时异常，编译阶段就提醒，激进，必须抛出去才能正常编译运行
public class ItheimaAgeIllegalException extends Exception{
    public ItheimaAgeIllegalException() {
    }

    public ItheimaAgeIllegalException(String message) {
        super(message);
    }
}
```

### 异常的处理方案：

1. 底层异常层层往上抛出，最外层捕获异常，记录下异常信息，并响应适合用户观看的信息进行提示；
2. 最外层捕获异常后，尝试重新修复；

```java
package com.itheima.demo1exception;

import java.util.Scanner;

public class ExceptionDemo6 {
    public static void main(String[] args) {
        // 目标：掌握异常的处理方案2：捕获异常对象，尝试重新修复。
        // 接收用户的一个定价
        System.out.println("程序开始。。。。");

        // 设置一个死循环，只有正常处理才能break，如果出现异常，则继续循环，知道用户修复bug为止
        while (true) {
            try {
                double price = userInputPrice();
                System.out.println("用户成功设置了商品定价：" + price);
                break;
            } catch (Exception e) {
                System.out.println("您输入的数据是瞎搞的，请不要瞎输入价格！");
            }
        }

        System.out.println("程序结束。。。。");
    }

    public static double userInputPrice(){
        Scanner sc = new Scanner(System.in);
        System.out.println("请您输入商品定价：");
        double price = sc.nextDouble();
        return price;
    }
}

```

## 泛型

- 定义类、接口、方法时，同时声明了一个或者多个类型变量（如：<E>），称为泛型类，泛型接口，泛型方法，它们统称为泛型；

- **作用**：泛型约束了在编译阶段所能操作的数据类型，并自动进行检查的能力！

     这样可以避免强制类型转换，及其可能出现的异常；

- **泛型的本质**：把具体的数据类型作为参数传给类型变量；



#### 自定义泛型类

```java
// 自定义泛型类
public class MyArrayList<E> {

    private ArrayList list = new ArrayList();

    public boolean add(E e){
        list.add(e);
        return true;
    }

    public boolean remove(E e){
        return list.remove(e);
    }

    @Override
    public String toString() {
        return list.toString();
    }
}


public class GenericDemo2 {
    public static void main(String[] args) {
        // 目标：学会自定义泛型类。
        // 需求：请您模拟ArrayList集合自定义一个集合MyArrayList.
        // MyArrayList<String> list = new MyArrayList<String>();
        MyArrayList<String> mlist = new MyArrayList<>(); // JDK 7开始支持的后面类型可以不写
        mlist.add("hello");
        mlist.add("world");
//        list.add(555); // 报错
        mlist.add("java");
        mlist.add("前端");

        System.out.println(mlist.remove("world"));

        System.out.println(mlist);
    }
}
```

#### 自定义泛型接口

```java
// 自定义泛型接口
public interface Data<T> {
    void add(T t);
    void delete(T t);
    void update(T t);
    T query(int id);
}
```

#### 自定义泛型方法，能够接收任何类型参数，实现通用

```java
public class GenericDemo4 {
    public static void main(String[] args) {
        // 目标：学会定义泛型方法，搞清楚作用。
        // 需求：打印任意数组的内容。
        String[] names = {"赵敏", "张无忌", "周芷若", "小昭"};
        printArray(names);

        Student[] stus = new Student[3];
        printArray(stus);

        Student max = getMax(stus);
        String max2 = getMax(names);
    }

    public static <T> void printArray(T[] names){
        for (T name : names) {
            System.out.println(name);
        }
    }

    public static <T> T getMax(T[] names){
        return null;
    }
}
```

**通配符：**

- 就是“？”，可以在“使用泛型”的时候代表一切类型；E、T、K、V 是在定义泛型的时候使用的；

**泛型的上下限：**

- 泛型上限：`? extends Car `：?能接收的必须是 Car 或者其子类；
- 泛型下限：`? super Car`：?能接收的必须是 Car 或者其父类；

```java
package com.itheima.demo4genericity;

import java.util.ArrayList;

public class GenericDemo5 {
    public static void main(String[] args) {
        // 目标：理解通配符和上下限。
        ArrayList<Xiaomi> xiaomis = new ArrayList<>();
        xiaomis.add(new Xiaomi());
        xiaomis.add(new Xiaomi());
        xiaomis.add(new Xiaomi());
        go(xiaomis);

        ArrayList<BYD> byds = new ArrayList<>();
        byds.add(new BYD());
        byds.add(new BYD());
        byds.add(new BYD());
        go(byds);


//        ArrayList<Dog> dogs = new ArrayList<>();
//        dogs.add(new Dog());
//        dogs.add(new Dog());
//        dogs.add(new Dog());
//        go(dogs);
    }

    // 需求：开发一个极品飞车的游戏。
    // 虽然Xiaomi和BYD是Car的子类，但是 ArrayList<Xiaomi>  ArrayList<BYD>和 ArrayList<Car> 是没有半毛钱关系！
    public static void go(ArrayList<? extends Car> cars) {
    }

    // public static void go2(ArrayList<E>){
    //
    // }
}

```

**泛型支持的类型：**

- 泛型不支持基本数据类型，只能支持对象类型（引用数据类型）

| 基本数据类型 | 对应的包装类（引用数据类型） |
| :----------: | :--------------------------: |
|     byte     |             Byte             |
|    short     |            Short             |
|     int      |           Integer            |
|     long     |             Long             |
|     char     |          Character           |
|    float     |            Float             |
|    double    |            Double            |
|   boolean    |           Boolean            |

自动装箱：基本数据类型可以自动转化为包装类型；

自动拆箱：包装类型可以自动转化为基本数据类型；

**包装类具备的其他功能：**

- 可以把基本类型的数据转换成字符串类型

  - ```java
    public static String toString(double d)
    public String toString()
    ```

- 可以把字符串类型的数值转换成数值本身对应的真实数据类型

  - ```java
    public static int parseInt(String s)
    public static Integer valueOf(String s)
    ```

```java
package com.itheima.demo5genericity;

import java.util.ArrayList;

public class GenericDemo6 {
    public static void main(String[] args) {
        // 目标：搞清楚泛型和集合不支持基本数据类型，只能支持对象类型（引用数据类型）。
        // ArrayList<int> list = new ArrayList<>();
        // 泛型擦除：泛型工作在编译阶段，等编译后泛型就没用了，所以泛型在编译后都会被擦除。所有类型会恢复成Object类型

        // 把基本数据类型变成包装类对象。
        // 手工包装:
        // Integer i = new Integer(100); // 过时
        Integer it1 = Integer.valueOf(100);  // 推荐的
        Integer it2 = Integer.valueOf(100);  // 推荐的
        System.out.println(it1 == it2);

        // 自动装箱成对象：基本数据类型的数据可以直接变成包装对象的数据，不需要额外做任何事情
        Integer it11 = 130;
        Integer it22 = 130;
        System.out.println(it11 == it22);

        // 自动拆箱：把包装类型的对象直接给基本类型的数据
        int i = it11;
        System.out.println(i);

        ArrayList<Integer> list = new ArrayList<>();
        list.add(130);  // 自动装箱
        list.add(120);  // 自动装箱
        int rs = list.get(1); // 自动拆箱

        System.out.println("-----------------------------------------------------------------------");

        // 包装类新增的功能：
        // 1、把基本类型的数据转换成字符串。
        int j = 23;
        String rs1 = Integer.toString(j);   // "23"
        System.out.println(rs1 + 1); // 231

        Integer i2 = j;
        String rs2 = i2.toString(); // "23"
        System.out.println(rs2 + 1 ); // 231

        String rs3 = j + "";
        System.out.println(rs3 + 1 ); // 231

        System.out.println("-----------------------------------------------------------------------");

        // 2、把字符串数值转换成对应的基本数据类型（很有用）。
        String str = "98";
        // int i1 = Integer.parseInt(str);
        int i1 = Integer.valueOf(str);
        System.out.println(i1 + 2);

        String str2 = "98.8";
//        double d = Double.parseDouble(str2);
        double d = Double.valueOf(str2);
        System.out.println(d + 2);
    }
}

```

为什么要有包装类？

- 为了万物皆对象，并且泛型和集合都不支持基本类型，只支持包装类；

## File、字符集、I/O 流

### stream 流

使用 stream 流流式编程；简化代码，提高可读性；Stream API（`java.util.stream`）提供了一种声明式处理集合数据的方式，支持函数式编程风格。

#### 创建流

| 方法                                  | 说明             | 示例                                 |
| :------------------------------------ | :--------------- | :----------------------------------- |
| `集合.stream()`                       | 从集合创建顺序流 | `list.stream()`                      |
| `集合.parallelStream()`               | 创建并行流       | `list.parallelStream()`              |
| `Stream.of(T...)`                     | 从元素创建流     | `Stream.of("a", "b")`                |
| `Arrays.stream(T[])`                  | 从数组创建流     | `Arrays.stream(new int[]{1,2})`      |
| `Stream.iterate(种子, UnaryOperator)` | 迭代生成无限流   | `Stream.iterate(0, n -> n+2)`        |
| `Stream.generate(Supplier)`           | 生成无限流       | `Stream.generate(Math::random)`      |
| `Stream.empty()`                      | 创建空流         | `Stream.empty()`                     |
| `Files.lines(Path)`                   | 从文件创建行流   | `Files.lines(Paths.get("file.txt"))` |

#### 中间操作（惰性操作）

| 操作                 | 说明                   | 示例                                       |
| :------------------- | :--------------------- | :----------------------------------------- |
| `filter(Predicate)`  | 过滤元素               | `stream.filter(s -> s.contains("a"))`      |
| `map(Function)`      | 元素转换               | `stream.map(String::toUpperCase)`          |
| `flatMap(Function)`  | 扁平化流（合并嵌套流） | `listStream.flatMap(List::stream)`         |
| `distinct()`         | 去重                   | `stream.distinct()`                        |
| `sorted()`           | 自然排序               | `stream.sorted()`                          |
| `sorted(Comparator)` | 自定义排序             | `stream.sorted(Comparator.reverseOrder())` |
| `limit(long)`        | 截取前 n 个元素        | `stream.limit(5)`                          |
| `skip(long)`         | 跳过前 n 个元素        | `stream.skip(2)`                           |
| `peek(Consumer)`     | 调试（不修改流）       | `stream.peek(System.out::println)`         |

------

#### 终端操作（触发计算）

##### 遍历与匹配

| 操作                   | 说明                       | 示例                                       |
| :--------------------- | :------------------------- | :----------------------------------------- |
| `forEach(Consumer)`    | 遍历所有元素               | `stream.forEach(System.out::println)`      |
| `allMatch(Predicate)`  | 所有元素匹配               | `stream.allMatch(s -> s.length() > 0)`     |
| `anyMatch(Predicate)`  | 任意元素匹配               | `stream.anyMatch(s -> s.equals("Java"))`   |
| `noneMatch(Predicate)` | 无元素匹配                 | `stream.noneMatch(s -> s.startsWith("x"))` |
| `findFirst()`          | 返回第一个元素             | `stream.findFirst()`                       |
| `findAny()`            | 返回任意元素（并行流高效） | `stream.findAny()`                         |

##### 聚合计算

| 操作                             | 说明           | 示例                             |
| :------------------------------- | :------------- | :------------------------------- |
| `count()`                        | 元素总数       | `stream.count()`                 |
| `max(Comparator)`                | 最大值         | `stream.max(Integer::compare)`   |
| `min(Comparator)`                | 最小值         | `stream.min(String::compareTo)`  |
| `reduce(BinaryOperator)`         | 自定义聚合     | `stream.reduce((a,b) -> a + b)`  |
| `reduce(初始值, BinaryOperator)` | 带初始值的聚合 | `stream.reduce(0, Integer::sum)` |

##### 收集结果

```java
// 转为集合
List<String> list = stream.collect(Collectors.toList());
Set<String> set = stream.collect(Collectors.toSet());

// 转为数组
String[] arr = stream.toArray(String[]::new);

// 连接字符串
String joined = stream.collect(Collectors.joining(", "));

// 分组（返回 Map<K, List<T>>）
Map<Integer, List<Person>> byAge = personStream.collect(
    Collectors.groupingBy(Person::getAge)
);

// 分区（按 true/false 分组）
Map<Boolean, List<Person>> adults = personStream.collect(
    Collectors.partitioningBy(p -> p.getAge() >= 18)
);

// 汇总统计（数值流）
IntSummaryStatistics stats = intStream.summaryStatistics();
System.out.println("平均值: " + stats.getAverage());
```

------

数值流（避免装箱开销）

| 类型           | 创建方法                                      | 特殊操作                                    |
| :------------- | :-------------------------------------------- | :------------------------------------------ |
| `IntStream`    | `IntStream.of(1,2,3)` `IntStream.range(1,10)` | `sum()`, `average()`, `summaryStatistics()` |
| `LongStream`   | `LongStream.rangeClosed(1,100)`               | 同 `IntStream`                              |
| `DoubleStream` | `Arrays.stream(new double[]{1.1, 2.2})`       | 同 `IntStream`                              |

```java
// 对象流转数值流
IntStream ages = personStream.mapToInt(Person::getAge);

// 数值流转对象流
Stream<Integer> boxed = intStream.boxed();
```

------

#### 并行流

```java
// 创建并行流
Stream<String> parallelStream = list.parallelStream();

// 顺序流转并行流
stream.parallel().filter(...)

// 注意事项：
// 1. 确保操作线程安全（避免共享可变状态）
// 2. 数据量大时使用更高效
// 3. 避免有状态操作（如 sorted()）
```

------

#### 其他实用技巧

1. **跳过空值**

   ```java
   stream.filter(Objects::nonNull)
   ```

2. **链式操作组合**

   ```java
   list.stream()
      .filter(s -> s.length() > 3)
      .map(String::toUpperCase)
      .distinct()
      .forEach(System.out::println);
   ```

3. **短路操作**

   ```java
   boolean hasJava = list.stream()
             	   .anyMatch("Java"::equals); // 找到即终止
   ```

4. **自定义收集器**

   ```java
   Collector<Person, ?, TreeSet<Person>> toTreeSet = 
       Collector.of(TreeSet::new, TreeSet::add, (left, right) -> {
           left.addAll(right);
           return left;
       });
   ```

------

#### 注意事项

1. **流不可复用**：终端操作后流即关闭，再次使用会抛 `IllegalStateException`。
2. **惰性求值**：中间操作不立即执行，直到调用终端操作。
3. **避免副作用**：不要在 `map/filter` 中修改外部状态。
4. **并行流谨慎使用**：确保操作线程安全且数据量足够大。

示例代码

```java
package com.itheima.demo3stream;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class StreamDemo1 {
    public static void main(String[] args) {
        // 目标：认识Stream流，掌握其基本使用步骤。体会它的优势和特点。
        List<String> list = new ArrayList<>();
        list.add("张无忌");
        list.add("周芷若");
        list.add("赵敏");
        list.add("张强");
        list.add("张三丰");
        list.add("张翠山");

        // 1、先用传统方案：找出姓张的人，名字为3个字的，存入到一个新集合中去。
        List<String> newList = new ArrayList<>();
        for (String name : list) {
            if(name.startsWith("张") && name.length() == 3){
                newList.add(name);
            }
        }
        System.out.println(newList);

        // 2、使用Stream流解决
        List<String> newList2 = list.stream().filter(s -> s.startsWith("张")).filter(s -> s.length() == 3).collect(Collectors.toList());
        System.out.println(newList2);
    }
}


=======================================================
package com.itheima.demo3stream;

import java.util.*;
import java.util.stream.Stream;

public class StreamDemo2 {
    public static void main(String[] args) {
        // 目标：获取Stream流的方式。
        // 1、获取集合的Stream流：调用集合提供的stream()方法
        Collection<String> list = new ArrayList<>();
        Stream<String> s1 = list.stream();

        // 2、Map集合，怎么拿Stream流。
        Map<String, Integer> map = new HashMap<>();
        // 获取键流
        Stream<String> s2 = map.keySet().stream();
        // 获取值流
        Stream<Integer> s3 = map.values().stream();
        // 获取键值对流
        Stream<Map.Entry<String, Integer>> s4 = map.entrySet().stream();

        // 3、获取数组的流。
        String[] names = {"张三丰", "张无忌", "张翠山", "张良", "张学友"};
        Stream<String> s5 = Arrays.stream(names);
        System.out.println(s5.count()); // 5
        Stream<String> s6 = Stream.of(names);
        Stream<String> s7 = Stream.of("张三丰", "张无忌", "张翠山", "张良", "张学友");
    }
}

=================================================================
package com.itheima.demo3stream;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class StreamDemo3 {
    public static void main(String[] args) {
        // 目标：掌握Stream提供的常用的中间方法，对流上的数据进行处理（返回新流：支持链式编程）
        List<String> list = new ArrayList<>();
        list.add("张无忌");
        list.add("周芷若");
        list.add("赵敏");
        list.add("张强");
        list.add("张三丰");
        list.add("张翠山");

        // 1、过滤方法
        list.stream().filter(s -> s.startsWith("张") &&  s.length() == 3).forEach(System.out::println);

        // 2、排序方法。
        List<Double> scores = new ArrayList<>();
        scores.add(88.6);
        scores.add(66.6);
        scores.add(66.6);
        scores.add(77.6);
        scores.add(77.6);
        scores.add(99.6);
        scores.stream().sorted().forEach(System.out::println); // 默认是升序。
        System.out.println("--------------------------------------------------");

        scores.stream().sorted((s1, s2) -> Double.compare(s2, s1)).forEach(System.out::println); // 降序
        System.out.println("--------------------------------------------------");

        scores.stream().sorted((s1, s2) -> Double.compare(s2, s1)).limit(2).forEach(System.out::println); // 只要前2名
        System.out.println("--------------------------------------------------");

        scores.stream().sorted((s1, s2) -> Double.compare(s2, s1)).skip(2).forEach(System.out::println); // 跳过前2名
        System.out.println("--------------------------------------------------");

        // 如果希望自定义对象能够去重复，重写对象的hashCode和equals方法，才可以去重复！
        scores.stream().sorted((s1, s2) -> Double.compare(s2, s1)).distinct().forEach(System.out::println); // 去重复

        // 映射/加工方法： 把流上原来的数据拿出来变成新数据又放到流上去。
        scores.stream().map(s -> "加10分后：" + (s + 10)).forEach(System.out::println);

        // 合并流：
        Stream<String> s1 = Stream.of("张三丰", "张无忌", "张翠山", "张良", "张学友");
        Stream<Integer> s2 = Stream.of(111, 22, 33, 44);
        Stream<Object> s3  = Stream.concat(s1, s2);
        System.out.println(s3.count());
    }
}

================================================================
package com.itheima.demo3stream;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamDemo4 {
    public static void main(String[] args) {
        // 目标：掌握Stream流的统计，收集操作（终结方法）
        List<Teacher> teachers = new ArrayList<>();
        teachers.add(new Teacher("张三", 23, 5000));
        teachers.add(new Teacher("金毛狮王", 54, 16000));
        teachers.add(new Teacher("李四", 24, 6000));
        teachers.add(new Teacher("王五", 25, 7000));
        teachers.add(new Teacher("白眉鹰王", 66, 108000));
        teachers.add(new Teacher("陈昆", 42, 48000));

        teachers.stream().filter(t -> t.getSalary() > 15000).forEach(System.out::println);

        System.out.println("--------------------------------------------------");

        long count = teachers.stream().filter(t -> t.getSalary() > 15000).count();
        System.out.println(count);

        System.out.println("--------------------------------------------------");

        // 获取薪水最高的老师对象
        Optional<Teacher> max = teachers.stream().max((t1, t2) -> Double.compare(t1.getSalary(), t2.getSalary()));
        Teacher maxTeacher = max.get(); // 获取Optional对象中的元素
        System.out.println(maxTeacher);

        Optional<Teacher> min = teachers.stream().min((t1, t2) -> Double.compare(t1.getSalary(), t2.getSalary()));
        Teacher minTeacher = min.get(); // 获取Optional对象中的元素
        System.out.println(minTeacher);

        System.out.println("---------------------------------------------------------");

        List<String> list = new ArrayList<>();
        list.add("张无忌");
        list.add("周芷若");
        list.add("赵敏");
        list.add("张强");
        list.add("张三丰");
        list.add("张三丰");
        list.add("张翠山");

        // 流只能收集一次

        // 收集到集合或者数组中去。
        Stream<String> s1 = list.stream().filter(s -> s.startsWith("张"));
        // 收集到List集合
        List<String> list1 = s1.collect(Collectors.toList());
        System.out.println(list1);

//        Set<String> set2 = new HashSet<>();
//        set2.addAll(list1);

        // 收集到Set集合
        Stream<String> s2 = list.stream().filter(s -> s.startsWith("张"));
        Set<String> set = s2.collect(Collectors.toSet());
        System.out.println(set);

        // 收集到数组中去
        Stream<String> s3 = list.stream().filter(s -> s.startsWith("张"));
        Object[] array = s3.toArray();
        System.out.println("数组：" + Arrays.toString(array));

        System.out.println("------------------收集到Map集合---------------------------");

        // 收集到Map集合：键是老师名称，值是老师薪水
        Map<String, Double> map = teachers.stream().collect(Collectors.toMap(Teacher::getName, Teacher::getSalary));
        System.out.println(map);
    }
}



package com.itheima.demo3stream;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

// 1、对象类实现一个Comparable比较接口，重写compareTo方法，指定大小比较规则
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Teacher implements Comparable<Teacher>{
   private String name;
   private int age;
   private double salary;

   @Override
   public String toString() {
       return "Teacher{" +
               "name='" + name + '\'' +
               ", age=" + age +
               ", salary=" + salary +
               '}' + "\n";
   }

    // t2.compareTo(t1)
    // t2 == this 比较者
    // t1 == o  被比较者
    // 规定1：如果你认为左边大于右边 请返回正整数
    // 规定2：如果你认为左边小于右边 请返回负整数
    // 规定3：如果你认为左边等于右边 请返回0
    // 默认就会升序。
   @Override
   public int compareTo(Teacher o) {
       // 按照年龄升序
//        if(this.getAge() > o.getAge()) return 1;
//        if(this.getAge() < o.getAge()) return -1;
//        return 0;
       return this.getAge() - o.getAge(); // 升序
//        return o.getAge() - this.getAge(); // 降序
   }
}

```

### File 读写

File 是 java.io 包下的类，File 类的对象，用于代表当前操作系统的文件（文件或者文件夹）；

> File 类只能对文件本身进行操作，**不能读写文件里存储的数据**

IO 流

- 用于读写数据的（可以读写文件、或者网络中的数据）；
- 通过 IO 流实现内存和外存（磁盘、硬盘）的交互；

<span style="color:#CC00CC;">File对象代表具体的文件，操作的对象是文件本身；IO流是读写、更改文件里存储的数据；</span>

#### 创建 FIle 类的对象

| **构造器**                               | **说明**                                       |
| ---------------------------------------- | :--------------------------------------------- |
| public File(String pathname)             | 根据文件路径创建文件对象                       |
| public File(String parent, String child) | 根据父路径和子路径名字创建文件对象             |
| public File(File parent, String child)   | 根据父路径对应文件对象和子路径名字创建文件对象 |

注意：

- File 对象既可以代表文件，也可以代表文件夹
- File 封装的对象仅仅是一个路径名，这个路径可以是存在的，也可以是不存在的；

示例代码：

```java
public class FileDemo1 {
    public static void main(String[] args) throws Exception {
        // 目标：创建File创建对象代表文件（文件/目录），搞清楚其提供的对文件进行操作的方法。
        // 1、创建File对象，去获取某个文件的信息
        // 如果路径终点的文件不存在，那么创建的时候就会失败，但是如果throws了而且没有try...catch，就不会报错，后续判断是否是文件和文件夹都是false
        File f1 = new File("day03-FIle、字符集、IO流/代码/day03-file-io/src/csb.txt");
        System.out.println(f1.length()); // 字节个数
        System.out.println(f1.getName()); // 文件名称
        System.out.println(f1.isFile()); // true 判断是否是一个文件
        System.out.println(f1.isDirectory()); // false 判断是否是一个文件夹
        System.out.println("=========================================================");

        // 2、可以使用相对路径定位文件对象
        // 只要带盘符的都称之为：绝对路径 E:/resource/dlei.jpg
        // 相对路径：不带盘符，默认是到你的idea工程下直接寻找文件的。一般用来找工程下的项目文件的。从项目模块开始，不然idea找不到
        File f2 = new File("day03-FIle、字符集、IO流/代码/day03-file-io\\src\\dlei01.txt");
        System.out.println(f2.length());
        System.out.println(f2.getAbsoluteFile()); // 获取绝对路径
        System.out.println("=========================================================");

        // 3、创建对象代表不存在的文件路径。
        File f3 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\com\\itheima\\dlei01.txt");
        System.out.println(f3.exists()); // 判断是否存在
        System.out.println(f3.createNewFile()); // 把这个文件创建出来，如果文件已经存在，返回false
        System.out.println("=========================================================");

        // 4、创建对象代表不存在的文件夹路径。
        File f4 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\resource\\aaa");
        System.out.println(f4.mkdir()); // mkdir只能创建一级文件夹

        File f5 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\resource\\kkk\\jjj\\mmm");
        System.out.println(f5.mkdirs()); // mkdir可以创建多级文件夹，很重要！
        System.out.println("=========================================================");

        // 5、创建File对象代表存在的文件，然后删除它
        File f6 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\resource\\dlei01.txt");
        System.out.println(f6.delete()); // 删除文件
        System.out.println("=========================================================");
		  
        // 6、创建File对象代表存在的文件夹，然后删除它
        File f7 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\resource\\aaa");
        System.out.println(f7.delete());  // 只能删除空文件，不能删除非空文件夹
        System.out.println("=========================================================");
		
        // 7、
        File f8 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\resource");
        System.out.println(f8.delete());  // 只能删除空文件，不能删除非空文件夹
        System.out.println("=========================================================");

        // 8、可以获取某个目录下的全部一级文件名称
        File f9 = new File("F:\\learn_source\\java\\java_strength_6\\day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\");
        String[] names = f9.list();
        for (String name : names) {
            System.out.println(name);
        }
        File[] files = f9.listFiles();
        for (File file : files) {
            System.out.println(file.getAbsoluteFile()); // 获取绝对路径
        }
        System.out.println("=========================================================");
    }
}

```

File 方法总结：

| 方法名称                        | 说明                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| public boolean exists()         | 判断当前文件对象，对应的文件路径是否存在，存在返回 true       |
| public boolean isFile()         | 判断当前文件对象指代的是否是文件，是文件返回 true，反之。     |
| public boolean isDirectory()    | 判断当前文件对象指代的是否是文件夹，是文件夹返回 true，反之。 |
| public String getName()         | 获取文件的名称（包含后缀）                                   |
| public long length()            | 获取文件的大小，返回字节个数                                 |
| public long lastModified()      | 获取文件的最后修改时间。                                     |
| public String getPath()         | 获取创建文件对象时，使用的路径                               |
| public String getAbsolutePath() | 获取绝对路径                                                 |

File 类创建文件的功能

| 方法名称                       | 说明                 |
| ------------------------------ | -------------------- |
| public boolean createNewFile() | 创建一个新的空的文件 |
| public boolean mkdir()         | 只能创建一级文件夹   |
| public boolean mkdirs()        | 可以创建多级文件夹   |

File 类删除文件的功能

| 方法名称                 | 说明                                        |
| ------------------------ | ------------------------------------------- |
| public  boolean delete() | 删除文件、空文件夹 （默认不能删除空文件夹） |

>   **注意：delete 方法默认只能删除文件和空文件夹，删除后的文件不会进入回收站**

File 类提供的遍历文件夹的功能

| 方法名称                  | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| public String [] list()    | 获取当前目录下所有的 **"一级文件名称"** 到一个 **字符串数组** 中去返回。 |
| public File [] listFiles() | 获取当前目录下所有的 **"一级文件对象"** 到一个 **文件对象数组** 中去返回（重点） |

使用 listFiles 方法时的注意事项：

-   当主调是文件，或者路径不存在时，返回 null
-   当主调是空文件夹时，返回一个长度为 0 的数组
-   当主调是一个有内容的文件夹时，将里面所有一级文件和文件夹的文件对象放在 File 数组里返回
-   当主调是一个文件夹，且里面有隐藏文件时，将里面所有文件和文件夹的文件对象放在 File 数组中返回，包含隐藏文件
-   当主调是一个文件夹，但是没有权限访问该文件夹时，返回 null

### 常见字符集

字符集，就是二进制码和现实字母、数字、文字的一个映射表，计算机中存储的本质上是它们的二进制码，显示的时候通过字符集编码规则映射成对应的字母、数字、文字；

#### 标准 ASCII 字符集

包括英文字母（大小写）、数字、标点符号、特殊字符；

-   一个字母、数字、标点符号、特殊字符用一个字节（8 个二进制位）存储；首位全部是 0，因此最多可以表示 128 个字符；

#### GBK（汉字内码扩展规范，国标）

-   汉字编码字符集，包含了 2 万多个汉字等字符，<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">GBK中一个中文字符编码成**两个字节**的形式存储；</span>
-   注意：GBK 兼容了 ASCII 字符集；
-   GBK 规定：<span style="color:#d59bf6;">汉字的第一个字节的第一位必须是0；</span>

#### Unicode 字符集（统一码，也叫万国码）

-   国际组织制定，可以容纳世界上所有文字、符号的字符集；
-   最初采用 32 个二进制位也就是 4 个字节来表示一个字符，缺点是占存储空间大，通信效率变低；

UTF-8 字符集

-   是 Unicode 字符集的一种编码方案，采取可变长编码方案，共分四个长度区：1 个字节，2 个字节，3 个字节，4 个字节
-   **英文字符、数字等只占 1 个字节（兼容标准 ASCII 编码），汉字字符占用 3 个字节。**

>   <span style="color:#d59bf6;">注意：</span>
>
>   -   <span style="color:#d59bf6;">字符编码时使用的字符集，和解码时使用的字符集必须一致，否则会出现乱码</span>
>   -   <span style="color:#d59bf6;">英文，数字一般不会乱码，因为很多字符集都兼容了ASCII编码</span>

#### 使用程序对字符进行编码和解码操作

对字符的编码

| String 提供了如下方法                | 说明                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| byte [] getBytes()                   | 使用平台的默认字符集将该 String **编码** 为一系列字节，将结果存储到新的字节数组中 |
| byte [] getBytes(String charsetName) | 使用指定的字符集将该 String **编码** 为一系列字节，将结果存储到新的字节数组中 |

对字符的解码

| String 提供了如下方法                     | 说明                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| String(byte [] bytes)                     | 通过使用平台的默认字符集 **解码** 指定的字节数组来构造新的  String |
| String(byte [] bytes, String charsetName) | 通过指定的字符集 **解码** 指定的字节数组来构造新的 String      |

### IO 流

就是内存和硬盘的交互，将内存中的东西写入到硬盘是输入 Input，将硬盘中的东西写出到内存是输出 Output

![认识 IO 流](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250613232112065.png)

#### IO 流的体系

分为字节流、字符流，字节流又分为字节输入流、字节输出流；字符流又分为字符输入流、字符输出流；

字节流，顾名思义，传输通道中以一个一个的字节为基本单位；字符流，则是以一个一个的字符为基本单位，如一个字母、一个数字、一个汉字等；



![IO 流体系](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250613232408069.png)

##### FileInputStream（文件字节输入流）

作用：以内存为基准，可以将磁盘文件中的数据以字节形式读入到内存中；

| 构造器                                              | 说明                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| public **FileInputStream**(File file)               | 创建字节输入流管道与源文件接通                               |
| public **FileInputStream**(String pathname)         | 创建字节输入流管道与源文件接通                               |
| public int **read**()                               | 每次读取一个字节返回，如果发现没有数据可读会返回-1           |
| public int **read**(byte []  buffer)                 | 每次用一个字节数组去读取数据，返回字节数组读取了多少个字节，如果发现没有数据可读会返回-1. |
| public byte [] **readAllBytes**() throws IOException | 直接将当前字节输入流对应的文件对象的 **所有字节数据** 装到一个字节数组返回 |

注意事项：

-   使用 FileInputStream 每次读取一个字节，读取性能较差，并且读取汉字输出会乱码（因为 UTF-8 字符集中一个汉字占 3 个字节）；
-   使用 FileInputStream 每次读取多个字节，读取性能得到了提升，但读取汉字输出还是会乱码；
-   直接把文件数据全部读取到一个字节数组可以避免乱码，但是 **如果文件过大，创建的字节数组也会过大，可能引起内存溢出**
-   <span style="color:#d59bf6;">读取文本适合用字符流；字节流适合做数据的转移，比如：文件复制</span>

>   想要使用字节流读取中文，如何保证输出不乱码？
>
>   -   定义一个 **与文件一样大的字节数组，一次性读取完文件的全部字节**

示例代码：

```java
public class FileInputStreamDemo2 {
    public static void main(String[] args) throws Exception {
        // 目标：掌握文件字节输入流读取文件中的字节数组到内存中来。
        // 1、创建文件字节输入流管道于源文件接通
        InputStream is = new FileInputStream("day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\dlei03.txt"); // 简化写法

        // 2、开始读取文件中的字节并输出： 每次读取多个字节
        // 定义一个字节数组用于每次读取字节
        byte[] buffer = new byte[3];
        // 定义一个变量记住每次读取了多少个字节。
        int len;
        while ((len = is.read(buffer)) != -1) {
            // 3、把读取到的字节数组转换成字符串输出,读取多少倒出多少
            String str = new String(buffer,0, len);
            System.out.print(str);
        }
        is.close();

        // 拓展：每次读取多个字节，性能得到提升，因为每次读取多个字节，可以“减少硬盘和内存的交互次数，从而提升性能”。
        // 依然无法避免读取汉字输出乱码的问题：存在“截断汉字字节”的可能性！
    }
}


public class FileInputStreamDemo3 {
    public static void main(String[] args) throws Exception {
        // 目标：掌握文件字节输入流读取文件中的字节数组到内存中来。
        // 1、创建文件字节输入流管道于源文件接通
        InputStream is = new FileInputStream("day03-FIle、字符集、IO流\\代码\\day03-file-io\\src\\dlei04.txt"); // 简化写法

        // 2、一次性读完文件的全部字节:可以避免读取汉字输出乱码的问题。
        byte[] bytes = is.readAllBytes();

        String rs = new String(bytes);
        System.out.println(rs);

        is.close();
    }
}
```

##### FileOutputStream（文件字节输出流）

以内存为基准，把内存中的数据以字节的形式写出到文件中去；

基本构造：

| **构造器**                                               | **说明**                                               |
| -------------------------------------------------------- | ------------------------------------------------------ |
| public FileOutputStream(File file)                       | 创建字节输出流管道与 **源文件对象** 接通                 |
| public FileOutputStream(String filepath)                 | 创建字节输出流管道与 **源文件路径** 接通                 |
| public FileOutputStream(File file，boolean append)       | 创建字节输出流管道与 **源文件对象** 接通，可 **追加** 数据 |
| public FileOutputStream(String filepath，boolean append) | 创建字节输出流管道与 **源文件路径** 接通，可 **追加** 数据 |

常用方法：

| **方法名称**                                         | **说明**                         |
| ---------------------------------------------------- | -------------------------------- |
| public void **write**(int a)                         | 写一个 **字节** 出去               |
| public void write(byte [] buffer)                     | 写一个 **字节数组** 出去           |
| public void write(byte [] buffer , int pos , int len) | 写一个 **字节数组的一部分** 出去。 |
| public void **close**() throws IOException           | 关闭流。                         |

用文件字节输入流（FileInputStream）读取一个文件的字节流，再用文件字节输出流（FileOutputStream）将这个字节流写出到另一个文件，实现文件复制

同时了解 try..catch..finally 的用法，try-with-resources 的语法

```java
public class CopyDemo1 {
    public static void main(String[] args) {
        // 目标：使用字节流完成文件的复制操作。
        // 源文件：E:\resource\jt.jpg
        // 目标文件：D:\jt_new.jpg （复制过去的时候必须带文件名的，无法自动生成文件名。）
        copyFile("E:\\resource\\jt.jpg", "D:\\jt_new.jpg");
    }

    // 复制文件
    public static void copyFile(String srcPath, String destPath)  {
        // 1、创建一个文件字节输入流管道与源文件接通
        InputStream fis = null;
        OutputStream fos = null;
        try {
            fis = new FileInputStream(srcPath);
            fos = new FileOutputStream(destPath);
            // 2、读取一个字节数组，写入一个字节数组  1024 + 1024 + 3
            byte[] buffer = new byte[1024];
            int len;
            while ((len = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, len); // 读取多少个字节，就写入多少个字节
            }
            System.out.println("复制成功！");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 最后一定会执行一次：即便程序出现异常！
            // 3、释放资源
            try {
                if(fos != null) fos.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            try {
                if(fis != null) fis.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

public class CopyDemo2 {
    public static void main(String[] args) {
        // 目标：掌握资源的新方式：try-with-resource
        // 源文件：E:\resource\jt.jpg
        // 目标文件：D:\jt_new.jpg （复制过去的时候必须带文件名的，无法自动生成文件名。）
        copyFile("E:\\resource\\jt.jpg", "D:\\jt_new.jpg");
    }

    // 复制文件
    public static void copyFile(String srcPath, String destPath)  {
        // 1、创建一个文件字节输入流管道与源文件接通
        try (
             // 这里只能放置资源对象，用完后，最终会自动调用其close方法关闭！！
             InputStream fis = new FileInputStream(srcPath);
             OutputStream fos = new FileOutputStream(destPath);
             MyConn conn = new MyConn(); // 自定义的资源对象 最终会自动调用其close方法关闭！！
            ){
            // 2、读取一个字节数组，写入一个字节数组  1024 + 1024 + 3
            byte[] buffer = new byte[1024];
            int len;
            while ((len = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, len); // 读取多少个字节，就写入多少个字节
            }
            System.out.println("复制成功！");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class MyConn implements Closeable{
    @Override
    public void close() throws IOException {
        System.out.println("dlei的资源关闭了！");
    }
}
```

-   finally 代码区的特点：无论 try 中的程序是正常执行了，还是出现了异常，最后都一定会执行 finally 区，除非 JVM 终止。作用：一般用于在程序执行完成后进行资源的释放操作（专业级做法）


##### FIleReader（文件字符输入流）

以内存为基准，可以把文件中的数据以字符的形式读入到内存中去；

| **构造器**                             | **说明**                       |
| -------------------------------------- | ------------------------------ |
| public **FileReader**(File file)       | 创建字符输入流管道与源文件接通 |
| public **FileReader**(String pathname) | 创建字符输入流管道与源文件接通 |

读取字符流的方法：

| **方法名称**                        | **说明**                                                     |
| ----------------------------------- | ------------------------------------------------------------ |
| public int read()                   | 每次读取一个字符返回，如果发现没有数据可读会返回-1.          |
| public int read(**char []  buffer**) | 每次用一个字符数组去读取数据，返回字符数组读取了多少个字符，如果发现没有数据可读会返回-1. |

```java
public class FileReaderDemo1 {
    public static void main(String[] args) {
        // 目标：掌握文件字符输入流读取字符内容到程序中来。
        try (
                // 1、创建文件字符输入流与源文件接通
            Reader fr = new FileReader("day03-FIle、字符集、IO流/代码/day03-file-io\\src\\dlei06.txt");
        ) {
            // 2、定义一个字符数组，每次读多个字符
            char[] chs = new char[3];
            int len; // 用于记录每次读取了多少个字符
            while ((len = fr.read(chs)) != -1){
                // 3、每次读取多个字符，并把字符数组转换成字符串输出
                String str = new String(chs,0,len);
                System.out.print(str);
            }
            // 拓展：文件字符输入流每次读取多个字符，性能较好，而且读取中文
            // 是按照字符读取，不会出现乱码！这是一种读取中文很好的方案。
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
```



##### FileWriter（文件字符输出流）

以内存为基准，把内存中的数据以字符的形式写出到文件中；

| **构造器**                                         | **说明**                                       |
| -------------------------------------------------- | ---------------------------------------------- |
| public FileWriter(File file)                       | 创建字节输出流管道与源文件对象接通             |
| public FileWriter(String filepath)                 | 创建字节输出流管道与源文件路径接通             |
| public FileWriter(File file，boolean append)       | 创建字节输出流管道与源文件对象接通，可追加数据 |
| public FileWriter(String filepath，boolean append) | 创建字节输出流管道与源文件路径接通，可追加数据 |

常用方法

| **方法名称**                               | **说明**             |
| ------------------------------------------ | -------------------- |
| void  write(int c)                         | 写一个字符           |
| void  write(String str)                    | 写一个字符串         |
| void  write(String str, int off, int len)  | 写一个字符串的一部分 |
| void  write(char [] cbuf)                   | 写入一个字符数组     |
| void  write(char [] cbuf, int off, int len) | 写入字符数组的一部分 |

<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">字符输出流写出数据后，必须刷新流，或者关闭流，写出去的数据才能生效</span>

| 方法名称                                | 说明                                                 |
| --------------------------------------- | ---------------------------------------------------- |
| public  void flush() throws IOException | 刷新流，就是将内存中缓存的数据立即写到文件中去生效！ |
| public  void close() throws IOException | 关闭流的操作，包含了刷新！                           |

```java
public class FileWriterDemo1 {
    public static void main(String[] args) {
        // 目标：搞清楚文件字符输出流的使用：写字符出去的流。

        try (
            // 1. 创建一个字符输出流对象，指定写出的目的地。
            // Writer fw = new FileWriter("day03-file-io/src/dlei07-out.txt"); // 覆盖管道
            Writer fw = new FileWriter("day03-FIle、字符集、IO流\\代码\\day03-file-io/src/dlei07-out.txt", true); // 追加数据
            ){

            // 2. 写一个字符出去：  public void write(int c)
            fw.write('a');
            fw.write(98);
            fw.write('磊');
            fw.write("\r\n"); // 换行

            // 3、写一个字符串出去：  public void write(String str)
            fw.write("java");
            fw.write("我爱Java，虽然Java不是最好的编程之一,但是可以挣钱");
            fw.write("\r\n"); // 换行

            // 4、写字符串的一部分出去：  public void write(String str, int off, int len)
            fw.write("java", 1, 2);
            fw.write("\r\n"); // 换行

            // 5、写一个字符数组出去：  public void write(char[] cbuf)
            char[] chars = "java".toCharArray();
            fw.write(chars);
            fw.write("\r\n"); // 换行

            // 6、写字符数组的一部分出去：  public void write(char[] cbuf, int off, int len)
            fw.write(chars, 1, 2);
            fw.write("\r\n"); // 换行

            // fw.flush(); // 刷新缓冲区，将缓冲区中的数据全部写出去。
            // 刷新后，流可以继续使用。
            // fw.close(); // 关闭资源，关闭包含了刷新！关闭后流不能继续使用！
				// 因为使用了try-with-resource，资源会自动关闭，因此也就会自动flush
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```



#### 缓冲流

![字节、字符缓冲流](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250615154929492.png)

BufferedInputStream（缓冲字节输入流）

-   作用：可以提高字节输入流读取数据的性能；
-   原理：缓冲字节输入流自带了 8KB 缓冲池；缓冲字节输出流也自带了 8KB 缓冲池；

| 构造器                                               | 说明                                                         |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| public BufferedInputStream(InputStream is)           | 把低级的字节输入流包装成一个高级的缓冲字节输入流，从而提高读数据的性能 |
| public BufferedOutputStream(OutputStream os)         | 把低级的字节输出流包装成一个高级的缓冲字节输出流，从而提高写数据的性能 |
| public BufferedInputStream(InputStream in, int size) | 把低级的字节输入流包装成一个高级的缓冲字节输入流，`size` 表示缓冲池大小，单位为字节； |

示例代码：用缓冲字节输入流、输出流提高文件复制效率；

```java
public class CopyDemo1 {
    public static void main(String[] args) {
        // 目标：掌握缓冲字节流的使用。
        // 源文件：E:\resource\jt.jpg
        // 目标文件：D:\jt_new.jpg （复制过去的时候必须带文件名的，无法自动生成文件名。）
        copyFile("E:\\resource\\jt.jpg", "D:\\jt_new2.jpg");
    }

    // 复制文件
    public static void copyFile(String srcPath, String destPath)  {
        // 1、创建一个文件字节输入流管道与源文件接通
        try (
                // 这里只能放置资源对象，用完后，最终会自动调用其close方法关闭！！
                InputStream fis = new FileInputStream(srcPath);
                // 把低级的字节输入流包装成高级的缓冲字节输入流
                InputStream bis = new BufferedInputStream(fis);

                OutputStream fos = new FileOutputStream(destPath);
                // 把低级的字节输出流包装成高级的缓冲字节输出流
                OutputStream bos = new BufferedOutputStream(fos);
                ){
            // 2、读取一个字节数组，写入一个字节数组  1024 + 1024 + 3
            byte[] buffer = new byte[1024];
            int len;
            while ((len = bis.read(buffer)) != -1) {
                bos.write(buffer, 0, len); // 读取多少个字节，就写入多少个字节
            }
            System.out.println("复制成功！");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

##### BufferedReader（缓冲字符输入流）

作用：自带 8KB（8192 字节）的字符缓冲池，可以提高字符输入流读取字符数据的性能；本质上都是减少内存和硬盘的交互次数；

![缓冲字符输入流](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250615162615086.png)

| 构造器                           | 说明                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| public  BufferedReader(Reader r) | 把低级的字符输入流包装成字符缓冲输入流管道，从而提高字符输入流读字符数据的性能 |

**字符缓冲输入流新增的功能：按照行读取字符**

| 方法                      | 说明                                             |
| ------------------------- | ------------------------------------------------ |
| public  String readLine() | 读取一行数据返回，如果没有数据可读了，会返回 null |



##### BufferedWriter（缓冲字符输出流）

-   作用：自带 8K 的字符缓冲池，可以提高字符输出流写字符数据的性能。

| 构造器                           | 说明                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| public  BufferedWriter(Writer r) | 把低级的字符输出流包装成一个高级的缓冲字符输出流管道，从而提高字符输出流写数据的性能 |

**字符缓冲输出流新增的功能：换行**

| 方法                   | 说明 |
| ---------------------- | ---- |
| public  void newLine() | 换行 |

**推荐使用哪种方式提高字节流读写数据的性能？**

-   建议使用字节缓冲输入流、字节缓冲输出流，结合字节数组的方式，目前来看是性能最优的组合。

#### 其他流

![整个 IO 流体系](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250615173105469.png)

##### InputStreamReader（字符输入转换流）

-   解决不同编码时，字符流读取文本内容乱码的问题。

-   解决思路：<span style="color:#d59bf6;">先获取文件的原始字节流，再将其按真实的字符集编码转成字符输入流</span>，这样字符输入流中的字符就不乱码了

| **构造器**                                                 | **说明**                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| public InputStreamReader(InputStream is)                   | 把原始的字节输入流，按照代码默认编码转成字符输入流（与直接用 FileReader 的效果一样） |
| public InputStreamReader(InputStream is ，String  charset) | 把原始的字节输入流，按照指定字符集编码转成字符输入流(重点)   |

示例代码：

```java
public class Demo2 {
    public static void main(String[] args) {
        // 目标：使用字符输入转换流InputStreamReader解决不同编码读取乱码的问题、
        // 代码：UTF-8   文件 UTF-8  读取不乱码
        // 代码：UTF-8   文件 GBK  读取乱码
        try (
                // 先提取文件的原始字节流
                InputStream is = new FileInputStream("day03-FIle、字符集、IO流/代码/day03-file-io\\src\\dlei09.txt");
                // 指定字符集把原始字节流转换成字符输入流
                Reader isr = new InputStreamReader(is, "GBK");
                // 2、创建缓冲字符输入流包装低级的字符输入流
                BufferedReader br = new BufferedReader(isr);
        ) {
            // 定义一个字符串变量用于记住每次读取的一行数据
            String line;
            while ((line = br.readLine()) != null){
                System.out.println(line);
            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
```

##### PrintStream/PrintWriter（打印流）

-   作用：打印流可以实现更方便、更高效的打印数据出去（到硬盘），能实现打印啥出去就是啥出去。


**PrintStream** 提供的打印数据的方案：

| 构造器                                                       | 说明                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| public  **PrintStream**(OutputStream/File/String)            | 打印流直接通向字节输出流/文件/文件路径   |
| public PrintStream(String fileName, Charset charset)         | 可以指定写出去的字符编码                 |
| public PrintStream(OutputStream, boolean autoFlush)          | 可以指定实现自动刷新                     |
| public PrintStream(OutputStream, boolean autoFlush, String encoding) | 可以指定实现自动刷新，并可指定字符的编码 |

方法：

| **方法**                                          | **说明**                   |
| ------------------------------------------------- | -------------------------- |
| public  void **println**()                        | 打印任意类型的数据出去     |
| public  void **write**(int/byte []/byte [] 的一部分) | 可以支持写 **字节** 数据出去 |

**PrintWriter** 提供的打印数据的方案：

| 构造器                                                       | 说明                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| public  PrintWriter(OutputStream/Writer/FIle/String)         | 打印流直接通向字节输出流/文件/文件路径   |
| public PrintWriter(String fileName, Charset charset)         | 可以指定写出去的字符编码                 |
| public PrintWriter(OutputStream out/writer, boolean autoFlush) | 可以指定实现自动刷新                     |
| public PrintWriter(OutputStream out, boolean autoFlush, String encoding) | 可以指定实现自动刷新，并可指定字符的编码 |

方法：

| 方法                                     | 说明                   |
| ---------------------------------------- | ---------------------- |
| public  void println(Xxx xx)             | 打印任意类型的数据出去 |
| public  void write(int/String/char []/..) | 可以支持写字符数据出去 |

示例代码：

```java
public class PrintStreamDemo1 {
    public static void main(String[] args) {
        // 目标：打印流的使用。
       try (    // PrintStream ps = new PrintStream("day03-file-io/src/ps.txt");
                PrintStream ps = new PrintStream(new FileOutputStream("day03-FIle、字符集、IO流/代码/day03-file-io/src/ps.txt", true));
                // PrintWriter ps = new PrintWriter("day03-file-io/src/ps.txt");
       ){
           ps.println(97);
           ps.println('a');
           ps.println("黑马");
           ps.println(true);
           ps.println(99.9);
       }catch (Exception e){
           e.printStackTrace();
       }
    }
}
```

PrintStream 和 PrintWriter 的区别：

-   打印数据的功能是一样的：都是<span style="color:#d59bf6;">使用方便，性能高效（核心优势）</span>；
-   PrintStream 继承自字节输出流 OutputStream，因此支持写字节数据的方法；
-   PrintWriter 底层由缓冲字符输出流 BufferedWriter 实现，因此支持写字符数据出去；

#### 特殊数据流

##### DataOutputStream（数据输出流）

-   允许把数据和其类型一并写出去；

| 构造器                                    | 说明                                 |
| ----------------------------------------- | ------------------------------------ |
| public DataOutputStream(OutputStream out) | 创建新数据输出流包装基础的字节输出流 |

方法：

| 方法                                                        | 说明                                              |
| ----------------------------------------------------------- | ------------------------------------------------- |
| public  final void writeByte(int v)  throws IOException     | 将 byte 类型的数据写入基础的字节输出流              |
| public  final void writeInt(int v) throws IOException       | 将 int 类型的数据写入基础的字节输出流               |
| public  final void writeDouble(Double v) throws IOException | 将 double 类型的数据写入基础的字节输出流            |
| public  final void writeUTF(String str) throws IOException  | 将字符串数据以 UTF-8 编码成字节写入基础的字节输出流 |
| public  void write(int/byte []/byte [] 一部分)                 | 支持写字节数据出去                                |



##### DataInputStream（数据输入流）

-   用于读取数据输出流写出去的数据，和 DataOutputStream 配合使用

构造器：

| 构造器                                 | 说明                                 |
| -------------------------------------- | ------------------------------------ |
| public DataInputStream(InputStream is) | 创建新数据输入流包装基础的字节输入流 |

方法：

| 方法                                                 | 说明                        |
| ---------------------------------------------------- | --------------------------- |
| Public  final byte readByte()  throws IOException    | 读取字节数据返回            |
| public  final int readInt() throws IOException       | 读取 int 类型的数据返回       |
| public  final double readDouble() throws IOException | 读取 double 类型的数据返回    |
| public  final String readUTF() throws IOException    | 读取字符串数（UTF-8）据返回 |
| public  int readInt()/read(byte [])                   | 支持读字节数据进来          |

```java
public class DataStreamDemo2 {
    public static void main(String[] args) {
        // 目标：特殊数据流的使用。
       try (
               DataOutputStream dos = new DataOutputStream(new FileOutputStream("day03-FIle、字符集、IO流/代码/day03-file-io\\src\\data.txt"));
               ){
           dos.writeByte(34);
           dos.writeUTF("你好");
           dos.writeInt(3665);
           dos.writeDouble(9.9);
       }catch (Exception e){
           e.printStackTrace();
       }
       
public class DataStreamDemo3 {
    public static void main(String[] args) {
        // 目标：特殊数据流的使用。
       try (
               DataInputStream dis = new DataInputStream(new FileInputStream("day03-FIle、字符集、IO流/代码/day03-file-io\\src\\data.txt"));
               ){
           System.out.println(dis.readByte());
           System.out.println(dis.readUTF());
           System.out.println(dis.readInt());
           System.out.println(dis.readDouble());
       }catch (Exception e){
           e.printStackTrace();
       }
    }
}
```



### IO 框架

-   框架（Framework）是一个预先写好的代码库或一组工具，旨在简化和加速开发过程
-   框架的形式：一般是把类、接口等编译成 class 形式，再压缩成一个.jar 结尾的文件发行出去

IO 框架：封装了 Java 提供的对文件、数据进行操作的代码，对外提供了更简单的方式来对文件进行操作，对数据进行读写等

#### Commons-io 框架

Commons-io 是 apache 开源基金组织提供的一组有关 IO 操作的小框架，目的是提高 IO 流的开发效率

| FileUtils 类提供的部分方法展示                                | 说明       |
| ------------------------------------------------------------ | ---------- |
| public static void **copyFile**(File srcFile, File destFile) | 复制文件。 |
| public static void **copyDirectory**(File srcDir, File destDir) | 复制文件夹 |
| public static void **deleteDirectory**(File directory)       | 删除文件夹 |
| public static String **readFileToString**(File file, String encoding) | 读数据     |
| public static void **writeStringToFile**(File file, String data, String charname, boolean append) | 写数据     |



| IOUtils 类提供的部分方法展示                                  | 说明       |
| ------------------------------------------------------------ | ---------- |
| public static int **copy**(InputStream inputStream, OutputStream outputStream) | 复制文件。 |
| public static int **copy**(Reader reader, Writer writer)     | 复制文件。 |
| public static void **write**(String data, OutputStream output, String charsetName) | 写数据     |



## 多线程

基本概念：

-   线程(Thread)是一个程序内部的一条执行流程；
-   程序中如果只有一条执行流程，那这个程序就是单线程的程序
-   多线程是指从软硬件上实现的多条执行流程的技术（多条线程由 CPU 负责调度执行）

### 创建线程

#### 多线程的创建方式一：继承 Thread 类

1.  定义一个子类 MyThread 继承线程类 `java.lang.Thread`，重写 `run()` 方法；
2.  创建 MyThread 类的对象；
3.  调用线程对象的 `start()` 方法启动线程（实际启动后还是执行 run 方法完成线程任务）

##### 方式一优缺点：

-   优点：写代码简单；
-   缺点：线程类已经继承 Thread，无法继承其他类，不利于功能的扩展；

##### 创建线程的注意事项

1.  启动线程必须是调用 start 方法，不是调用 run 方法
    -   直接调用 run 方法会被当成普通方法执行，此时相当于还是单线程执行；
    -   只有调用 start 方法才是启动一个新的线程执行；
2.  不要把主线程任务放在启动子线程之前
    -   这样主线程一直是先跑完的，相当于是一个单线程的效果了。

```java
public class ThreadDemo1 {
    // main方法本身是由一条主线程负责推荐执行的。
    public static void main(String[] args) {
        // 目标：认识多线程，掌握创建线程的方式一：继承Thread类来实现
        // 4、创建线程类的对象：代表线程。
        Thread t1 = new MyThread();
        // 5、调用start方法，启动线程。还是调用run方法执行的
        t1.start(); // 启动线程，让线程执行run方法
        // 子线程启动后，程序不需要在这里等待子线程执行完毕，而是主线程继续往下执行代码，出现子线程和主线程交替输出数字的效果

        // 主线程后启动，先启动子线程打印，再启动主线程打印
        for (int i = 0; i < 5; i++) {
            System.out.println("主线程输出：" + i);
        }
    }
}

// 1、定义一个子类继承Thread类，成为一个线程类。
class MyThread extends Thread {
    // 2、重写Thread类的run方法
    @Override
    public void run() {
        // 3、在run方法中编写线程的任务代码（线程要干的活儿）
        for (int i = 0; i < 5; i++) {
            System.out.println("子线程输出：" + i);
        }
    }
}

```

#### 多线程的创建方式二：实现 Runnable 接口

1.  定义一个线程任务类 MyRunnable 实现 Runnable 接口，重写 run()方法；

2.  创建 MyRunnable 任务对象；

3.  把 MyRunnable 任务对象交给 Thread 处理；

    -   | Thread 类提供的构造器           | 说明                         |
        | ------------------------------ | ---------------------------- |
        | public Thread(Runnable target) | 封装 Runnable 对象成为线程对象 |

4.  调用线程对象的 start()方法启动线程；

##### 方式二的优缺点：

-   优点：任务类只是实现接口，可以继续继承其他类、实现其他接口，扩展性强；
-   缺口：需要多一个 Runnable 对象；

```java
public class ThreadDemo2 {
    public static void main(String[] args) {
        // 目标：掌握多线程的创建方式二：实现Runnable接口来创建。
        // 3、创建线程任务类的对象代表一个线程任务。
        Runnable r = new MyRunnable();
        // 4、把线程任务对象交给一个线程对象来处理
        Thread t1 = new Thread(r); // public Thread(Runnable r)
        // Thread t1 = new Thread(r, "1号子线程"); // public Thread(Runnable r,String name)
        // 5、启动线程
        t1.start();

        for (int i = 0; i < 5; i++) {
            System.out.println("主线程输出：" + i);
        }
    }
}

// 1、定义一个线程任务类实现Runnable接口
class MyRunnable implements Runnable {
    // 2、重写run方法，设置线程任务
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("子线程输出：" + i);
        }
    }
}



// 用匿名内部类简化代码
public class ThreadDemo2_2 {
    public static void main(String[] args) {
        // 目标：掌握多线程的创建方式二：使用Runnable接口的匿名内部类来创建
        // Runnable是一个函数式接口，只有一个待实现方法Run，因此可以用匿名内部类来简化代码
        Runnable r = new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.println("子线程1输出：" + i);
                }
            }
        };
        Thread t1 = new Thread(r); // public Thread(Runnable r)
        t1.start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.println("子线程2输出：" + i);
                }
            }
        }).start();

        new Thread(() -> {
                for (int i = 0; i < 5; i++) {
                    System.out.println("子线程3输出：" + i);
                }
        }).start();

        for (int i = 0; i < 5; i++) {
            System.out.println("主线程输出：" + i);
        }
    }
}

```



#### 线程的创建方式三：实现 Callable 接口

>   <span style="color:#d59bf6;">前两种线程创建方式都存在的一个问题：如果线程执行完毕后有一些数据需要返回，它们重写的run方法均不能直接返回结果</span>

解决方式：

-   JDK5.0 提供了 Callable 接口和 FutureTask 类来实现（多线程的第三种创建方式）
-   这种方式最大的优点：可以返回线程执行完毕后的结果；

1.  创建任务对象
    -   定义一个类实现 Callable 接口，重写 call 方法，封装该线程任务要做的事情，和要返回的数据；
    -   把 Callable 类型的对象封装成 FutureTask（线程任务对象），`public FutureTask(Callable<V> callable)`
2.  把线程任务交给 Thread 对象；
3.  调用 Thread 对象的 start 方法启动线程；
4.  线程执行完毕后，通过 FutureTask 对象的 get 方法去获取任务执行的结果；

FutureTask 的 API

| FutureTask 提供的构造器                 | 说明                                 |
| -------------------------------------- | ------------------------------------ |
| public **FutureTask** <>(Callable call) | 把 Callable 对象封装成 FutureTask 对象。 |
| public V **get()** throws Exception    | 获取线程执行 call 方法返回的结果。     |

##### 线程创建方式三的优缺点：

-   优点：线程任务类只是实现 Callable 接口，可以继续继承类和实现其他接口，扩展性强；**可以在线程执行完毕后去获取线程执行的结果；**
-   缺点：编码复杂一点；

```java
public class ThreadDemo3 {
    public static void main(String[] args) {
        // 目标：掌握多线程的创建方式三：实现Callable接口，方式三的优势：可以获取线程执行完毕后的结果的。
        // 3、创建一个Callable接口的实现类对象。n=100是类的初始化参数，表示求1到100的和
        Callable<String> c1 = new MyCallable(100);
        // 4、把Callable对象封装成一个真正的线程任务对象FutureTask对象。
        /**
         * 未来任务对象的作用？
         *    a、本质是一个Runnable线程任务对象，可以交给Thread线程对象处理。
         *    b、可以获取线程执行完毕后的结果。
         */
        FutureTask<String> f1 = new FutureTask<>(c1); // public FutureTask(Callable<V> callable)
        // 5、把FutureTask对象作为参数传递给Thread线程对象。
        Thread t1 = new Thread(f1);
        // 6、启动线程。
        t1.start();

        Callable<String> c2 = new MyCallable(50);
        FutureTask<String> f2 = new FutureTask<>(c2); // public FutureTask(Callable<V> callable)
        Thread t2 = new Thread(f2);
        t2.start();

        // 获取线程执行完毕后返回的结果
        try {
            // 如果主线程发现第一个线程还没有执行完毕，会让出CPU，等第一个线程执行完毕后，才会往下执行！
            System.out.println(f1.get());
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            // 如果主线程发现第二个线程还没有执行完毕，会让出CPU，等第一个线程执行完毕后，才会往下执行！
            System.out.println(f2.get());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// 1、定义一个实现类实现Callable接口
class MyCallable implements Callable<String> {
    private int n;
    public MyCallable(int n) {
        this.n = n;
    }
    // 2、实现call方法，定义线程执行体
    public String call() throws Exception {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return "子线程计算1-" + n + "的和是："  + sum;
    }
}
```



#### 总结三种线程创建方式的优缺点对比：

| 方式             | 优点                                                         | 缺点                                                   |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| 继承 Thread 类     | 编程比较简单，可以直接使用 Thread 类中的方法                   | 扩展性较差，不能再继承其他的类，不能返回线程执行的结果 |
| 实现 Runnable 接口 | 扩展性强，实现该接口的同时还可以继承其他的类。               | 编程相对复杂，不能返回线程执行的结果                   |
| 实现 Callable 接口 | 扩展性强，实现该接口的同时还可以继承其他的类。可以得到线程执行的结果 | 编程相对复杂                                           |

---

Thread 的常用方法：

| Thread 提供的常用方法                     | 说明                                          |
| ---------------------------------------- | --------------------------------------------- |
| public void **run()**                    | 线程的任务方法                                |
| public void **start()**                  | 启动线程                                      |
| public String **getName()**              | 获取当前线程的名称，线程名称默认是 Thread-索引 |
| public void **setName(String name)**     | 为线程设置名称                                |
| public static Thread **currentThread()** | 获取当前执行的线程对象                        |
| public static void **sleep(long time)**  | 让当前执行的线程休眠多少毫秒后，再继续执行    |
| public final void **join()**             | 让调用当前这个方法的线程先执行完！            |

示例代码：

```java
// 演示设置和获取线程名称
public class ThreadApiDemo1 {
    public static void main(String[] args) {
        // 目标：搞清楚线程的常用方法。
        Thread t1 = new MyThread("1号线程");
        // t1.setName("1号线程");
        t1.start();
        System.out.println(t1.getName()); // 线程默认名称是：Thread-索引

        Thread t2 = new MyThread("2号线程");
        // t2.setName("2号线程");
        t2.start();
        System.out.println(t2.getName()); // 线程默认名称是：Thread-索引

        // 哪个线程调用这个代码，这个代码就拿到哪个线程
        Thread m = Thread.currentThread(); // 主线程
        m.setName("主线程");
        System.out.println(m.getName()); // main
    }
}

// 1、定义一个子类继承Thread类，成为一个线程类。
class MyThread extends Thread {
    public MyThread(String name) {
        super(name); // public Thread(String name)
    }

    // 2、重写Thread类的run方法
    @Override
    public void run() {
        // 3、在run方法中编写线程的任务代码（线程要干的活儿）
        for (int i = 0; i < 5; i++) {
            System.out.println(Thread.currentThread().getName() +"子线程输出：" + i);
        }
    }
}

// 演示线程的休眠方法
public class ThreadApiDemo2 {
    public static void main(String[] args) {
        // 目标：搞清楚Thread类的Sleep方法（线程休眠）
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
            try {
                // 让当前执行的线程进入休眠状态，直到时间到了，才会继续执行。
                // 项目经理让我加上这行代码，如果用户交钱了，我就注释掉。
                // 默认是主线程
                Thread.sleep(1000); // 1000ms = 1s
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

// 演示线程的插队方法join
public class ThreadApiDemo3 {
    public static void main(String[] args) {
        // 目标：搞清楚线程的join方法：线程插队：让调用这个方法线程先执行完毕。
        MyThread2 t1 = new MyThread2();
        t1.start();

        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() +"线程输出：" + i);
            // main线程只要执行到1，就会调用t1线程的join方法，插队，让t1线程先打印，然后继续执行主线程
            if(i == 1){
                try {
                    t1.join(); // 插队 让t1线程先执行完毕，然后继续执行主线程
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

class MyThread2 extends Thread {
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() +"子线程输出：" + i);
        }
    }
}
```

Thread 提供的常见的构造器：

| Thread 提供的常见构造器                      | 说明                                         |
| ------------------------------------------- | -------------------------------------------- |
| public Thread(String name)                  | 可以为当前线程指定名称                       |
| public Thread(Runnable target)              | 封装 Runnable 对象成为线程对象                 |
| public Thread(Runnable target, String name) | 封装 Runnable 对象成为线程对象，并指定线程名称 |

>Thread 类还提供了诸如：yield、interrupt、守护线程、线程优先级等线程的控制方法，在开发中很少使用，这些方法会后续需要用到的时候再讲解。

### 什么是线程安全问题？

-   多个线程，同时操作同一个共享资源的时候，可能会出现业务安全问题；

举例：取钱的线程安全问题

-   场景：小明和小红是一对夫妻，他们有一个共同的账户，余额是 10 万元，如果小明和小红同时来取钱，并且 2 人各自都在取钱 10 万元，可能会出现什么问题呢？

![取钱的线程安全问题](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250617122519746.png)

线程安全问题出现的原因？

-   存在 **多个线程** 同时执行；
-   同时访问同一个 **共享资源**；
-   存在 **修改** 该共享资源；

**模拟线程安全问题的场景：取钱**

示例代码：

```java
// 主类
public class ThreadDemo1 {
    public static void main(String[] args) {
        // 目标：模拟线程安全问题。
        // 1、设计一个账户类：用于创建小明和小红的共同账户对象，存入10万。
        Account acc = new Account("ICBC-110", 100000);

        // 2、设计线程类：创建小明和小红两个线程，模拟小明和小红同时去同一个账户取款10万。
        new DrawThread("小明", acc).start();
        new DrawThread("小红", acc).start();
    }
}

// 模拟银行账户类
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Account {
    private String cardId; // 卡号
    private double money; // 余额

    // 小明和小红都到这里来了取钱
    public void drawMoney(double money) {
        // 拿到当前谁来取钱。
        String name = Thread.currentThread().getName();
        // 判断余额是否足够
        if (this.money >= money) {
            // 余额足够，取钱
            System.out.println(name + "取钱成功，吐出了" + money + "元成功！");
            // 更新余额
            this.money -= money;
            System.out.println(name + "取钱成功，取钱后，余额剩余" + this.money + "元");

        } else {
            // 余额不足
            System.out.println(name + "取钱失败，余额不足");
        }
    }
}


// 取钱线程类
public class DrawThread extends Thread{
    private Account acc; // 记住线程对象要处理的账户对象。

    public DrawThread(String name, Account acc) {
        super(name);
        this.acc = acc;
    }

    @Override
    public void run() {
        // 小明 小红 取钱
        acc.drawMoney(100000);
    }
}
```

#### 线程同步

-   线程同步是线程安全问题的解决方案。

核心思想：让多个线程先后依次访问共享资源，这样就可以避免出现线程安全问题；

实现方案：

-   加锁：每次只允许一个线程加锁，加锁后才能进入访问，访问完毕后自动解锁，然后其他线程才能再加锁进来。

##### 方式一：同步代码块；

```java
synchronized(同步锁){
	访问共享资源的核心代码
}
```

<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">原理：每次只允许一个线程加锁进来，执行完毕后自动解锁，然后其他线程才可以进来执行；</span>

>   **注意事项：对于当前同步执行的线程来说，同步锁必须是同一把（同一个对象），否则一个线程抢到锁，不能阻止其他线程继续执行“访问共享资源的核心代码”；**

-   锁对象不要随便选择一个唯一的对象，这样不好，可能会影响到其他无关线程的执行；
-   **建议使用共享资源作为锁对象**，对于实例方法建议用 `this` 作为锁对象；
-   对于静态方法建议使用字节码（类名.class）对象作为锁对象；

##### 方式二：同步方法；

-   <span style="background:#6fe7dd; border-radius:5px; display:inline-block;">原理：把访问共享资源的核心方法给上锁，以此保证线程安全；</span>
-   每次只能一个线程进入该方法，执行完毕以后自动解锁，其他线程才可以进来执行；

底层原理：

-   同步方法其实底层也是有隐式锁对象的，只是锁的范围是整个方法代码；
-   如果方法是实例方法：同步方法默认用 `this` 作为锁；
-   如果方法是静态方法：同步方法默认用 `类名.class` 作为锁；

同步代码块和同步方法哪个好？

-   范围上：同步代码块锁的范围更小，同步方法锁的范围更大；使用同步代码块理论上性能略高；
-   可读性：同步方法更好；

##### 方式三：lock 锁；

-   Lock 锁是 JDK5 开始提供的一个新的锁定操作，通过它可以创建出锁对象来进行加锁和解锁，更灵活、更方便、更强大。
-   Lock 是接口，不能直接实例化，可以采用它的实现类 `ReentrantLock` 来构建 Lock 锁对象；

Lock 的常用方法：

| 方法名称      | 说明   |
| ------------- | ------ |
| void lock()   | 获得锁 |
| void unlock() | 释放锁 |

>   **注意事项：**
>
>   -   **建议给锁对象加上 final 修饰，放在被别人篡改；**
>   -   **建议将释放锁的操作放到 finally 代码块中，这样无论是否出现异常，都可以确保锁用完了一定会被释放**

核心实现代码：

```java
// 方法一：同步代码块
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Account {
    private String cardId; // 卡号
    private double money; // 余额

    // 小明和小红都到这里来了取钱
    public void drawMoney(double money) {
        // 拿到当前谁来取钱。
        String name = Thread.currentThread().getName();
        // 判断余额是否足够
        synchronized (this) {	// 上锁，先抢到锁的人，判断余额是否充足，取完钱，更新完余额再解锁
            if (this.money >= money) {
                // 余额足够，取钱
                System.out.println(name + "取钱成功，吐出了" + money + "元成功！");
                // 更新余额
                this.money -= money;
                System.out.println(name + "取钱成功，取钱后，余额剩余" + this.money + "元");

            } else {
                // 余额不足
                System.out.println(name + "取钱失败，余额不足");
            }
        }
    }
}

// 方法二：同步方法
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Account {
    private String cardId; // 卡号
    private double money; // 余额

    // 小明和小红都到这里来了取钱，synchronized关键字修饰，给方法上锁；
    public synchronized void drawMoney(double money) {
        // 拿到当前谁来取钱。
        String name = Thread.currentThread().getName();
        // 判断余额是否足够
        if (this.money >= money) {
            // 余额足够，取钱
            System.out.println(name + "取钱成功，吐出了" + money + "元成功！");
            // 更新余额
            this.money -= money;
            System.out.println(name + "取钱成功，取钱后，余额剩余" + this.money + "元");

        } else {
            // 余额不足
            System.out.println(name + "取钱失败，余额不足");
        }
    }
}

// 方法三：同步锁
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Account {
    private String cardId; // 卡号
    private double money; // 余额
    private final Lock lk = new ReentrantLock(); // 使用final修饰，保护锁对象

    // 小明和小红都到这里来了取钱
    public void drawMoney(double money) {
        // 拿到当前谁来取钱。
        String name = Thread.currentThread().getName();
        lk.lock(); // 上锁
        try {
            // 判断余额是否足够
            if (this.money >= money) {
                // 余额足够，取钱
                System.out.println(name + "取钱成功，吐出了" + money + "元成功！");
                // 更新余额
                this.money -= money;
                System.out.println(name + "取钱成功，取钱后，余额剩余" + this.money + "元");
            } else {
                // 余额不足
                System.out.println(name + "取钱失败，余额不足");
            }
        } finally {
            // 建议将释放锁的操作放到finally代码块中，这样无论是否出现异常，都可以确保锁用完了一定会被释放
            lk.unlock();	// 解锁
        }
    }
}
```



### 线程池

线程池就是一个可以复用线程的技术；

**如果不使用线程池，用户每发起一个请求，后台就需要创建一个新线程来处理，下次同样的任务来了又要创建新线程处理，创建新线程的开销很大，并且请求过多时，会产生大量的线程出来，会严重影响系统的性能。**

#### 线程池的工作原理：

<img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250617195255243.png" alt="线程池的工作原理" style="zoom:67%;" />

线程池中的线程就好比餐馆里的服务员，任务队列就好比来吃饭的顾客，一个服务员一次服务一位顾客，服务结束后，不会把服务员炒鱿鱼，因为如果炒掉下次再来顾客又要雇新的服务员；而是让他继续服务下一位顾客，也就是任务队列中源源不断地顾客；

#### 创建线程池

JDK5.0 提供了代表线程池的接口：`ExecutorService`

如何创建线程池对象？

##### 方式一：使用 ExecutorService 的实现类 ThreadPoolExecutor 来创建一个线程池对象；

| ThreadPoolExecutor 类提供的构造器                             | 作用                                       |
| ------------------------------------------------------------ | ------------------------------------------ |
| public **ThreadPoolExecutor**(`int  corePoolSize`, `int  maximumPoolSize`,  `long  keepAliveTime`, `TimeUnit unit`, `BlockingQueue<Runnable>  workQueue`, `ThreadFactory threadFactory`,   `RejectedExecutionHandler handler`) | 使用指定的初始化参数创建一个新的线程池对象 |

**各个参数含义：**

-   参数一：`corePoolSize` : 指定线程池的核心线程的数量
-   参数二：`maximumPoolSize`：指定线程池的最大线程数量
-   参数三：`keepAliveTime` ：指定临时线程的存活时间
-   参数四：`unit`：指定临时线程存活的时间单位(秒、分、时、天）
-   参数五：`workQueue`：指定线程池的任务队列
-   参数六：`threadFactory`：指定线程池的线程工厂
-   参数七：`handler`：指定线程池的 **任务拒绝策略**（线程都在忙，任务队列也满了的时候，新任务来了该怎么处理）

**ExecutorService 的常用方法**

| 方法名称                            | 说明                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| void execute(Runnable command)      | 执行 **Runnable** 任务                                        |
| Future <T>  submit(Callable <T> task) | 执行 **Callable** 任务，返回未来任务对象，用于获取线程返回的结果 |
| void  shutdown()                    | 等全部任务执行完毕后，再关闭线程池！                         |
| List <Runnable> shutdownNow()        | 立刻关闭线程池，停止正在执行的任务，并返回队列中未执行的任务 |

**线程池注意事项：**

-   什么时候开始创建临时线程？新任务提交时发现核心线程都在忙，任务队列也满了，并且还可以创建临时线程，此时才会创建临时线程；
-   什么时候会拒绝新任务？核心线程和临时线程都在忙，任务队列也满了，新的任务过来的时候才会开始拒绝任务；

**任务拒绝策略：**

| 策略                                     | 说明                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| ThreadPoolExecutor.AbortPolicy()         | 丢弃任务并抛出 `RejectedExecutionException` 异常。是默认的策略 |
| ThreadPoolExecutor.DiscardPolicy()       | 丢弃任务，但是不抛出异常，这是不推荐的做法                   |
| ThreadPoolExecutor.DiscardOldestPolicy() | 抛弃队列中等待最久的任务  然后把当前任务加入队列中           |
| ThreadPoolExecutor.CallerRunsPolicy()    | 由主线程负责调用任务的 run()方法从而绕过线程池直接执行        |

示例代码：

```java
public class ExecutorServiceDemo1 {
    public static void main(String[] args) {
        // 目标：创建线程池对象来使用。
        // 1、使用线程池的实现类ThreadPoolExecutor声明七个参数来创建线程池对象。
        ExecutorService pool = new ThreadPoolExecutor(3, 5,
                10, TimeUnit.SECONDS, new ArrayBlockingQueue<>(3),
               Executors.defaultThreadFactory(), new ThreadPoolExecutor.CallerRunsPolicy());

        // 2、使用线程池处理任务！看会不会复用线程？
        Runnable target = new MyRunnable();
        pool.execute(target); // 提交第1个任务 创建第1个线程 自动启动线程处理这个任务
        pool.execute(target); // 提交第2个任务 创建第2个线程 自动启动线程处理这个任务
        pool.execute(target); // 提交第2个任务 创建第3个线程 自动启动线程处理这个任务
        pool.execute(target);
        pool.execute(target);
        pool.execute(target);
        // 只有当所有的核心线程都在忙，而且任务队列也排满了的时候，才会创建临时线程；
        pool.execute(target); // 到了临时线程的创建时机了
        pool.execute(target); // 到了临时线程的创建时机了
        pool.execute(target); // 到了任务拒绝策略了，忙不过来

        // 3、关闭线程池 ：一般不关闭线程池。
        // pool.shutdown(); // 等所有任务执行完毕后再关闭线程池！
        // pool.shutdownNow(); // 立即关闭，不管任务是否执行完毕！
    }
}


public class ExecutorServiceDemo2 {
    public static void main(String[] args) {
        // 目标：创建线程池对象来使用。
        // 1、使用线程池的实现类ThreadPoolExecutor声明七个参数来创建线程池对象。
        ExecutorService pool = new ThreadPoolExecutor(3, 5,
                10, TimeUnit.SECONDS, new ArrayBlockingQueue<>(3),
               Executors.defaultThreadFactory(), new ThreadPoolExecutor.CallerRunsPolicy());

        // 2、使用线程池处理Callable任务！
        Future<String> f1 = pool.submit(new MyCallable(100));
        Future<String> f2 = pool.submit(new MyCallable(200));
        Future<String> f3 = pool.submit(new MyCallable(300));
        Future<String> f4 = pool.submit(new MyCallable(400));

        try {
            System.out.println(f1.get());
            System.out.println(f2.get());
            System.out.println(f3.get());
            System.out.println(f4.get());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

##### 方式二：使用 Executors（线程池的工具类）调用方法来返回不同特点的线程池对象；

-   Executors 是一个线程池工具类，提供了很多静态方法用于返回不同特点的线程池对象；


| 方法名称                                                     | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| public static newFixedThreadPool(int nThreads)               | 创建固定线程数量的线程池，如果某个线程因为执行异常而结束，那么线程池会补充一个新线程替代它。 |
| public  static ExecutorService newSingleThreadExecutor()     | 创建只有一个线程的线程池对象，如果该线程出现异常而结束，那么线程池会补充一个新线程。 |
| public  static ExecutorService newCachedThreadPool()         | 线程数量随着任务增加而增加，如果线程任务执行完毕且空闲了 60s 则会被回收掉。 |
| public  static ScheduledExecutorService newScheduledThreadPool(int corePoolSize) | 创建一个线程池，可以实现在给定的延迟后运行任务，或者定期执行任务。 |

**注意 ：这些方法的底层，都是通过线程池的实现类 ThreadPoolExecutor 创建的线程池对象**

Executors 使用可能存在的陷阱

-   大型并发系统环境中使用 Executors 如果不注意可能会出现系统风险

<img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250617202153455.png" alt="阿里巴巴Java开发手册" style="zoom: 80%;" />

## 网络编程

指的是可以让设备中的程序与网络上其他设备中的程序进行数据交互的技术（实现网络通信）

基本的通信架构

-   基本的通信架构有2种形式：CS架构（Client客户端/Server服务端）、BS架构（Browser浏览器/Server服务端）

<img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250620170554912.png" alt="客户端-服务端架构" style="zoom:60%;" />

<img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250620170718472.png" alt="浏览器-服务端架构" style="zoom:60%;" />

无论是CS架构、还是BS架构的软件都必须依赖网络编程！

### 网络编程三要素

#### IP

IP地址是设备在网络中的地址，是设备在网络中的唯一标识；

**IP地址版本:**

IPv4:是一个32位的地址，通常用“点分十进制”表示法书写，例如 `192.168.1.66`

IPv6:是一个128位的地址，旨在为海量的网络设备提供地址。它通常使用“冒分十六进制”表示法，例如 `2001:0db8:0000:0023:0008:0800:200c:417a`

 **IP地址类型:**

-   公网IP:可以直接连接到互联网的IP地址 
-   内网IP (局域网IP): 仅在组织机构内部使用的IP地址，例如以 `192.168.`开头的地址 ，范围为`192.168.0.0--192.168.255.255`
-   本机IP:`127.0.0.1`或 `localhost`都代表当前设备自己的IP地址 

**域名系统 (DNS):** DNS是一个分布式命名系统，它负责将人类易于记忆的域名（如 `www.itheima.com`）转换为机器能够识别的IP地址 。

**Java中的 `InetAddress` 类:** 这个类在Java中代表一个IP地址 。

核心方法:

-   `getLocalHost()`: 获取本机的 InetAddress对象 
-   `getByName(String host)`: 根据主机名或IP地址字符串获取 InetAddress对象
-   `getHostName()`: 获取IP地址对应的主机名 
-   `getHostAddress()`: 获取IP地址的字符串表示 
-   `isReachable(int timeout)`: 在指定的毫秒数内测试该IP地址是否可达 

**常用命令:**

-   `ipconfig`: 查看本机的IP地址 
-   `ping <IP地址>`: 检查与另一个网络的连通性 

示例代码：

```java
public class InetAddressDemo1 {
    public static void main(String[] args) {
        // 目标：认识InetAddress获取本机IP对象和对方IP对象。
        try {
            // 1.获取本机IP对象
            InetAddress ip1 = InetAddress.getLocalHost();
            System.out.println(ip1.getHostName());          // LAPTOP-AGQHL0AG 本机设备名称
            System.out.println(ip1.getHostAddress());       // 172.24.144.1

            // 2、获取对方IP对象，获取百度官网的IP对象
            InetAddress ip2 = InetAddress.getByName("www.baidu.com");
            System.out.println(ip2.getHostName());
            System.out.println(ip2.getHostAddress());

           // 3、判断本机与对方主机在5000ms内是否互通
            System.out.println(ip2.isReachable(5000)); // false ping
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
```



#### 端口

应用程序在设备中的唯一标识；它是一个16位的数字，范围从0到65535，用于区分一台计算机上正在运行的不同程序；

端口分类：

-   周知端口（0-1023）：被预先定义的知名应用占用（例如HTTP占用80端口）
-   注册端口（1024-49151）：分配给用户进程或者某些应用程序；
-   动态端口（49152-65535）：通常是动态分配给客户端程序的临时端口；

在同一台设备上，不能有两个程序的端口号相同，否则会引发端口冲突错误；

#### 协议

网络通信协议是网络上通信的设备间事先规定好的连接和数据传输的规则，目前事实上的国际标准是TCP/IP网络模型；

### UDP通信

UDP（User Datagram Protocol）：用户数据报协议

UDP通信效率高，应用场景有视频直播、语音通话；

特点：不事先建立连接，数据按照包发送，一个包的数据包含：自己的IP、端口，目的地的IP、端口，以及要发送的数据（限制在64KB内）；发送方不管对方是否在线，数据在中间丢失也不管，如果接收方收到数据也不返回确认，因此是不可靠的；

示例代码：

```java
// 客户端实现，客户端通过DatagramSocket创建发送端对象
// 通过DatagramPacket建立发送数据包对象，指定要发送的字节流、字节流长度、目的地IP、端口号
public class UDPClientDemo1 {
    public static void main(String[] args) throws Exception {
        // 目标：完成UDP通信一发一收：客户端开发
        System.out.println("===客户端启动==");
        // 1、创建发送端对象（代表抛韭菜的人） DatagramSocket()用于创建UDP通信的客户端和服务端
        DatagramSocket socket = new DatagramSocket(); // 随机端口

        // 2、创建数据包对象封装要发送的数据。(韭菜盘子)
        byte[] bytes = "我是客户端，约你今晚啤酒、龙虾、小烧烤".getBytes();
        /**
         *   public DatagramPacket(byte[] buf, int length,
         *                           InetAddress address, int port)
         * 参数一：发送的数据，字节数组（韭菜）
         * 参数二：发送的字节长度。
         * 参数三：目的地的IP地址。
         * 参数四：服务端程序的端口号
         */
        DatagramPacket packet = new DatagramPacket(bytes, bytes.length, InetAddress.getLocalHost(), 8080);

        // 3、让发送端对象发送数据包的数据
        socket.send(packet);

        socket.close();
    }
}


// 服务端程序开发
// 先启动服务端程序，开启监听状态，接收到客户端发来的消息后，打印该消息
public class UDPServerDemo2 {
    public static void main(String[] args) throws Exception {
        // 目标：完成UDP通信一发一收：服务端开发。
        System.out.println("==服务端启动了===");
        // 1、创建接收端对象，注册端口。（接韭菜的人）
        DatagramSocket socket = new DatagramSocket(8080);

        // 2、创建一个数据包对象负责接收数据。（韭菜盘子）
        byte[] buf = new byte[1024 * 64];
        DatagramPacket packet = new DatagramPacket(buf, buf.length);

        // 3、接收数据，将数据封装到数据包对象的字节数组中去
        socket.receive(packet);

        // 4、看看数据是否收到了
        int len = packet.getLength();   // 获取当前收到的数据长度。
        String data = new String(buf, 0 , len);
        System.out.println("服务端收到了：" + data);

        // 获取对方的ip对象和程序端口
        String ip = packet.getAddress().getHostAddress();
        int port = packet.getPort();
        System.out.println("对方ip：" + ip + "   对方端口：" + port);

        socket.close();
    }
}
```

通过死循环实现多次对话

```java
public class UDPClientDemo1 {
    public static void main(String[] args) throws Exception {
        // 目标：完成UDP通信多发多收：客户端开发
        System.out.println("===客户端启动==");
        // 1、创建发送端对象（代表抛韭菜的人）
        DatagramSocket socket = new DatagramSocket(); // 随机端口

        Scanner sc = new Scanner(System.in);
        while (true) {
            // 2、创建数据包对象封装要发送的数据。(韭菜盘子)
            System.out.println("请说：");
            String msg = sc.nextLine();

            // 如果用户输入的是 exit，则退出
            if ("exit".equals(msg)) {
                System.out.println("===客户端退出==");
                socket.close();
                break;
            }

            byte[] bytes = msg.getBytes();
            DatagramPacket packet = new DatagramPacket(bytes, bytes.length,
                    InetAddress.getLocalHost(), 8080);

            // 3、让发送端对象发送数据包的数据
            socket.send(packet);
        }

    }
}


public class UDPServerDemo2 {
    public static void main(String[] args) throws Exception {
        // 目标：完成UDP通信多发多收：服务端开发。
        System.out.println("==服务端启动了===");
        // 1、创建接收端对象，注册端口。（接韭菜的人）
        DatagramSocket socket = new DatagramSocket(8080);

        // 2、创建一个数据包对象负责接收数据。（韭菜盘子）
        byte[] buf = new byte[1024 * 64];
        DatagramPacket packet = new DatagramPacket(buf, buf.length);

        while (true) {
            // 3、接收数据，将数据封装到数据包对象的字节数组中去
            socket.receive(packet); // 等待式接收数据。

            // 4、看看数据是否收到了
            int len = packet.getLength();   // 获取当前收到的数据长度。
            String data = new String(buf, 0 , len);
            System.out.println("服务端收到了：" + data);

            // 获取对方的ip对象和程序端口
            String ip = packet.getAddress().getHostAddress();
            int port = packet.getPort();
            System.out.println("对方ip：" + ip + "   对方端口：" + port);

            System.out.println("----------------------------------------------");
        }
    }
}
```

### TCP通信

特点：面向连接、可靠通信；

TCP的最终目的：要保证在不可靠的信道上实现可靠的数据传输；

TCP主要通过三个步骤实现可靠传输：三次握手建立连接，传输数据进行确认，四次挥手断开连接；

### 综合案例

































## Java 高级技术

### 单元测试

指的是针对最小的功能单元方法，编写测试代码对其进行正确性测试；

咱们之前是如何进行单元测试的？在 main 方法中调用该方法，编写测试代码，人为观测结果和预期是否一致；**存在的问题：**

-   只能在 main 方法编写测试代码，来调用其他方法进行测试；
-   无法实现自动化测试，一个方法测试失败，可能会影响其他方法测试；
-   无法得到测试的报告，需要程序员自己去观察测试是否成功；

Junit 单元测试框架

为了解决上述问题，可以用 Junit 单元测试框架来对代码进行测试，由第三方公司开源（很多开发工具已经集成了 Junit 框架，比如 Idea）

优点：

-   **可以灵活的编写测试代码，可以针对某个方法执行测试，也支持一键完成对全部方法的自动化测试，且各自独立；**
-   不需要程序员去分析测试的结果，会 **自动生成测试报告** 出来；

Junit 单元测试的使用步骤

需求：某个系统，有多个业务方法，请使用 Junit 单元测试框架，编写测试代码，完成对这些方法的正确性测试；

具体步骤：

1.  将 Junit 框架的 jar 包导入到项目中（注意：Idea 中已经集成了 Junit 框架，不需要我们自己手工导入了）；
2.  为需要测试的业务类，定义对应的测试类，并为每个业务方法，编写对应的 **测试方法（要求：公开、无参、无返回值）；**
3.  测试方法上 **必须声明 `@Test`** 注解，然后在测试方法中，编写代码调用<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">被测试的业务方法</span>进行测试；
4.  开始测试，选中测试方法，右键选择“Junit 运行”，如果测试通过则是绿色；如果测试失败，则是红色；

示例代码：

```java
/**
 * 字符串工具类
 */
public class StringUtil {
    // 工具一：获取给定字符串的长度；
    public static void printNumber(String name){
        if(name == null){
            System.out.println("参数为null！请注意");
            return;
        }
        System.out.println("名字长度是：" + name.length());
    }


     // 工具二：获取字符串的最大索引
    public static int getMaxIndex(String data){
        if(data == null || "".equals(data)) {
            return -1;
        }
        return data.length() - 1;
    }
}

// 测试类：junit单元测试框架，对业务类中的业务方法进行正确性测试。
public class StringUtilTest {
    // 测试方法：必须是公开public，无参，无返回值。
    // 测试方法必须加上@Test注解（Junit框架的核心步骤）
    @Test
    public void testPrinNumber() {
        // 测试步骤：
        StringUtil.printNumber("张三abc"); // 5
        // 测试用例
        StringUtil.printNumber("");
        StringUtil.printNumber(null);
    }

    @Test
    public void testGetMaxIndex() {
        // 测试步骤：
        int index = StringUtil.getMaxIndex("abcdefg"); // 6
        // 测试用例
        int index2 = StringUtil.getMaxIndex("");
        int index3 = StringUtil.getMaxIndex(null);

        System.out.println(index);
        System.out.println(index2);
        System.out.println(index3);

        // 做断言：断言结果是否与预期结果一致
        Assert.assertEquals("本轮测试失败，业务获取的最大索引有问题！请检查",6, index);
        Assert.assertEquals("本轮测试失败，业务获取的最大索引有问题！请检查",-1, index2);
        Assert.assertEquals("本轮测试失败，业务获取的最大索引有问题！请检查",-1, index3);
    }
}
```

### 反射

#### 认识反射、获取类

反射（Reflection）是 Java 语言提供的一种运行时动态操作类、对象、方法和属性的机制。通过反射，程序可以在运行时检查和修改类、接口、字段、方法等信息，甚至可以动态调用方法或创建对象，而无需在编译时知道这些信息。

反射是 Java 的运行时特性，允许程序 **在运行时动态获取类的元数据（如类名、方法、构造函数、字段等），并通过这些元数据操作类或对象**。反射的核心类和接口主要位于 `java.lang.reflect` 包中，常用的类包括：

-   `Class`：表示运行时的类或接口。

-   `Field`：表示类的成员变量（字段）。

-   `Method`：表示类的方法。

-   `Constructor`：表示类的构造函数

通过反射，程序可以动态地：

-   获取类的结构信息（方法、字段、构造函数等）。
-   创建对象。
-   调用方法或修改字段值。
-   绕过访问权限限制（例如访问私有字段或方法）

##### 反射第一步，获取类的 class 对象（类本身）

示例代码提供了获取类的 class 对象的三种方式：

```java
public class ReflectDemo1 {
    public static void main(String[] args) throws Exception {
        // 目标：掌握反射第一步操作：或者类的Class对象。（获取类本身）。
        // 1、获取类本身：类.class
        Class c1 = Student.class;
        System.out.println(c1);

        // 2、获取类本身：Class.forName("类的全类名")
        Class c2 = Class.forName("com.itheima.demo2reflect.Student");
        System.out.println(c2);

        // 3、获取类本身：对象.getClass()
        Student s = new Student();
        Class c3 = s.getClass();
        System.out.println(c3);

        System.out.println(c1 == c2); // true
        System.out.println(c2 == c3); // true
    }
}
```

##### 反射获取类中的成分并操作

Class 类提供了从类中 **获取构造器** 的方法：

| 方法                                                         | 说明                                   |
| ------------------------------------------------------------ | -------------------------------------- |
| Constructor <?> []  getConstructors()                          | 获取全部构造器（只能获取 public 修饰的） |
| Constructor <?> []  **getDeclaredConstructors**()              | 获取全部构造器（只要存在就能拿到）     |
| Constructor <T>  getConstructor(Class <?>...  parameterTypes)  | 获取某个构造器（只能获取 public 修饰的） |
| Constructor <T>  **getDeclaredConstructor**(Class <?>...  parameterTypes) | 获取某个构造器（只要存在就能拿到）     |

获取类构造器的作用：依然是初始化对象返回

| Constructor 提供的方法                   | 说明                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| T newInstance(Object... initargs)       | 调用此构造器对象表示的构造器，并传入参数，完成对象的初始化并返回 |
| public void setAccessible(boolean flag) | 设置为 true，表示 **禁止检查** 访问控制（暴力反射）             |

<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">暴力反射可以访问私有的构造器、方法、属性</span>

---

Class 类提供了从类中获取 **成员变量** 的方法：

| 方法                                       | 说明                                         |
| ------------------------------------------ | -------------------------------------------- |
| public Field [] getFields()                 | 获取类的全部成员变量（只能获取 public 修饰的） |
| public Field [] getDeclaredFields()         | 获取类的全部成员变量（只要存在就能拿到）     |
| public Field getField(String name)         | 获取类的某个成员变量（只能获取 public 修饰的） |
| public Field getDeclaredField(String name) | 获取类的某个成员变量（只要存在就能拿到）     |

获取到成员变量的目的：依然是给成员变量进行赋值、或者取值；

| 方法                                    | 说明                                             |
| --------------------------------------- | ------------------------------------------------ |
| void set(Object obj, Object value)：    | 赋值                                             |
| Object get(Object obj)                  | 取值                                             |
| public void setAccessible(boolean flag) | 设置为 true，表示 **禁止检查** 访问控制（暴力反射） |

---

Class 提供了从类中获取 **成员方法** 的 API

| 方法                                                         | 说明                                         |
| ------------------------------------------------------------ | -------------------------------------------- |
| Method [] getMethods()                                        | 获取类的全部成员方法（只能获取 public 修饰的） |
| Method [] getDeclaredMethods()                                | 获取类的全部成员方法（只要存在就能拿到）     |
| Method getMethod(String name, Class <?>... parameterTypes)    | 获取类的某个成员方法（只能获取 public 修饰的） |
| Method getDeclaredMethod(String name, Class <?>... parameterTypes) | 获取类的某个成员方法（只要存在就能拿到）     |

获取成员方法的目的：执行成员方法

| Method 提供的方法                                 | 说明                                             |
| ------------------------------------------------ | ------------------------------------------------ |
| public Object invoke(Object obj, Object... args) | 触发某个对象的该方法执行。                       |
| public void setAccessible(boolean flag)          | 设置为 true，表示 **禁止检查** 访问控制（暴力反射） |



示例代码：

```java
public class ReflectDemo2 {
    @Test
    public void getClassInfo(){
        // 目标：获取类的信息。
        // 1、反射第一步：或者Class对象，代表拿到类。
        Class c1 = Student.class;
        System.out.println(c1.getName()); // 类名的全类名 com.itheima.demo2reflect.Student
        System.out.println(c1.getSimpleName()); // 类名 Student
    }

    // 2、获取类的构造器对象并对其进行操作。
    @Test
    public void getConstructorInfo() throws Exception {
        // 目标：获取类的构造器对象并对其进行操作。
        // 1、反射第一步：或者Class对象，代表拿到类。
        Class c1 = Dog.class;
        // 2、获取构造器对象。
        Constructor[] cons = c1.getDeclaredConstructors();
        for (Constructor con : cons) {
            // getParameterCount()获取构造器的参数个数
            System.out.println(con.getName() + "(" + con.getParameterCount() + ")");
        }
        // 3、获取单个构造器
        Constructor con = c1.getDeclaredConstructor(); // 无参数构造器
        System.out.println(con.getName() + "(" + con.getParameterCount() + ")");

        Constructor con2 = c1.getDeclaredConstructor(String.class, int.class); // 2个参数的有参数构造器
        System.out.println(con2.getName() + "(" + con2.getParameterCount() + ")");

        // 4、获取构造器的作用依然是创建对象：创建对象。
        // 暴力反射：暴力反射可以访问私有的构造器、方法、属性。
        con.setAccessible(true); // 绕过访问权限，直接访问！
        Dog d1 = (Dog) con.newInstance();
        // System.out.println(d1.name);
        System.out.println(d1);

        Dog d2 = (Dog)con2.newInstance("小黑", 3);
        System.out.println(d2);
    }

    // 3、获取类的成员变量对象并对其进行操作。
    @Test
    public void getFieldInfo() throws Exception {
        // 目标：获取类的成员变量对象并对其进行操作。
        // 1、反射第一步：或者Class对象，代表拿到类。
        Class c1 = Dog.class;
        // 2、获取成员变量对象。
        Field[] fields = c1.getDeclaredFields();
        for (Field field : fields) {
            System.out.println(field.getName() + "(" + field.getType().getName() + ")");
        }
        // 3、获取单个成员变量对象。
        Field field = c1.getDeclaredField("hobby");
        // field.setAccessible(true);
        // System.out.println(c1.getName());
        System.out.println(field.getName() + "(" + field.getType().getName() + ")");

        Field field2 = c1.getDeclaredField("age");
        System.out.println(field2.getName() + "(" + field2.getType().getName() + ")");

        // 4、获取成员变量的目的依然是取值和赋值。
        Dog d = new Dog("泰迪", 3);
        field.setAccessible(true); // 绕过访问权限，直接访问！
        field.set(d, "社交");  //   d.setHobby("社交");
        System.out.println(d);

        String hobby = (String) field.get(d); // d.getHobby();
        System.out.println(hobby);

    }

    // 4、获取类的成员方法对象并对其进行操作。
    @Test
    public void getMethodInfo() throws Exception {
        // 目标：获取类的成员方法对象并对其进行操作。
        // 1、反射第一步：或者Class对象，代表拿到类。
        Class c1 = Dog.class;
        // 2、获取成员方法对象。
        Method[] methods = c1.getDeclaredMethods();
        for (Method method : methods) {
            System.out.println(method.getName() + "(" + method.getParameterCount() + ")");
        }
        // 3、获取单个成员方法对象。
        Method m1 = c1.getDeclaredMethod("eat");// 获取是无参数的eat方法
        Method m2 = c1.getDeclaredMethod("eat", String.class);// 获取是有参数的eat方法
        System.out.println(m1.getName() + "(" + m1.getParameterCount() + ")");
        System.out.println(m2.getName() + "(" + m2.getParameterCount() + ")");

        // 4、获取成员方法的目的依然是调用方法。
        Dog d = new Dog("泰迪", 3);
        m1.setAccessible(true); // 绕过访问权限，直接访问！
        Object rs1 = m1.invoke(d); // 唤醒对象d的eat方法执行，相当于 d.eat();
        System.out.println(rs1); // null

        Object rs2 = m2.invoke(d, "牛肉"); // 唤醒对象d的eat带String参数的方法执行，相当于 d.eat("牛肉");
        System.out.println(rs2);
    }
}



package com.itheima.demo2reflect;

public class Dog {
    private String name;
    private int age;
    private String hobby;
    // 无参构造器
    private Dog() {
        System.out.println("无参数构造器执行了~~");
    }
    // 带一个参数的构造器
    private Dog(String name) {
        System.out.println("1个参数有参数构造器执行了~~");
        this.name = name;
    }
    // 带两个参数的构造器
    public Dog(String name, int age) {
        System.out.println("2个参数有参数构造器执行了~~");
        this.name = name;
        this.age = age;
    }
    // 不带参数的eat()方法
    private void eat(){
        System.out.println("狗吃骨头！");
    }
    // 带一个参数的eat()方法
    public String eat(String name){
        System.out.println("狗吃" + name);
        return "狗说：谢谢！谢谢！汪汪汪！";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getHobby() {
        return hobby;
    }

    public void setHobby(String hobby) {
        this.hobby = hobby;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", hobby='" + hobby + '\'' +
                '}';
    }
}

```



#### 反射的作用、应用场景

反射的作用：

-   拿到一个类的 class 本身的全部成分然后进行操作；
-   可以破坏封装性（通过暴力反射访问私有构造器、成员变量、成员方法）；
-   可以绕过泛型的约束；
-   最重要的用途：适合做 Java 的框架，基本上主流的框架都会基于反射设计出一些通用的功能；

示例代码：

```java
public class ReflectDemo3 {
    public static void main(String[] args) throws Exception {
        // 目标：反射的基本作用。
        // 1、类的全部成分的获取
        // 2、可以破坏封装性
        // 3、可以绕过泛型的约束。
        ArrayList<String> list = new ArrayList<>();
        list.add("张无忌");
        list.add("令狐冲");
        list.add("东方不败");
        // list.add(9.9);
        // list.add(true);

        // 反射绕过泛型约束的原理：泛型在编译得到字节码时，会擦除泛型信息。
        Class c1 = list.getClass(); // c1 == ArrayList.class
        // 逆向获取 ArrayList 类的add方法
        Method add = c1.getDeclaredMethod("add", Object.class);
        // 触发list集合对象的add方法执行。
        add.invoke(list, 9.9); // 翻墙
        add.invoke(list, true); // 翻墙
        System.out.println(list);
    }
}
```

使用反射做一个简易版的框架，需求：

-   对于 **任意** 一个对象，该框架都可以把 **对象的字段名和对应的值**，保存到文件中去；

分析：如果只是简单的用一个方法来接收一个对象，来获取它的所有字段名和对应的值，无法实现对任意对象都通用；因此可以想到应该使用泛型，通过泛型来实现接收任意一个对象的功能（或者使用所有对象的祖宗类 Object，用多态来实现接收不同类型的对象），但接收一个对象前，我们并不知道该对象中有哪些字段名、更不知道字段名对应的值，就无法实现将它们写入到文件中，这里就需要用到刚才学的反射，对传进来的泛型对象，用反射获取该对象的 class 本身，从而获取它的所有 Filed 字段名和对应的字段值，再将它们写入到文件中；

实现代码如下：

```java
public class SaveObjectFrameWork {
    // 保存任意对象的静态方法
    public static void saveObject(Object obj) throws Exception {
        PrintStream ps = new PrintStream(new FileOutputStream("day06-junit-reflect-annotation-proxy/src/obj.txt", true));
        // obj 可能是学生  老师  狗
        // 只有反射可以直到对象有多少个字段：
        // 1. 获取Class对象
        Class c = obj.getClass();
        String simpleName = c.getSimpleName();
        ps.println("==============" + simpleName + "====================");
        // 2. 获取Class对象的所有字段。
        Field[] fields = c.getDeclaredFields();
        // 3. 遍历字段
        for (Field field : fields) {
            // 4. 获取字段的值
            // 4.1 获取字段名称
            String fieldName = field.getName();
            // 4.2 获取字段的值
            field.setAccessible(true); // 暴力反射
            Object fieldValue = field.get(obj) + "";
            // 5. 打印到文件中去
            ps.println(fieldName + "=" + fieldValue);
       }
       ps.close();
    }
}

public class ReflectDemo4 {
    public static void main(String[] args) throws Exception {
        // 目标：搞清楚反射的应用：做框架的通用技术。
        Dog d = new Dog("小黑", 3);
        SaveObjectFrameWork.saveObject(d);

        // 创建学生对象
        Student s = new Student("小明", 18, "爱问问题");
        SaveObjectFrameWork.saveObject(s);

        // 创建老师对象
        Teacher t = new Teacher("小红", 19, "java、前端、动漫", 3000, "422期", '女', "12345678901");
        SaveObjectFrameWork.saveObject(t);

    }
}
```

总结，反射的作用有哪些？

-   可以在运行时得到一个类的全部成分然后操作；
-   可以破坏封装性。（很突出）
-   也可以破坏泛型的约束性。（很突出）
-   更重要的用途是适合：做 Java 高级框架；
-   基本上主流框架都会基于反射设计一些通用技术功能。

### 注解

**一、注解的本质是什么？—— 一个可以被程序读取的“标签”**

**注解的本质就是元数据（Metadata），即“关于数据的数据”。**

如果这个定义太抽象，你可以把它理解成一个贴在代码（类、方法、字段等）上的 **“标签”** 或 **“说明书”**。

想象一下你整理箱子：

-   **代码**：就是箱子里的物品（衣服、书籍）。
-   **注释 (`//` 或 `/\* \*/`)**：是你用笔在箱子上写的字，比如“冬天的衣服”。这个字是**写给人看的**，帮助你自己或其他开发者理解。
-   **注解 (`@Override`)**：是一个标准化的、机器可读的**标签**，比如一个印有“易碎品”图标的贴纸。这个标签不是给人看的，而是给**搬运工（程序）**看的，告诉他要轻拿轻放。

**核心要点：**

1.  **注解本身不执行任何代码**：它就像那个“易碎品”标签，标签本身不会让箱子变得更坚固。它只是一个被动的、携带信息的标记。
2.  **注解为其他程序提供信息**：它的价值完全体现在“读取者”身上。没有读取和处理注解的程序，注解就毫无用处，等同于注释。

------

**二、怎么理解注解？—— 从“谁来读”和“何时读”的角度**

要真正理解注解，关键要明白**“谁”** 在 **“什么时候”** 读取这个“标签”，以及读取后会 **“做什么”**。

处理注解的程序主要有三类：

<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">1. 编译器（`javac`）在【编译时】读取</span>

这类注解主要用于辅助编译器进行静态检查，确保代码的正确性。

-   例子：`@Override`
    -   **你贴的标签**：在方法上写 `@Override`。
    -   **谁来读**：Java编译器。
    -   **何时读**：代码编译期间。
    -   **做什么**：编译器看到这个标签后，会去检查父类或接口中是否存在一个一模一样的方法。如果不存在，编译器就报错。它帮你避免了因拼写错误导致重写失败的问题。
-   例子：`@SuppressWarnings("deprecation")`
    -   **你贴的标签**：`@SuppressWarnings`。
    -   **谁来读**：编译器。
    -   **做什么**：告诉编译器“我知道这里用了一个过时的方法，别烦我，不要显示警告信息”。

<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">2. 框架或程序在【运行时】读取</span>

这是最常见、最强大的一种用法。程序在运行时，通过**反射（Reflection）**技术来查找代码中的注解，并根据注解信息执行相应的逻辑。

-   **例子：JUnit中的 `@Test`**

    -   **你贴的标签**：在测试方法上写 `@Test`。
    -   **谁来读**：JUnit测试框架。
    -   **何时读**：当你运行测试时。
    -   **做什么**：JUnit框架启动后，会扫描你的代码，通过反射找到所有贴了 `@Test` 标签的方法，然后自动执行这些方法，并生成测试报告。你不需要手动在 `main` 方法里一个一个调用它们。

-   **例子：Spring中的 `@Autowired` 和 `@Service`**

    -   **你贴的标签**：在类上写 `@Service`，在字段上写 `@Autowired`。

    -   **谁来读**：Spring IoC容器。

    -   **何时读**：应用程序启动和运行时。

    -   做什么

        ：

        1.  Spring启动时，会扫描所有类，把贴了 `@Service`, `@Component` 等标签的类创建实例，并放入一个“容器”中管理起来。
        2.  当发现某个对象的字段上贴了 `@Autowired` 标签时，Spring会自动从容器里找到匹配类型的实例，并注入（赋值）给这个字段。这一切都是自动完成的。

<span style="background:#6fe7dd; border-radius:5px; display:inline-block;">3. 工具在【编译时】处理并生成代码</span>

这是一类特殊的注解，它们在编译期间被读取，并用来**生成新的Java代码**，这些新生成的代码会和你的手写代码一起被编译。

-   例子：Lombok中的 `@Data`
    -   **你贴的标签**：在你的 `User` 类上写 `@Data`。
    -   **谁来读**：Lombok的注解处理器（一个编译器插件）。
    -   **何时读**：代码编译期间。
    -   **做什么**：Lombok看到 `@Data` 标签后，会自动为你这个类**生成** `getter`, `setter`, `toString()`, `equals()` 等方法的源代码。你虽然没写这些代码，但编译后的 `.class` 文件里是真实存在的。

**总结：如何形成一个完整的理解**

1.  **本质上，注解是元数据，是一个被动的“标签”**。它本身没有功能。
2.  **功能来源于“读取者”**。一个注解的意义完全取决于处理它的程序（编译器、框架等）。
3.  **它是一种“约定”**。你通过贴标签的方式，和框架之间形成一种约定。比如你用 `@Test` 和JUnit约定“这个方法是用来测试的”，用 `@Service` 和Spring约定“这个类交给你管理”。
4.  **它是“配置思路的演进”**。在早期，很多配置都写在独立的XML文件里。这种方式将配置和代码分离，但不够直观。注解将配置信息直接写在它所描述的代码旁边，实现了**“约定优于配置”（Convention over Configuration）**，让代码更简洁、更内聚。

所以，下次看到一个注解时，你可以这样问自己：

-   这个注解是给谁看的？（编译器？Spring？JUnit？）
-   它在什么时候被读取？（编译时？运行时？）
-   读取它的程序会根据它做什么事？（报错？注入对象？执行方法？）

想通了这几点，你就能从本质上理解任何一个注解了。

#### 概述、自定义注解

注解：

-   就是 Java 代码里的特殊标记，比如 `@Override`、`@Test` 等，作用是 **让其他程序根据注解信息来决定怎么执行该程序**。
-   注解可以用在类、构造器、方法、成员变量、参数等几乎任意位置上；

自定义注解：

-   就是自己定义注解

    -   ```java
        public @interface 注解名称{
        	public 属性类型 属性名() default 默认值;
        }
        ```

-   特殊属性名：value

    -   如果注解中只有一个 value 属性，使用注解时，value 名称可以不写！

![注解的原理](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2Fimage-20250619105234142.png)

注解的原理：

-   注解本质是一个接口，Java 中所有注解都继承了 Annotation 接口；
-   `@注解(...)`：本质上其实是一个实现类对象，实现了该注解以及 Annotation 接口；

注解的作用：

-   **对 Java 中的类、方法、成员变量做标记，然后进行特殊处理；**
-   例如：Junit 框架中，标记了注解@Test 的方法就可以被当成测试方法执行，而没有标记的就不能当成测试方法执行；

示例代码：

```java
// 自定义注解A
public @interface A {
    String value(); // 特殊属性value，在使用时如果只有一个value属性，value名称可以不写
    String hobby() default "打篮球";
}

// 自定义注解MyBook
public @interface MyBook {
    String name();
    int age() default 18;
    String[] address();
}


```



#### 元注解

指的是 **注解的注解**

##### @Target

作用：声明被修饰的注解只能在哪些位置使用，即限制注解的使用范围；

`@Target(ElementType.TYPE)`

1.  `TYPE`：类、接口
2.  `FIELD`：成员变量；
3.  `METHOD`：成员方法；
4.  `PARAMETER`：方法参数；
5.  `CONSTRUCTOR`：构造器；
6.  `LOCAL_VARIABLE`：局部变量；

##### @Retention

作用：声明注解的保留周期，约束自定义注解的存活范围；

`@Retention(RetentionPolicy.RUNTIME)`

1.  `SOURCE`：只作用在源码阶段，字节码文件中不存在；
2.  `CLASS`：默认值，保留到字节码文件阶段，运行阶段不存在；
3.  `RUNTIME`：开发常用，一直保留到运行阶段；

```java
// 自定义注解MyTest
@Target({ElementType.METHOD}) // 表示注解的作用目标为方法
@Retention(RetentionPolicy.RUNTIME) // 表示注解的保留策略: 编译器运行时(一直活着)
public @interface MyTest {
    int count() default 1; // 表示注解的属性
}

@Target({ElementType.METHOD, ElementType.FIELD}) // 表示注解的作用目标为方法,成员变量
@Retention(RetentionPolicy.RUNTIME) // 表示注解的保留策略: 编译器运行时(一直活着)
public @interface MyTest1 {
}

// @MyTest1		不能作用于类
public class AnnotationDemo2 {

    @MyTest1
    private int age;
   	 // @MyTest1 	不能作用于构造器
    public AnnotationDemo2(){
    }
    @MyTest1
    public static void main(String[] args) {
    // 目标：搞清楚元注解的作用。
    }
    @MyTest1
    public void getAgeTest(){
    }
}
```

#### 注解的解析

即判断类上、方法上、成员变量上等是否存在注解，并把注解里面的内容给解析出来；

**在运行时，利用 Java 反射机制，动态地检查并获取注解信息，从而实现特定的逻辑处理。这在很多框架（如 Spring、JUnit）中被广泛应用，用于简化配置和实现特定功能。**

##### 如何解析注解？

-   指导思想：要解析谁上面的注解，就要先拿到谁；
-   比如要解析类上的注解，则应该先获取该类的 Class 对象，再通过 Class 对象解析类上面的注解；
-   比如要解析成员方法上的注解，则应该先获取成员方法的 Method 对象，再通过 Method 对象解析其上面的注解；
-   Class、Method、Field、Constructor 都实现了 AnnotatedElement 接口，它们都拥有解析注解的能力；

**Class 对象、Method 对象等都可以通过反射来获取；**

| AnnotatedElement 接口提供了解析注解的方法                     | 说明                           |
| ------------------------------------------------------------ | ------------------------------ |
| public  Annotation [] **getDeclaredAnnotations**()            | 获取当前 **对象** 上面的注解。   |
| public  T **getDeclaredAnnotation**(Class <T> annotationClass) | 获取指定的注解对象             |
| public  boolean **isAnnotationPresent**(Class <Annotation> annotationClass) | 判断当前对象上是否存在某个注解 |



##### 解析注解的案例

1.  定义注解 MyTest2，要求如下：
    -   包含属性：`String value()`
    -   包含属性：`double height() default 169.5`
    -   包含属性：`String address`

示例代码：

```java
// 定义MyTest2注解
@Target({ElementType.METHOD, ElementType.TYPE}) // 表示注解的作用目标为方法，类或者接口
@Retention(RetentionPolicy.RUNTIME) // 表示注解的保留策略: 编译器运行时(一直活着)
public @interface MyTest2 {
    String value();
    double height() default 169.5;
    String[] address();
}

// 分别给类Demo和方法go加上MyTest2注解
@MyTest2(value = "刘亦菲", address = {"北京", "上海", "深圳"})
public class Demo {
    @MyTest2(value = "欧阳娜娜", address = {"湖南", "湖北"})
    public void go(){
    }
}

public class AnnotationDemo3 {
    // 目标：解析注解，通过反射注解注解的类实现
    @Test
    public void parseClass() throws Exception {
        // 解析Demo类上的注解，并把注解里面的内容给解析出来
        // 1.获取类对象
        Class c1 = Demo.class;
        // 2、使用isAnnotationPresent判断这个类上是否陈列了注解MyTest2
        if (c1.isAnnotationPresent(MyTest2.class)) {
            // 3、获取注解对象
            MyTest2 myTest2 = (MyTest2) c1.getDeclaredAnnotation(MyTest2.class);

            // 4、获取注解属性值
            String[] address = myTest2.address();
            double height = myTest2.height();
            String value = myTest2.value();

            // 5、打印注解属性值
            System.out.println(Arrays.toString(address));
            System.out.println(height);
            System.out.println(value);
        }
    }

    @Test
    public void parseMethod() throws Exception {
        // // 解析go方法上的注解，并把注解里面的内容给解析出来
        // 1.获取类对象
        Class c1 = Demo.class;
        // 2、获取方法对象
        Method method = c1.getMethod("go");
        // 3、使用isAnnotationPresent判断这个方法上是否陈列了注解MyTest2
        if (method.isAnnotationPresent(MyTest2.class)) {
            // 4、获取注解对象
            MyTest2 myTest2 = method.getDeclaredAnnotation(MyTest2.class);

            // 5、获取注解属性值
            String[] address = myTest2.address();
            double height = myTest2.height();
            String value = myTest2.value();

            // 6、打印注解属性值
            System.out.println(Arrays.toString(address));
            System.out.println(height);
            System.out.println(value);
        }
    }
}
```



#### 作用、应用场景

使用注解开发出一个简易版的 Junit 框架

需求：定义若干个方法，只要加了 MyTest 注解，就会触发该方法的执行；

分析：

1.  定义一个注解 MyTest，只能注解方法，存活范围是一直都在；
2.  定义若干个方法，部分方法加上@MyTest 注解修饰，部分方法不加；
3.  模拟一个 Junit 程序，可以触发加了@MyTest 注解的方法执行，没加@MyTest 的方法就不执行；

实现代码：

```java
@Target({ElementType.METHOD}) // 表示注解的作用目标为方法
@Retention(RetentionPolicy.RUNTIME) // 表示注解的保留策略: 编译器运行时(一直活着)
public @interface MyTest {
    int count() default 1; // 表示注解的属性
}


public class AnnotationDemo4 {
    // 目标：搞清楚注解的应用场景：模拟junit框架。有MyTest注解的方法就执行，没有的就不执行。
    public static void main(String[] args) throws Exception {
        AnnotationDemo4 ad = new AnnotationDemo4();
        // 1、获取类对象
        Class c = AnnotationDemo4.class;
        // 2、获取所有方法
        Method[] methods = c.getMethods();
        // 3、遍历所有方法，判断方法上是否有MyTest注解，有就执行，没有就不执行。
        for (Method method : methods) {
            // 4、判断方法上是否有MyTest注解
            if (method.isAnnotationPresent(MyTest.class)) {
                // 获取到这个方法的注解
                MyTest myTest = method.getDeclaredAnnotation(MyTest.class);
                // 可以通过count属性控制一个方法测试几次
                int count = myTest.count();
                // 5、有就执行这个method方法
                for (int i = 0; i < count; i++) {
                    method.invoke(ad);
                }
            }
        }

    }

    // 测试方法：public 无参 无返回值
    @MyTest
    public void test1(){
        System.out.println("test1方法执行了");
    }

    public void test2(){
        System.out.println("test2方法执行了");
    }

    @MyTest(count = 2)
    public void test3(){
        System.out.println("test3方法执行了");
    }

    @MyTest
    public void test4(){
        System.out.println("test4方法执行了");
    }
}
```



### 动态代理

#### 为什么需要代理？

想象一个生活中的场景：你是一位大明星（**目标对象**），你的核心工作是唱歌和演戏。但除了这些，你还有很多琐事，比如谈合同、安排档期、过滤骚扰电话等。如果你亲自处理所有这些事，会非常低效且分散精力。

于是，你雇佣了一位经纪人（**代理对象**）。

-   当有人想找你谈合作，他们会先联系你的 **经纪人**。
-   经纪人会负责处理所有前期工作：审核资质、谈判条款、安排时间。
-   只有当一切准备就绪，需要你亲自出面（唱歌、演戏）时，经纪人才会通知你。

在这个模型中，经纪人并没有取代你的核心技能，而是在不改变你核心工作的前提下，为你 **增强了功能**（合同谈判、安全过滤等）。

**在软件开发中，代理模式（Proxy Pattern）的思想是完全一样的。**

它的核心目的是：**在不修改目标对象（原始类）代码的前提下，通过引入一个代理对象来为目标对象增加额外的功能或控制其访问。**

这遵循了软件设计中的一个重要原则——**开闭原则（Open/Closed Principle）**：<span style="color:#d59bf6;">对扩展开放，对修改关闭。我们不希望每次增加一个新功能（比如记录日志）就去修改一次原始类的代码。</span>

**使用代理的好处（解决的实际问题）：**

1.  **功能增强（Enhancement）**: 在调用原始方法前后，增加新的逻辑。
    -   **事务管理**：在方法开始时开启事务，在方法结束时提交或回滚事务。
    -   **日志记录**：记录方法的入参、出参和执行时间，方便调试和监控。
    -   **性能监控**：计算每个方法的执行耗时。
2.  **访问控制（Access Control）**: 代理可以决定是否要将请求转发给目标对象。
    -   **权限校验**：在调用方法前，检查当前用户是否具有执行该操作的权限。
3.  **懒加载（Lazy Loading）**: 如果一个对象的创建非常耗费资源，代理可以等到真正需要使用它时才去创建它。

#### 解决实际问题、掌握使用代理的好处

使用代理的好处：

1、**功能增强（Enhancement）**: 在调用原始方法前后，增加新的逻辑。

-   **事务管理**：在方法开始时开启事务，在方法结束时提交或回滚事务。
-   **日志记录**：记录方法的入参、出参和执行时间，方便调试和监控。
-   **性能监控**：计算每个方法的执行耗时。

2、**访问控制（Access Control）**: 代理可以决定是否要将请求转发给目标对象。

-   **权限校验**：在调用方法前，检查当前用户是否具有执行该操作的权限。

3、**懒加载（Lazy Loading）**: 如果一个对象的创建非常耗费资源，代理可以等到真正需要使用它时才去创建它。

理解了为什么需要代理后，我们来看 Java 是如何实现的。代理可以分为 **静态代理** 和 **动态代理**。

-   **静态代理**：需要我们手动为每个目标接口编写一个代理类。如果接口很多，或者接口中的方法发生变化，维护起来会非常繁琐，导致类爆炸。
-   **动态代理**：不需要手动编写代理类。代理类是在程序运行时，由 JVM 根据我们提供的信息动态生成的。这极大地提高了灵活性和可维护性。

Java 的 `java.lang.reflect` 包提供了实现动态代理的核心机制。主要涉及两个关键角色：

1.  `Proxy` 类：这是创建动态代理实例的主工厂。最重要的方法是 `Proxy.newProxyInstance()`。
2.  `InvocationHandler` 接口：这是代理的“大脑”。它是一个接口，只有一个 `invoke` 方法。所有对代理对象的方法调用，最终都会被转发到这个 `invoke` 方法中来统一处理。

#### 动态代理的工作流程

1.  当客户端代码调用代理对象的一个方法时（例如 `proxy.doSomething()`）。
2.  <span style="color:#d59bf6;">这个调用请求不会直接执行</span>，而是被 **转发** 到与该代理关联的 `InvocationHandler` 的 `invoke` 方法上。
3.  `invoke` 方法会接收到三个参数：
    -   `Object proxy`: 代理对象本身（一般很少使用）。
    -   `Method method`: 被调用的方法对象（例如 `doSomething` 方法）。
    -   `Object[] args`: 调用方法时传递的参数。
4.  在 `invoke` 方法内部，我们可以：
    -   **执行前置增强**：比如打印日志、开启事务。
    -   通过反射调用**目标对象的原始方法**：`method.invoke(target, args)`。
    -   **执行后置增强**：比如提交事务、计算耗时。
    -   返回原始方法的执行结果。

示例代码：

```java
// 代理是基于接口的，代理要知道明星能够接哪些活，比如唱歌和跳舞
// 明星行为接口，StarService就是明星Star的代理
public interface StarService {
    void sing(String name);
    String dance();
}

// 被代理的明星类
@Data
@AllArgsConstructor
@NoArgsConstructor
// 明星类要实现明星行为接口，由明星本身来完成，如唱歌、跳舞等明星行为
public class Star implements StarService{
    private String name;
    // 重写接口方法
    @Override
    public void sing(String name) {
        System.out.println(this.name + "表演唱歌：" + name);
    }

    @Override
    public String dance() {
        System.out.println(this.name + "表演跳舞：魅力四射！" );
        return "谢谢！谢谢！";
    }
}


/**
 * 代理工具类：中介公司，专门负责创建代理对象并返回给别人使用
 */
public class ProxyUtil {
    // 创建一个明星对象的代理对象返回。
    public static StarService createProxy(Star s){
        /**
         * 参数一：用于执行用哪个类加载器去加载生成的代理类。
         * 参数二：用于指定代理类需要实现的接口: 明星类实现了哪些接口，代理类就实现哪些接口
         * 参数三：用于指定代理类需要如何去代理（代理要做的事情）。
         */
        StarService proxy = (StarService) Proxy.newProxyInstance(ProxyUtil.class.getClassLoader(),
                s.getClass().getInterfaces(), new InvocationHandler() {
                    @Override
                    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                        // 用来声明代理对象要干的事情。
                        // 参数一： proxy接收到代理对象本身（暂时用处不大）
                        // 参数二： method代表正在被代理的方法
                        // 参数三： args代表正在被代理的方法的参数
                        String methodName = method.getName();
                        if("sing".equals(methodName)){
                            System.out.println("准备话筒，收钱20万！");
                        }else if("dance".equals(methodName)){
                            System.out.println("准备场地，收钱100万！");
                        }
                        // 真正干活（把真正的明星对象叫过来正式干活）
                        // 找真正的明星对象来执行被代理的行为：method方法
                        Object result = method.invoke(s, args);
                        return result;
                    }
                });
        return proxy;
    }
}

public class Test {
    public static void main(String[] args) {
        // 目标：创建代理对象。
        // 1、准备一个明星对象：设计明星类。
        Star star = new Star("章若楠");
        // star.sing("《红昭愿》");
        // 2、为章若楠创建一个专属与她的代理对象。
        StarService proxy = ProxyUtil.createProxy(star);
        proxy.sing("《红昭愿》");
        System.out.println(proxy.dance());
    }
}
```

#### 代码实例

让我们通过一个“为用户服务添加性能监控”的例子来演示。

**第一步：定义一个接口**

动态代理是基于接口的，所以我们首先需要一个接口。

```java
// UserService.java
public interface UserService {
    void addUser(String username);
    String findUser(int id);
}
```

**第二步：创建接口的实现类（目标对象）**

这是我们原始的、不希望被修改的业务逻辑。

```java
// UserServiceImpl.java
public class UserServiceImpl implements UserService {
    @Override
    public void addUser(String username) {
        // 模拟数据库操作耗时
        try { Thread.sleep(50); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.println("成功添加用户: " + username);
    }

    @Override
    public String findUser(int id) {
        // 模拟数据库操作耗时
        try { Thread.sleep(100); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.println("正在查找ID为 " + id + " 的用户...");
        return "用户" + id;
    }
}
```

**第三步：创建`InvocationHandler`实现**

这是动态代理的核心，我们在这里编写增强逻辑。

```Java
// PerformanceMonitorHandler.java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class PerformanceMonitorHandler implements InvocationHandler {

    // 目标对象，也就是被代理的对象
    private final Object target;

    public PerformanceMonitorHandler(Object target) {
        this.target = target;
    }

    /**
     * 所有对代理对象的方法调用都会进入这个invoke方法
     * @param proxy 代理对象
     * @param method 被调用的方法
     * @param args 方法的参数
     * @return 方法的返回值
     * @throws Throwable
     */
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("---进入性能监控代理---");
        
        // 1. 前置增强：记录方法开始时间
        long startTime = System.currentTimeMillis();

        // 2. 通过反射调用目标对象的原始方法
        Object result = method.invoke(target, args);

        // 3. 后置增强：记录方法结束时间并计算耗时
        long endTime = System.currentTimeMillis();
        System.out.println("方法 " + method.getName() + " 执行耗时: " + (endTime - startTime) + "毫秒");
        
        System.out.println("---退出性能监控代理---");

        // 4. 返回原始方法的执行结果
        return result;
    }
}
```

**第四步：创建并使用代理对象**

在客户端代码中，我们使用 `Proxy.newProxyInstance()` 来生成代理。

```Java
// ProxyClient.java
import java.lang.reflect.Proxy;

public class ProxyClient {
    public static void main(String[] args) {
        // 1. 创建目标对象实例
        UserService realUserService = new UserServiceImpl();

        // 2. 创建 InvocationHandler 实例，并将目标对象传入
        InvocationHandler handler = new PerformanceMonitorHandler(realUserService);

        // 3. 使用 Proxy.newProxyInstance() 创建动态代理对象
        // 参数1: 类加载器，通常和目标对象使用同一个
        // 参数2: 代理类需要实现的接口数组，和目标对象的接口保持一致
        // 参数3: InvocationHandler，我们将方法调度的逻辑委托给它
        UserService proxyUserService = (UserService) Proxy.newProxyInstance(
                realUserService.getClass().getClassLoader(),
                realUserService.getClass().getInterfaces(),
                handler
        );

        // 4. 通过代理对象调用方法
        // 注意：我们现在操作的是 proxyUserService，而不是 realUserService
        System.out.println("开始调用 addUser 方法...");
        proxyUserService.addUser("Alice");
        System.out.println();

        System.out.println("开始调用 findUser 方法...");
        String user = proxyUserService.findUser(101);
        System.out.println("查询结果: " + user);
    }
}
```

**运行结果：**

```Java
开始调用 addUser 方法...
---进入性能监控代理---
成功添加用户: Alice
方法 addUser 执行耗时: 53毫秒
---退出性能监控代理---

开始调用 findUser 方法...
---进入性能监控代理---
正在查找ID为 101 的用户...
方法 findUser 执行耗时: 101毫秒
---退出性能监控代理---
查询结果: 用户101
```

从结果可以看出，我们没有修改一行 `UserServiceImpl` 的代码，却成功地为它的每个方法都增加了性能监控的功能。

**总结**

-   **为什么需要代理？**

    -   为了在**不修改源码**的情况下，对已有对象的功能进行**增强**或**控制**。
    -   核心价值在于**解耦**，让业务逻辑和非业务的通用逻辑（如日志、事务、安全）分离。

-   **Java动态代理**

    -   **优点**：解决了静态代理的类爆炸问题，非常灵活，可以在运行时动态创建代理。

    -   **核心**：`Proxy` 类和 `InvocationHandler` 接口。所有逻辑都集中在 `invoke` 方法中。

    -   局限

        ：Java原生的动态代理

        必须基于接口

        。如果一个类没有实现任何接口，就无法为它创建动态代理。

        -   （*补充知识*：为了解决这个问题，可以引入第三方库如 **CGLIB**，它通过继承目标类来创建代理，从而绕过了接口的限制。）



又一个案例：

```java
/**
 *  用户业务接口
 */
// 在接口中定义好需要实现的核心功能
public interface UserService {
    // 登录功能
    void login(String loginName,String passWord) throws Exception;
    // 删除用户
    void deleteUsers() throws Exception;
    // 查询用户，返回数组的形式。
    String[] selectUsers() throws Exception;
    String[] selectUsers2() throws Exception;
}



/**
 * 用户业务实现类（面向接口编程）
 */
// 根据接口定义好核心功能的具体实现
public class UserServiceImpl implements UserService{
    @Override
    public void login(String loginName, String passWord) throws Exception {
        // ----------------------
        if("admin".equals(loginName) && "123456".equals(passWord)){
            System.out.println("您登录成功，欢迎光临本系统~");
        }else {
            System.out.println("您登录失败，用户名或密码错误~");
        }
        Thread.sleep(1000);
        // --------------------------
    }

    @Override
    public void deleteUsers() throws Exception{
        System.out.println("成功删除了1万个用户~");
        Thread.sleep(1500);
    }

    @Override
    public String[] selectUsers() throws Exception{
        System.out.println("查询出了3个用户");
        String[] names = {"张全蛋", "李二狗", "牛爱花"};
        Thread.sleep(500);

        return names;
    }

    @Override
    public String[] selectUsers2() throws Exception {
        System.out.println("查询出了3000个用户");
        String[] names = {"张全蛋2", "李二狗2", "牛爱花2"};
        Thread.sleep(2500);

        return names;
    }
}



// 通过代理为前面的核心功能增加附加功能，而不用修改核心功能的原始代码，比如这里为每一个核心功能增加了耗时检测功能
public class ProxyUtil {
    public static <T> T createProxy(T obj) {
        T proxy = (T) Proxy.newProxyInstance(ProxyUtil.class.getClassLoader(),
                obj.getClass().getInterfaces(), new InvocationHandler() {
                    @Override
                    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                        long start = System.currentTimeMillis(); // 记录开始时间 1970年1月1日0时0分0秒 走到此刻的总毫秒值
                        // 真正调用业务对象被代理的方法
                        Object result = method.invoke(obj, args);

                        long end = System.currentTimeMillis();
                        System.out.println(method.getName() + "方法耗时："+(end-start)/1000.0+"秒");
                        return result;
                    }
                });
        return proxy;
    }
}



/**
 * 目标：使用动态代理解决实际问题，并掌握使用代理的好处。
 */
// 测试代理功能
public class Test {
    public static void main(String[] args) throws Exception{
        // 1、创建用户业务对象。
        UserService userService = ProxyUtil.createProxy(new UserServiceImpl());

        // 2、调用用户业务的功能。
        userService.login("admin", "123456");

        userService.deleteUsers();

        String[] names = userService.selectUsers();
        System.out.println("查询到的用户是：" + Arrays.toString(names));

        String[] names2 = userService.selectUsers2();
        System.out.println("查询到的用户是：" + Arrays.toString(names2));
    }
}
```





















































































