[toc]

Java Stream 流式处理是自 Java 8 引入的一项革命性特性，它提供了一种声明式、函数化的方式来处理数据集合。 Stream API 极大地简化了集合（如 List、Set、Map）和数组的操作，让代码更简洁、可读性更强，并且易于并行化处理。 本文将对 Java Stream 的方法和技巧进行全面而详细的总结。

### 一、 Stream API 核心概念

#### 1. 什么是 Stream？
Stream（流）是数据渠道，用于操作数据源（如集合、数组等）所生成的元素序列。 它本身不存储数据，而是通过管道化的方式对数据进行一系列的中间操作，最后由一个终端操作产生最终结果。

#### 2. Stream 的核心特性
*   **非数据结构**：Stream 不是一种数据结构，它不存储元素。它只是对源数据进行计算的视图。
*   **不修改数据源**：Stream 的所有操作都不会修改其数据源，而是返回一个持有结果的新 Stream。
*   **惰性求值（Lazy Evaluation）**：Stream 的中间操作是惰性的。它们不会立即执行，只有当终端操作被调用时，整个处理管道才会开始执行。 这种特性使得 Stream 能够进行很多优化。
*   **只能消费一次**：一个 Stream 只能被一个终端操作消费一次。一旦终端操作执行完毕，该 Stream 就关闭了，再次使用会抛出 `IllegalStateException`。
*   **无限流**：Stream 可以是有限的，也可以是无限的。例如，通过 `Stream.iterate()` 或 `Stream.generate()` 可以创建无限流，通常需要与 `limit()` 等操作结合使用。
*   **内部迭代**：与传统的使用 `for`、`while` 循环的外部迭代不同，Stream 使用的是内部迭代。开发者只需声明要做什么，具体的迭代过程由 Stream API 内部完成。

### 二、 Stream 的创建

要使用 Stream，首先需要获取一个数据源的 Stream 实例。创建 Stream 的方式多种多样：

*   **从集合创建**：这是最常用的方式，所有 `java.util.Collection` 接口的实现类都可以通过 `stream()` 或 `parallelStream()` 方法创建 Stream。
    ```java
    List<String> list = Arrays.asList("a", "b", "c");
    Stream<String> stream = list.stream(); // 创建顺序流
    Stream<String> parallelStream = list.parallelStream(); // 创建并行流
    ```

*   **从数组创建**：使用 `Arrays.stream()` 方法可以从数组创建 Stream。
    ```java
    String[] array = new String[]{"a", "b", "c"};
    Stream<String> stream = Arrays.stream(array);
    ```

*   **使用 Stream 的静态方法**：
    *   `Stream.of()`：可以直接接收一系列元素来创建一个 Stream。
        ```java
        Stream<String> stream = Stream.of("a", "b", "c");
        ```
    *   `Stream.iterate()`：创建一个无限顺序流，它接受一个种子值和一个用于生成下一个元素的函数。
        ```java
        // 生成从1开始的无限整数流：1, 2, 3, 4...
        Stream<Integer> stream = Stream.iterate(1, n -> n + 1).limit(10); // 通常与 limit 结合使用
        ```
    *   `Stream.generate()`：创建一个无限顺序流，它接受一个 `Supplier<T>` 来生成元素。
        ```java
        // 生成10个随机数
        Stream<Double> stream = Stream.generate(Math::random).limit(10);
        ```

*   **从文件创建**：`java.nio.file.Files` 类提供了多种方法来从文件生成 Stream，例如 `lines()` 方法可以生成一个由文件每行内容组成的 Stream。
    ```java
    try (Stream<String> stream = Files.lines(Paths.get("file.txt"))) {
        stream.forEach(System.out::println);
    } catch (IOException e) {
        e.printStackTrace();
    }
    ```

### 三、 Stream 的中间操作 (Intermediate Operations)

中间操作会返回一个新的 Stream，并且可以链接起来形成一个处理管道。

