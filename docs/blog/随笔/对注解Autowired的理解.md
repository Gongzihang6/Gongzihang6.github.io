# @Autowired 和 import 的区别

在 Tilas 员工管理系统中，为什么需要@Autowired 这个注解来注解 EmployService 这个接口类呢？import 为什么不够呢？

```java
package com.gzh.tilas.Controller;

import com.gzh.tilas.Service.EmployeeService;
import com.gzh.tilas.pojo.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class EmployeeController {
    @Autowired
    EmployeeService employeeService;

    @PostMapping("/emps")
    public String insert(Employee employee) {
        int result = employeeService.insert(employee);
        if (result > 0) {
            return "添加成功";
        } else {
            return "添加失败";
        }
    }

    // 根据员工ID查询员工信息
    @GetMapping("/emps")
    public Employee getById(Integer id) {
        Employee employee = employeeService.getById(id);
        return employee;
    }


}

```

简单来说，`import` 和 `@Autowired` 解决了两个完全不同层面的问题：

1.  **`import`**: 解决的是 **编译时** 的 **“类型识别”** 问题。
2.  **`@Autowired`**: 解决的是 **运行时** 的 **“对象注入”** 问题。

让我们一步步来拆解。

---

### 1. `import` 的作用：告诉编译器这是什么

当你写下 `import com.gzh.tilas.Service.EmployeeService;` 时，你只是在告诉 Java 编译器：

> “嘿，编译器，我在代码里用到了一个叫做 `EmployeeService` 的东西，它的完整定义在 `com.gzh.tilas.Service` 这个包里。你去那里找它的‘设计图’（.class 文件），这样你就知道它有哪些方法、哪些属性，我调用 `employeeService.insert()` 的时候你就不会报错了。”

`import` 只是让你的代码能够 **通过编译**。它并没有创建任何 `EmployeeService` 的 **实例对象**。

在你的代码中，`EmployeeService employeeService;` 这行代码只是声明了一个变量，它的类型是 `EmployeeService`。此时，这个变量的值是 `null`，它没有指向任何实际的内存对象。

如果你只用 `import` 而没有 `@Autowired`，当请求进来，执行到 `employeeService.insert(employee);` 这一行时，因为 `employeeService` 是 `null`，程序会立即抛出 `NullPointerException`（空指针异常）。

---

### 2. `@Autowired` 的作用：告诉 Spring 框架给我一个实例

`@Autowired` 是 Spring 框架提供的注解。它的作用是告诉 **Spring IoC 容器**（Inversion of Control，控制反转容器）：

> “嘿，Spring 容器，我这里需要一个 `EmployeeService` 类型的 **实例对象**。请你在你管理的众多对象（我们称之为 "Bean"）中，找一个符合这个类型的，然后自动把它赋值给我这个 `employeeService` 变量。”

这个过程就是 **依赖注入（Dependency Injection, DI）**。

#### 它是如何工作的？

1.  **Bean 的扫描与创建**：当你的 Spring Boot 应用程序启动时，它会扫描你项目中的类。当它看到一个类被 `@Service`, `@Component`, `@Repository`, `@Controller` 等注解标记时（比如你的 `EmployeeServiceImpl` 类上很可能有一个 `@Service` 注解），Spring 就会创建这个类的一个实例，并把它放到自己的“大仓库”（IoC 容器）里进行管理。

2.  **依赖的注入**：接着，Spring 会处理那些需要被注入依赖的 Bean（比如你的 `EmployeeController`，因为它被 `@RestController` 标记了）。当 Spring 创建 `EmployeeController` 的实例时，它看到了 `@Autowired` 注解。

3.  **查找与装配**：Spring 容器就会在它的“大仓库”里寻找一个类型为 `EmployeeService` 的 Bean。它找到了之前创建的 `EmployeeServiceImpl` 实例，然后就像这样自动完成了赋值操作：`this.employeeService = [从容器中找到的EmployeeServiceImpl实例];`。

所以，当你的 Controller 方法被调用时，`employeeService` 已经是一个可以正常工作的、被 Spring 初始化好的实例了，而不是 `null`。

---

### 形象的比喻

想象一下你要组装一台电脑：

*   **`import`** 就像是你看懂了电脑配件的 **说明书**。你知道什么是 CPU，什么是内存条，它们有什么接口。但你手上没有任何实物。

*   **`new EmployeeServiceImpl()`** （手动创建对象）就像是你 **亲自去工厂生产** 了一个 CPU。这样做的问题是，你（`EmployeeController`）和 CPU 的生产过程紧紧地绑定在了一起，万一以后要换个牌子的 CPU，你还得自己去改生产线。这叫做“紧耦合”。

*   **`@Autowired`** 就像是你对电脑城老板（**Spring 容器**）说：“老板，给我来一个合适的 CPU”。老板会从他的货架上（**IoC 容器**）拿一个已经准备好的、能用的 CPU（**Bean 实例**）直接装到你的主板上（**注入到你的类中**）。你不需要关心这个 CPU 是怎么生产的、是哪个牌子的，只要它能用就行。这叫做“解耦”。

### 总结

| 特性     | `import`                                              | `@Autowired`                                                 |
| :------- | :---------------------------------------------------- | :----------------------------------------------------------- |
| **阶段** | 编译时 (Compile Time)                                 | 运行时 (Runtime)                                             |
| **角色** | Java 编译器                                           | Spring IoC 容器                                              |
| **作用** | 告知类的位置，让代码能识别类型，避免编译错误。        | 自动从容器中获取一个已经创建好的对象实例，并赋值给当前变量。 |
| **结果** | 变量类型已知，但变量本身是 `null`（除非手动 `new`）。 | 变量被赋予了一个由 Spring 管理的、可用的实例。               |
| **核心** | **类型声明**                                          | **实例注入**                                                 |

所以，在 Spring 框架中，`import` 和 `@Autowired` 必须同时使用：
*   用 `import` 告诉编译器 `EmployeeService` 是什么。
*   用 `@Autowired` 告诉 Spring 框架在运行时给我一个 `EmployeeService` 的实例。