| 方法                                     | 描述                                                         | 示例                                                         |
| :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **`filter(Predicate<T>)`**               | 筛选出满足指定条件的元素。                                   | `stream.filter(s -> s.startsWith("a"))`                      |
| **`map(Function<T, R>)`**                | 将每个元素转换为另一个元素。                                 | `stream.map(String::toUpperCase)`                            |
| **`flatMap(Function<T, Stream<R>>)`**    | 将每个元素转换为一个 Stream，然后将所有生成的 Stream 连接成一个单一的扁平化 Stream。 | `Stream.of(Arrays.asList(1, 2), Arrays.asList(3, 4)).flatMap(List::stream)` |
| **`distinct()`**                         | 去除流中的重复元素。 这是一个有状态的操作。                  | `stream.distinct()`                                          |
| **`sorted()` / `sorted(Comparator<T>)`** | 对流中的元素进行排序。 可以使用自然排序或自定义比较器。这是一个有状态的操作。 | `stream.sorted(Comparator.reverseOrder())`                   |
| **`peek(Consumer<T>)`**                  | 对每个元素执行一个操作，主要用于调试。 它返回一个包含原始元素的新 Stream。 | `stream.peek(System.out::println)`                           |
| **`limit(long n)`**                      | 截断流，使其元素不超过给定数量。 这是一个有状态的短路操作。  | `stream.limit(5)`                                            |
| **`skip(long n)`**                       | 跳过前 n 个元素。 这是一个有状态的操作。                     | `stream.skip(3)`                                             |
| **`takeWhile(Predicate<T>)` (Java 9+)**  | 返回从流的开头开始，满足谓词条件的连续元素。一旦遇到不满足条件的元素，立即停止。 | `Stream.of(1,2,3,4,1).takeWhile(n -> n < 4)` 结果为 `1,2,3`  |
| **`dropWhile(Predicate<T>)` (Java 9+)**  | 从流的开头丢弃满足谓词条件的连续元素，然后返回剩余的元素。   | `Stream.of(1,2,3,4,1).dropWhile(n -> n < 3)` 结果为 `3,4,1`  |



“Predicate”是一个关键的概念，它通常在函数式编程中特别重要。在 Java 中，`Predicate<T>` 是一个函数式接口，代表一个接受一个输入参数并返回布尔值（true 或 false）的函数。它用于定义一组可以用于过滤数据的条件。

#### 详细解释和分析

1. **功能性**:

    - `Predicate<T>` 接口的主要功能是提供测试的方法，通常用于判断某个条件是否成立。在流处理（Stream）的操作中，`Predicate` 常被用作过滤条件，以筛选出满足某些条件的元素。例如：在代码示例 `stream.filter(s -> s.startsWith("a"))` 中，`Predicate` 被用来判断一个字符串是否以字母 "a" 开头。

2. **用法示例**:

    - `Predicate` 的使用通常在流的操作中非常普遍，比如 `filter()` 方法，它会返回一个新流，其中包含通过给定的条件进行测试的元素。`takeWhile` 和 `dropWhile` 方法也使用了 `Predicate` 来控制从流中选择或丢弃哪些元素。

3. **特性**:

    - `Predicate` 是一个有状态的操作，因为它依赖于外部条件（即输入元素是否满足某种判断）。这意味着每次调用这个谓词都会检查新的输入。

4. **应用范围**:

    - 除了在流操作中，`Predicate` 也可以在其他地方使用，比如集合的过滤，以及任何需要条件测试的上下文。

5. **代码示例**:

    - 例如，使用 `Predicate` 来过滤一个整数列表中所有大于 5 的数字：

        ```java
        List<Integer> numbers = Arrays.asList(1, 2, 3, 6, 7, 8);
        List<Integer> filtered = numbers.stream()
                                        .filter(n -> n > 5)
                                        .collect(Collectors.toList());
        ```

综上所述，`Predicate` 在函数式编程和流处理中的重要性不言而喻，它使得开发者能够方便地定义和应用条件判断，以实现数据的灵活处理。

`Function<T, R>` 是 Java 中用于函数式编程的重要概念之一，特别是在处理流（Stream）时。

### 详细解释与分析：

1. **Function <T, R> 的结构**：
   - `Function` 是一个函数式接口，它接收一个类型为 `T` 的输入，并返回一个类型为 `R` 的输出。
   - `T` 和 `R` 是类型参数。它们可以被替换为任何非基本类型，例如 `String`、`Integer`、`Double` 等。这样，`Function` 的灵活性使得它可以用于各种不同类型的输入输出转换。

2. **常见用法**：
   - 在流的操作中，`Function<T, R>` 常用于 `map` 方法中。通过传入一个实现了 `Function` 接口的 lambda 表达式，可以对流中的元素进行转换。例如：
     ```java
     stream.map(String::toUpperCase)
     ```
     在这个例子中，`String::toUpperCase` 是一个 `Function<String, String>` 的实现，将流中的每个字符串转换为大写。

3. **函数式编程**：
   - `Function<T, R>` 表示一种函数式编程的思路，它使得代码更加简洁和可读。使用这种方式，程序员可以将行为作为参数传递，从而利用高阶函数的特性，提高代码的灵活性和重用性。

4. **与其他函数式接口的关系**：
   - `Function<T, R>` 只是 Java 函数式接口中的一种，其他常见的接口还有 `Predicate`（接受一个参数返回布尔值），`Consumer`（接受一个参数但不返回值）等。这些接口与 `Function<T, R>` 是相辅相成的，共同构成了强大的流处理工具。

综上所述，`Function<T, R>` 是一个核心概念，使得 Java 的流 API 能够执行各种复杂的数据转换操作，对于提高代码的可读性和维护性具有重要作用。

### 四、 Stream 的终端操作 (Terminal Operations)

终端操作会触发 Stream 管道的执行，并产生一个最终结果或副作用。

| 方法                                            | 描述                                                         | 示例                                                         |
| :---------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **`forEach(Consumer<T>)`**                      | 对流中的每个元素执行一个操作。                               | `stream.forEach(System.out::println)`                        |
| **`toArray()`**                                 | 将流中的元素收集到一个数组中。                               | `String[] array = stream.toArray(String[]::new)`             |
| **`reduce(T identity, BinaryOperator<T>)`**     | 将流中的所有元素聚合成一个值。                               | `int sum = numbers.stream().reduce(0, (a, b) -> a + b)`      |
| **`collect(Collector<T, A, R>)`**               | 最重要的终端操作之一，将流中的元素收集到集合或其他数据结构中。 | `List<String> list = stream.collect(Collectors.toList())`    |
| **`count()`**                                   | 返回流中元素的数量。                                         | `long count = stream.count()`                                |
| **`anyMatch(Predicate<T>)`**                    | 检查流中是否至少有一个元素匹配给定的谓词。 这是一个短路操作。 | `boolean hasA = stream.anyMatch(s -> s.startsWith("a"))`     |
| **`allMatch(Predicate<T>)`**                    | 检查流中的所有元素是否都匹配给定的谓词。 这是一个短路操作。  | `boolean allShort = stream.allMatch(s -> s.length() < 5)`    |
| **`noneMatch(Predicate<T>)`**                   | 检查流中是否没有任何元素匹配给定的谓词。 这是一个短路操作。  | `boolean noEmpty = stream.noneMatch(String::isEmpty)`        |
| **`findFirst()`**                               | 返回流中的第一个元素，包装在 `Optional` 中。                 | `Optional<String> first = stream.findFirst()`                |
| **`findAny()`**                                 | 返回流中的任意一个元素，包装在 `Optional` 中。在并行流中，性能可能比 `findFirst` 更好。 | `Optional<String> any = stream.findAny()`                    |
| **`min(Comparator<T>)` / `max(Comparator<T>)`** | 返回流中的最小/最大元素，包装在 `Optional` 中。              | `Optional<Integer> max = numbers.stream().max(Integer::compareTo)` |

### 五、 核心技巧与高级应用：`Collectors` 详解

`java.util.stream.Collectors` 是一个工具类，提供了大量预定义的收集器，极大地增强了 `collect` 方法的能力。

#### 1. 收集到集合
*   **`toList()`**: 将流元素收集到一个 `List` 中。
*   **`toSet()`**: 将流元素收集到一个 `Set` 中，自动去重。
*   **`toCollection(Supplier<C>)`**: 将流元素收集到指定类型的集合中。
    ```java
    LinkedList<String> linkedList = stream.collect(Collectors.toCollection(LinkedList::new));
    ```

#### 2. 收集到 Map
*   **`toMap(Function keyMapper, Function valueMapper)`**: 将流元素收集到一个 `Map` 中。
    ```java
    // 假设有 Person(id, name) 对象列表
    // Key 为 id，Value 为 Person 对象
    Map<Long, Person> personMap = people.stream()
                                    .collect(Collectors.toMap(Person::getId, p -> p));
    ```
    **注意**：如果 Key 重复，会抛出 `IllegalStateException`。可以使用 `toMap` 的重载版本来处理 Key 冲突：
    ```java
    // (oldValue, newValue) -> newValue 表示保留新值
    Map<String, Integer> map = items.stream()
            .collect(Collectors.toMap(Item::getName, Item::getQuantity, (oldValue, newValue) -> newValue));
    ```

#### 3. 字符串拼接
*   **`joining(CharSequence delimiter, CharSequence prefix, CharSequence suffix)`**: 将流中的 `String` 元素连接起来。
    ```java
    String names = people.stream()
                         .map(Person::getName)
                         .collect(Collectors.joining(", ", "[", "]"));
    // 结果类似：[Alice, Bob, Charlie]
    ```

#### 4. 分组与分区
*   **`groupingBy(Function classifier)`**: 根据指定的分类函数对元素进行分组，返回一个 `Map`。
    ```java
    // 按部门对员工进行分组
    Map<Department, List<Employee>> employeesByDept = employees.stream()
            .collect(Collectors.groupingBy(Employee::getDepartment));
    ```
*   **`groupingBy` 的高级用法（多级分组和下游收集器）**：
    ```java
    // 按部门分组，并统计每个部门的人数
    Map<Department, Long> countByDept = employees.stream()
            .collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
    
    // 先按部门分组，再按性别分组
    Map<Department, Map<Gender, List<Employee>>> multiLevelGroup = employees.stream()
            .collect(Collectors.groupingBy(Employee::getDepartment,
                                        Collectors.groupingBy(Employee::getGender)));
    ``` *   * *`partitioningBy(Predicate predicate)`**: 根据一个谓词将元素分为两组（`true` 和 `false`），返回 `Map<Boolean, List<T>>`。
    ```java
    // 将员工具体分为工资高于5000和低于等于5000两组
    Map<Boolean, List<Employee>> partitioned = employees.stream()
            .collect(Collectors.partitioningBy(e -> e.getSalary() > 5000));
    ```

#### 5. 聚合计算
`Collectors` 提供了一系列用于聚合计算的方法，常与 `groupingBy` 结合使用：
*   **`counting()`**: 计数。
*   **`summingInt()`, `summingLong()`, `summingDouble()`**: 求和。
*   **`averagingInt()`, `averagingLong()`, `averagingDouble()`**: 求平均值。
*   **`summarizingInt()`, `summarizingLong()`, `summarizingDouble()`**: 一次性获取计数、总和、平均值、最大值、最小值，返回一个统计对象（如 `IntSummaryStatistics`）。
    ```java
    // 计算每个部门的薪资统计信息
    Map<Department, IntSummaryStatistics> deptStats = employees.stream()
            .collect(Collectors.groupingBy(Employee::getDepartment,
                                        Collectors.summarizingInt(Employee::getSalary)));
    ```

### 六、 并行流 (Parallel Streams)

并行流是 Stream API 的一大亮点，能够充分利用多核处理器的性能，对大数据集合进行并行处理。

*   **创建并行流**:
    *   `collection.parallelStream()`
    *   `stream.parallel()`

*   **工作原理**: 并行流内部使用 Java 7 引入的 Fork/Join 框架。它会将流中的数据分割成多个小块（Splitting），然后为每个小块分配一个独立的线程进行处理（Processing），最后将处理结果合并（Combining）。

*   **注意事项**:
    *   **线程安全**: 确保在并行流中使用的 Lambda 表达式是无状态或线程安全的。
    *   **适用场景**: 适用于数据量大且每个元素处理耗时较长的计算密集型任务。对于数据量小或者 I/O 密集型任务，并行化带来的线程切换开销可能超过其收益。
    *   **避免共享可变状态**: 在 Lambda 表达式中修改共享变量（如 `List.add`）是极其危险的，会导致不可预期的结果。应使用 `collect` 等线程安全的操作。
    *   **顺序问题**: 并行流不保证处理顺序。如果需要保持顺序，可以使用 `forEachOrdered()` 代替 `forEach()`，但这会牺牲部分并行性能。

### 七、 总结与最佳实践

1.  **链式调用**: 尽量使用链式调用的方式组织 Stream 操作，使代码更具可读性。
2.  **选择合适的操作**: 熟悉每个操作的功能，选择最恰当的方法来解决问题。例如，用 `map` 进行转换，用 `filter` 进行筛选。
3.  **无状态 Lambda**: 尽量保证中间操作的 Lambda 表达式是无状态的，这对于并行处理至关重要。
4.  **提前过滤**: 尽可能早地使用 `filter` 操作，可以减少后续操作需要处理的元素数量，提高效率。
5.  **小心使用 `peek`**: `peek` 主要用于调试，避免在生产代码中滥用它执行业务逻辑。
6.  **善用 `Optional`**: 对于可能返回空结果的终端操作（如 `findFirst`, `reduce`），使用 `Optional` 来优雅地处理 `null` 值，避免 `NullPointerException`。
7.  **谨慎选择并行流**: 仅在确信可以带来性能提升的场景下使用并行流，并进行充分的性能测试。