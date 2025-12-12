### 前言：排版工具与书写工具的讨论

LaTeX 是一种“非所见即所得”的排版系统，用户需要输入特定的代码，保存在后缀为.tex 的文件中，通过编译得到所需的 pdf 文件，例如以下代码：

```tex
\documentclass{article}

\begin{document}

Hello, world!

\end{document}
```

最后输出的结果是一个 pdf 文件，内容是”Hello, world!“。

如何理解“非所见即所得”呢？在这里举个“所见即所得”的例子：Word。Word 的界面就是一张 A4 纸，输入的时候是什么样子，最后呈现出来就是什么样子。这给了我们极高的 **自由度**，也非常容易上手，但是有如下问题： - 对于对细节不敏感的用户，Word 的排版常常会在细节存在问题，比如两段话之间行间距不同、字体不同、标题样式不同等； - 对于撰写论文的用户，Word 的标题、章节、图表、参考文献等无法自动标号，也很难在正文中引用； - 对于有公式输入需求的用户，Word 自带的公式不稳定，而公式插件效果常常不好。

相比之下，使用 LaTeX 进行排版，就像是在铺好的轨道上驾驶火车一样。使用 LaTeX 没有办法像 Word 一样非常自由，但是可以保证 **规范性**，这使得 LaTeX 非常适合用于论文的排版。在学习的过程中，也将会感受到这一点。

无论是 LaTeX 还是 Word，其归根结底都只是 **排版工具**，用 Word 也可以排出 LaTeX 的效果，用 LaTeX 也可以排出 Word 的效果。另外，笔者最建议的 **书写工具** 是 Markdown，其书写的过程中可以不在意排版，也支持使用 LaTeX 语法输入公式，与 LaTeX 之间的转换非常方便。

- 

#### 利用 LaTeX 编写文档

#### 文档类型

TeX 有多种文档类型可选，笔者较常用的有如下几种类型：

- 对于英文，可以用 `book`、`article` 和 `beamer`；
- 对于中文，可以用 `ctexbook`、`ctexart` 和 `ctexbeamer`，这些类型自带了对中文的支持。

不同的文件类型，编写的过程中也会有一定的差异，如果直接修改文件类型的话，甚至会报错。以下统一选用 `ctexart`。在编辑框第一行，输入如下内容来设置文件类型：

```tex
\documentclass{ctexart}
```

另外，一般也可以在 `\documentclass` 处设置基本参数，笔者通常设置默认字体大小为 12pt，纸张大小为 A4，单面打印。需要将第一行的内容替换为：

```tex
\documentclass[12pt, a4paper, oneside]{ctexart}
```

文件的正文部分需要放入 document 环境中，在 document 环境外的部分不会出现在文件中。

```tex
\documentclass[12pt, a4paper, oneside]{ctexart}

\begin{document}

这里是正文. 

\end{document}
```

#### 宏包

为了完成一些功能（如定理环境），还需要在导言区，也即 document 环境之前加载宏包。加载宏包的代码是 `\usepackage{}`。本份教程中，与数学公式与定理环境相关的宏包为 `amsmath`、`amsthm`、`amssymb`，用于插入图片的宏包为 `graphicx`，代码如下：

```tex
\usepackage{amsmath, amsthm, amssymb, graphicx}
```

另外，在加载宏包时还可以设置基本参数，如使用超链接宏包 `hyperref`，可以设置引用的颜色为黑色等，代码如下：

```tex
\usepackage[bookmarks=true, colorlinks, citecolor=blue, linkcolor=black]{hyperref}
```

#### 标题

标题可以用 `\title{}` 设置，作者可以用 `\author` 设置，日期可以用 `\date{}` 设置，这些都需要放在导言区。为了在文档中显示标题信息，需要使用 `\maketitle`。例如：

```tex
\documentclass[12pt, a4paper, oneside]{ctexart}
\usepackage{amsmath, amsthm, amssymb, graphicx}
\usepackage[bookmarks=true, colorlinks, citecolor=blue, linkcolor=black]{hyperref}

% 导言区

\title{我的第一个\LaTeX 文档}
\author{Dylaaan}
\date{\today}

\begin{document}

\maketitle

这里是正文. 

\end{document}
```

#### 正文

正文可以直接在 document 环境中书写，没有必要加入空格来缩进，因为文档默认会进行首行缩进。相邻的两行在编译时仍然会视为同一段。在 LaTeX 中，另起一段的方式是使用一行相隔，例如：

```tex
我是第一段. 

我是第二段.
```

这样编译出来就是两个段落。在正文部分，多余的空格、回车等等都会被自动忽略，这保证了全文排版不会突然多出一行或者多出一个空格。另外，另起一页的方式是：

```tex
\newpage
```

笔者在编写文档时，为了保证美观，通常将中文标点符号替换为英文标点符号（需要注意的是英文标点符号后面还有一个空格），这比较适合数学类型的文档。

在正文中，还可以设置局部的特殊字体：

| 字体     | 命令      |
| -------- | --------- |
| 直立     | \textup{} |
| 意大利   | \textit{} |
| 倾斜     | \textsl{} |
| 小型大写 | \textsc{} |
| 加宽加粗 | \textbf{} |

### 章节

对于 `ctexart` 文件类型，章节可以用 `\section{}` 和 `\subsection{}` 命令来标记，例如：

```tex
\documentclass[12pt, a4paper, oneside]{ctexart}
\usepackage{amsmath, amsthm, amssymb, graphicx}
\usepackage[bookmarks=true, colorlinks, citecolor=blue, linkcolor=black]{hyperref}

% 导言区

\title{我的第一个\LaTeX 文档}
\author{Dylaaan}
\date{\today}

\begin{document}

\maketitle

\section{一级标题}

\subsection{二级标题}

这里是正文. 

\subsection{二级标题}

这里是正文. 

\end{document}
```

#### 目录

在有了章节的结构之后，使用 `\tableofcontents` 命令就可以在指定位置生成目录。通常带有目录的文件需要编译两次，因为需要先在目录中生成.toc 文件，再据此生成目录。

```tex
\documentclass[12pt, a4paper, oneside]{ctexart}
\usepackage{amsmath, amsthm, amssymb, graphicx}
\usepackage[bookmarks=true, colorlinks, citecolor=blue, linkcolor=black]{hyperref}

% 导言区

\title{我的第一个\LaTeX 文档}
\author{Dylaaan}
\date{\today}

\begin{document}

\maketitle

\tableofcontents

\section{一级标题}

\subsection{二级标题}

这里是正文. 

\subsection{二级标题}

这里是正文. 

\end{document}
```

#### 图片

插入图片需要使用 `graphicx` 宏包，建议使用如下方式：

```tex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=8cm]{图片.jpg}
    \caption{图片标题}
\end{figure}
```

其中，`[htbp]` 的作用是自动选择插入图片的最优位置，`\centering` 设置让图片居中，`[width=8cm]` 设置了图片的宽度为 8cm，`\caption{}` 用于设置图片的标题。

#### 表格

LaTeX 中表格的插入较为麻烦，可以直接使用 [Create LaTeX tables online – TablesGenerator.com](https://link.zhihu.com/?target=https%3A//www.tablesgenerator.com/%23) 来生成。建议使用如下方式：

```tex
\begin{table}[htbp]
    \centering
    \caption{表格标题}
    \begin{tabular}{ccc}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
        7 & 8 & 9
    \end{tabular}
\end{table}
```

#### 列表

LaTeX 中的列表环境包含无序列表 `itemize`、有序列表 `enumerate` 和描述 `description`，以 `enumerate` 为例，用法如下：

```tex
\begin{enumerate}
    \item 这是第一点; 
    \item 这是第二点;
    \item 这是第三点. 
\end{enumerate}
```

另外，也可以自定义 `\item` 的样式：

```tex
\begin{enumerate}
    \item[(1)] 这是第一点; 
    \item[(2)] 这是第二点;
    \item[(3)] 这是第三点. 
\end{enumerate}
```

#### 定理环境

定理环境需要使用 `amsthm` 宏包，首先在导言区加入：

```text
\newtheorem{theorem}{定理}[section]
```

其中 `{theorem}` 是环境的名称，`{定理}` 设置了该环境显示的名称是“定理”，`[section]` 的作用是让 `theorem` 环境在每个 section 中单独编号。在正文中，用如下方式来加入一条定理：

```tex
\begin{theorem}[定理名称]
    这里是定理的内容. 
\end{theorem}
```

其中 `[定理名称]` 不是必须的。另外，我们还可以建立新的环境，如果要让新的环境和 `theorem` 环境一起计数的话，可以用如下方式：

```tex
\newtheorem{theorem}{定理}[section]
\newtheorem{definition}[theorem]{定义}
\newtheorem{lemma}[theorem]{引理}
\newtheorem{corollary}[theorem]{推论}
\newtheorem{example}[theorem]{例}
\newtheorem{proposition}[theorem]{命题}
```

另外，定理的证明可以直接用 `proof` 环境。

#### 页面

最开始选择文件类型时，我们设置的页面大小是 a4paper，除此之外，我们也可以修改页面大小为 b5paper 等等。

一般情况下，LaTeX 默认的页边距很大，为了让每一页显示的内容更多一些，我们可以使用 `geometry` 宏包，并在导言区加入以下代码：

```tex
\usepackage{geometry}
\geometry{left=2.54cm, right=2.54cm, top=3.18cm, bottom=3.18cm}
```

另外，为了设置行间距，可以使用如下代码：

```tex
\linespread{1.5}
```

#### 页码

默认的页码编码方式是阿拉伯数字，用户也可以自己设置为小写罗马数字：

```tex
\pagenumbering{roman}
```

另外，`aiph` 表示小写字母，`Aiph` 表示大写字母，`Roman` 表示大写罗马数字，`arabic` 表示默认的阿拉伯数字。如果要设置页码的话，可以用如下代码来设置页码从 0 开始：

```tex
\setcounter{page}{0}
```

#### 数学公式的输入方式

#### 行内公式

行内公式通常使用 `$..$` 来输入，这通常被称为公式环境，例如：

```tex
若$a>0$, $b>0$, 则$a+b>0$.
```

若 $a>0$, $b>0$, 则 $a+b>0$.

公式环境通常使用特殊的字体，并且默认为斜体。需要注意的是，只要是公式，就需要放入公式环境中。如果需要在行内公式中展现出行间公式的效果，可以在前面加入 `\displaystyle`，例如

```tex
设$\displaystyle\lim_{n\to\infty}x_n=x$.
```

设 $\displaystyle\lim_{n\to\infty}x_n=x$

#### 行间公式

行间公式需要用 `\[..\]` 或者 `$$..$$` 来输入，推荐使用 `\[..\]`，输入方式如下：

```tex
若$a>0$, $b>0$, 则
\[
a+b>0.
\]
```

若 $a>0, b>0$, 则

$a+b>0.$



关于具体的输入方式，可以参考 [在线 LaTeX 公式编辑器-编辑器 (latexlive.com)](https://link.zhihu.com/?target=https%3A//www.latexlive.com/)，在这里只列举一些需要注意的。

#### 上下标

上标可以用 `^` 输入，例如 `a^n`，效果为 a^n ；下标可以用 `_` 来输入，例如 `a_1`，效果为 a_1 。上下标只会读取第一个字符，如果上下标的内容较多的话，需要改成 `^{}` 或 `_{}`。

$x_1$  	$x_n$			$x_n^m$		$x_{i+j}^{m+n}$

#### 分式

分式可以用 `\dfrac{}{}` 来输入，例如 `\dfrac{a}{b}`，效果为 \dfrac{a}{b} 。为了在行间、分子、分母或者指数上输入较小的分式，可以改用 `\frac{}{}`，例如 `a^\frac{1}{n}`，效果为 $a^\frac{1}{n}$ 。

#### 括号

括号可以直接用 `(..)` 输入，但是需要注意的是，有时候括号内的内容高度较大，需要改用 `\left(..\right)`。例如 `\left(1+\dfrac{1}{n}\right)^n`，效果是 $ \left(1+\dfrac{1}{n}\right)^n$ 。

在中间需要隔开时，可以用 `\left(..\middle|..\right)`。

另外，输入大括号{}时需要用 `\{..\}`，其中 `\` 起到了转义作用。

#### 加粗

对于加粗的公式，建议使用 `bm` 宏包，并且用命令 `\bm{}` 来加粗，这可以保留公式的斜体。

#### 大括号

在这里可以使用 `cases` 环境，可以用于分段函数或者方程组，例如

```tex
$$
f(x)=\begin{cases}
    x, & x>0, \\
    -x, & x\leq 0.
\end{cases}
$$
```

效果为

$f(x)=\begin{cases} x, & x>0, \\ -x, & x\leq 0. \end{cases}$

#### 多行公式

多行公式通常使用 `aligned` 环境，例如

```tex
$$
\begin{aligned}
a & =b+c \\
& =d+e
\end{aligned}
$$
```

效果为

$\begin{aligned} a & =b+c \\ & =d+e \end{aligned}$

#### 矩阵和行列式

矩阵可以用 `bmatrix` 环境和 `pmatrix` 环境，分别为方括号和圆括号，例如

```tex
$$
\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}
$$
```

效果为
$$
 \begin{bmatrix} a & b \\ c & d \end{bmatrix} 
$$

如果要输入行列式的话，可以使用 `vmatrix` 环境，用法同上。

---

#### 常用数学公式和符号

在 latex 中，字符 #、$、%、&、~、^、n、_、{、} 的含义特殊，不能直接表示

| 符号 |    命令    | 符号 | 命令 | 符号 | 命令 |
| :--: | :--------: | :--: | :--: | :--: | :--: |
|  $   |     \$     |  %   |  \%  |  {   |  \{  |
|  _   |     \_     |  }   |  \}  |  #   |  \#  |
|  &   |     \&     |  ^   | \^{} |  ~   | \~{} |
|  \   | \backslash |      |      |      |      |

#### 公式中常用到的希腊字母

|        符号        |      命令      |           符号            |         命令          |        符号        |      命令      |
| :----------------: | :------------: | :-----------------------: | :-------------------: | :----------------: | :------------: |
|      $\alpha$      |     \alpha     |          $\beta$          |         \beta         | $\gamma$  $\Gamma$ | \gamma  \Gamma |
| $\delta$  $\Delta$ | \delta  \Delta | $\epsilon$  $\varepsilon$ | \epsilon  \varepsilon |      $\zeta$       |     \zeta      |
|       $\eta$       |      \eta      |   $\theta$  $\vartheta$   |   \theta  \vartheta   |      $\iota$       |     \iota      |
|      $\kappa$      |     \kappa     |         $\Theta$          |        \Theta         |     $\lambda$      |    \lambda     |
|       $\mu$        |      \mu       |           $\nu$           |          \nu          |    $\xi$  $\Xi$    |    \xi  \Xi    |
|    $\pi$  $\Pi$    |    \pi  \Pi    |         $o$  $O$          |         o  O          | $\rho$  $\varrho$  | \rho  \varrho  |
| $\sigma$  $\Sigma$ | \sigma  \Sigma |          $\tau$           |         \tau          |     $\upsilon$     |    \upsilon    |
| $\phi$  $\varphi$  | \phi  \varphi  |          $\chi$           |         \chi          |   $\psi$  $\Psi$   |   \psi  \Psi   |
| $\omega$  $\Omega$ | \omega  \Omega |          $\Phi$           |         \Phi          |     $\Upsilon$     |    \Upsilon    |

#### 各种运算符号

|     符号     |    命令    |    符号     |   命令    |      符号      |    命令    |
| :----------: | :--------: | :---------: | :-------: | :------------: | :--------: |
|   $\times$   |   \times   |   $\div$    |   \div    | $\pm$  ($\mp$) | \pm  (\mp) |
|  $\otimes$   |  \otimes   |  $\oplus$   |  \oplus   |    $\odot$     |   \odot    |
|  $\oslash$   |  \oslash   | $\triangle$ | \triangle |     $\neq$     |    \neq    |
|   $\equiv$   |   \equiv   |    $\pm$    |    \pm    |   $\ominus$    |  \ominus   |
|    $\le$     |    \le     |     $<$     |     <     |      $>$       |     >      |
|    $\ge$     |    \ge     |   $\cup$    |   \cup    |   $\bigcup$    |  \bigcup   |
| $\bigotimes$ | \bigotimes | $\bigcirc$  | \bigcirc  |     $\vee$     |    \vee    |

|       符号        |      命令       |         符号          |        命令         |       符号       |      命令      |
| :---------------: | :-------------: | :-------------------: | :-----------------: | :--------------: | :------------: |
|     $\bigvee$     |     \bigvee     |       $\sqcap$        |       \sqcap        |    $\subset$     |    \subset     |
|    $\subseteq$    |    \subseteq    |      $\setminus$      |      \setminus      |   $\parallel$    |   \parallel    |
|     $\propto$     |     \propto     |       $\forall$       |       \forall       |     $\aleph$     |     \aleph     |
|      $\ell$       |      \ell       |       $\uplus$        |       \uplus        |      $\cap$      |      \cap      |
|     $\bigcap$     |     \bigcap     |      $\bigoplus$      |      \bigoplus      |     $\amalg$     |     \amalg     |
|     $\wedge$      |     \wedge      |      $\bigwedge$      |      \bigwedge      |     $\sqcup$     |     \sqcup     |
|     $\supset$     |     \supset     |      $\supseteq$      |      \supseteq      |      $\mid$      |      \mid      |
|      $\neg$       |      \neg       |       $\exists$       |       \exists       |     $\nabla$     |     \nabla     |
|    $\partial$     |    \partial     |      $\biguplus$      |      \biguplus      |      $\ast$      |      \ast      |
|      $\circ$      |      \circ      |         $\to$         |         \to         |      $\lhd$      |      \lhd      |
|     $\unlhd$      |     \unlhd      |        $\prec$        |        \prec        |      $\sim$      |      \sim      |
|      $\cong$      |      \cong      |         $\ll$         |         \ll         |      $\in$       |      \in       |
|     $\ldots$      |     \ldots      |       $\vdots$        |       \vdots        |     $\imath$     |     \imath     |
|      $\int$       |      \int       |        $\star$        |        \star        |    $\bullet$     |    \bullet     |
|     $\infty$      |     \infty      |        $\rhd$         |        \rhd         |     $\unrhd$     |     \unrhd     |
|      $\succ$      |      \succ      |       $\approx$       |       \approx       |     $\doteq$     |     \doteq     |
|       $\gg$       |       \gg       |       $\notin$        |       \notin        |     $\cdots$     |     \cdots     |
|     $\ddots$      |     \ddots      |       $\jmath$        |       \jmath        |     $\oint$      |     \oint      |
|  $\triangleleft$  |  \triangleleft  |   $\bigtriangleup$    |    \bigtriangle     |    $\uparrow$    |    \uparrow    |
|   $\leftarrow$    |   \leftarrow    |     $\Leftarrow$      |     \Leftarrow      | $\longleftarrow$ | \longleftarrow |
| $\Longleftarrow$  | \Longleftarrow  |   $\leftrightarrow$   |   \leftrightarrow   |    $\searrow$    |    \searrow    |
| $\leftharpoonup$  | \leftharpoonup  |  $\leftharpoondown$   |  \leftharpoondown   |    $\swarrow$    |    \swarrow    |
|    $\nwarrow$     |    \nwarrow     | $\rightleftharpoons$  | \rightleftharpoons  |   $\triangle$    |   \triangle    |
|    $\diamond$     |    \diamond     |     $\heartsuit$      |     \heartsuit      |   $\spadesuit$   |   \spadesuit   |
| $\triangleright$  | \triangleright  |  $\bigtriangledown$   |  \bigtriangledown   |   $\downarrow$   |   \downarrow   |
|   $\rightarrow$   |   \rightarrow   |     $\Rightarrow$     |     \Rightarrow     |    $\nearrow$    |    \nearrow    |
| $\Longrightarrow$ | \Longrightarrow | $\longleftrightarrow$ | \longleftrightarrow |       $\S$       |       \S       |
| $\rightharpoonup$ | \rightharpoonup |  $\rightharpoondown$  |  \rightharpoondown  |  $\diamondsuit$  |  \diamondsuit  |
| $\longrightarrow$ | \longrightarrow |   $\Leftrightarrow$   |   \Leftrightarrow   |     $\angle$     |     \angle     |
|    $\clubsuit$    |    \clubsuit    | $\Longleftrightarrow$ | \Longleftrightarrow |    $\because$    |    \because    |
|   $\therefore$    |   \therefore    |        $\log$         |        \log         |      $mod$       |      mod       |
|      $\bot$       |      \bot       |         $sin$         |         sin         |      $cos$       |      cos       |
|       $tan$       |       tan       |         $cot$         |         cot         |      $sec$       |      sec       |
|       $csc$       |       csc       |         $lg$          |         lg          |       $ln$       |       ln       |

#### 字形字体设置

|     命令     |        实例         |      说明      |
| :----------: | :-----------------: | :------------: |
|    \boxed    |   $\boxed{text}$    | 斜体加上文本框 |
|    \fbox     |    $\fbox{text}$    |   添加文本框   |
|   \mathbf    |   $\mathbf{text}$   |    字体加粗    |
| \boldsymbol  | $\boldsymbol{text}$ |   斜体再加粗   |
| A  \large{A} |   A  $\large{A}$    |    加大字体    |
| A  \small{A} |   A  $\small{A}$    |    缩小字体    |

#### 公式中常出现的式子样式

|               命令               |                实例                |              说明               |
| :------------------------------: | :--------------------------------: | :-----------------------------: |
|              a^{b}               |              $a^{b}$               |    上标（单字符可以省略{}）     |
|              a_{b}               |              $a_{b}$               |    下标（单字符可以省略{}）     |
|              a_{bb}              |              $a_{bb}$              |   下标（多字符，不可省略{}）    |
|            \sqrt{ab}             |            $\sqrt{ab}$             |             开平方              |
|           \sqrt [5]{ab}           |           $\sqrt[5]{ab}$           | 开 5 次根号，根号下多个字符时用{} |
|  \sideset{^1_2}{^3_4}\bigotimes  |  $\sideset{^1_2}{^3_4}\bigotimes$  |         左右都有上下标          |
| {}^{12}_{\phantom{1}6}\textrm{C} | ${}^{12}_{\phantom{1}6}\textrm{C}$ |         上下标都在左边          |
|           \frac{a}{b}            |           $\frac{a}{b}$            |              分数               |
|    1+\frac{a}{1+\frac{b}{c}}     |    $1+\frac{a}{1+\frac{b}{c}}$     |       分数，字体逐级变小        |
|    1+\frac{a}{1+\dfrac{b}{c}}    |    $1+\frac{a}{1+\dfrac{b}{c}}$    |   分数，字号为独立公式的大小    |
|          \binom{a}{b^2}          |          $\binom{a}{b^2}$          |             组合数              |
|         \dbinom{a}{b^2}          |         $\dbinom{a}{b^2}$          |             组合数              |
|         \tbinom{a}{b^2}          |         $\tbinom{a}{b^2}$          |             组合数              |
|         \stackrel{a}{b}          |         $\stackrel{a}{b}$          |     下面字符大，上面字符小      |
|          {a \atop b+c}           |           $a \atop b+c$            |          上下符号等大           |
|         {a \choose b+c}          |         ${a \choose b+c}$          |      上下符号等大，带括号       |
|        \sum_{i = a}^{b}c_i         |        $\sum_{i=a}^{b}c_i$         | 求和公式  $\Sigma_{i=a}^{b}c_i$ |
|    \sum\nolimits_{i = a}^{b}c_i    |    $\sum\nolimits_{i=a}^{b}c_i$    |    limits 和 nolimits 是否压缩     |
|        \prod_{i = a}^{b}c_i        |        $\prod_{i=a}^{b}ci$         |            求积公式             |
|   \prod\nolimits_{i = a}^{b}_c_i   |    $\prod\nolimits_{i=a}^{b}ci$    |    limits 和 nolimits 是否压缩     |
|        \int_{a}^{b}f(x)dx        |        $\int_{a}^{b}f(x)dx$        |             求积分              |
|   \int\nolimits_{a}^{b}f(x)dx    |   $\int\nolimits_{a}^{b}f(x)dx$    |    limits 和 nolimits 是否压缩     |
|              \iint               |              $\iint$               |            二重积分             |
|              \iiint              |              $\iiint$              |            三重积分             |
|            \idotsint             |            $\idotsint$             |            积分形式             |
|       \xleftarrow [x+y]{x}        |       $\xleftarrow[x+y]{x}$        |           可自行调整            |
|       \xrightarrow [x+y]{x}       |       $\xrightarrow[x+y]{x}$       |           可自行调整            |
|    \overset{x+y}{\rightarrow}    |    $\overset{x+y}{\rightarrow}$    |      长度固定，适用单字符       |
|       \overrightarrow{x+y}       |       $\overrightarrow{x+y}$       |     长度不固定，适用多字符      |
|      \underrightarrow{x+y}       |      $\underrightarrow{x+y}$       |     长度不固定，适用多字符      |
|             \bar{a}              |             $\bar{a}$              |      单个字母上面加上横线       |
|             \vec{x}              |             $\vec{x}$              |         向量，单个字母          |
|       \overrightarrow{AB}        |       $\overrightarrow{AB}$        |         向量，多个字母          |
|        \overleftarrow{AB}        |        $\overleftarrow{AB}$        |         向量，多个字母          |
|            \tilde{x}             |            $\tilde{x}$             |        波浪线，单个字母         |
|         \widetilde{xyz}          |         $\widetilde{xyz}$          |        波浪线，多个字符         |
|             \dot{x}              |             $\dot{x}$              |               点                |
|             \hat{x}              |             $\hat{x}$              |              尖帽               |
|           \widehat{x}            |          $\widehat{xyz}$           |             大尖帽              |
|            \grave{x}             |            $\grave{x}$             |              声调               |
|           \mathring{x}           |           $\mathring{x}$           |              声调               |
|             \ddot{x}             |             $\ddot{x}$             |              声调               |
|            \check{x}             |            $\check{x}$             |              声调               |
|            \breve{x}             |            $\breve{x}$             |              声调               |
|            \dddot{x}             |            $\dddot{x}$             |              声调               |
|              (a^b)               |              $(a^b)$               |              括号               |
|         \left(a^b\right)         |         $\left(a^b\right)$         |         括号，可变大小          |
|             \{a^b\}              |             $\{a^b\}$              |              括号               |
|  \left\lbrace a^b \right\rbrace  |  $\left\lbrace a^b \right\rbrace$  |         括号，可变大小          |
|              [a^b]               |              $[a^b]$               |              括号               |
|        \left [ a^b \right]        |        $\left[ a^b \right]$        |         括号，可变大小          |
|       \lfloor a^b \rfloor        |       $\lfloor a^b \rfloor$        |              括号               |
|        \lceil a^b \rceil         |        $\lceil a^b \rceil$         |              括号               |
|          \overline{a+b}          |          $\overline{a+b}$          |       多个字母上面加横线        |
|     \overbrace{a\dots a}^{n}     |    $\overbrace{a \dots a}^{n}$     |           括号在上面            |
|    \underbrace{a \dots a}_{n}    |    $\underbrace{a \dots a}_{n}$    |           括号在下面            |
|            a \quad b             |            $a \quad b$             |           一个 m 的宽度           |
|        a \<!--qquad--> b         |            $a \qquad b$            |           两个 m 的宽度           |
|              a \: b              |              $a \: b$              |          1/3 个 m 的宽度           |
|              a \: b              |              $a \; b$              |          2/7 个 m 的宽度           |
|              a \, b              |              $a \, b$              |          1/6 个 m 的宽度           |
|                ab                |                $ab$                |            没有空格             |
|              a \! b              |              $a \! b$              |        缩进 1/6 个 m 的宽度         |

公式中括号的应用，可以用一系列命令 (\big, \Big, \bigg, \Bigg) 改变括号大小，例如

{% raw %}

`\Bigg( \bigg( \Big( \big((x) \big) \Big) \bigg) \Bigg)` 

 `\Bigg\{ \bigg\{ \Big\{ \big\{\{x\} \big\} \Big\} \bigg\} \Bigg\}`

$\Bigg( \bigg( \Big( \big((x) \big) \Big) \bigg) \Bigg) $

$ \Bigg\{ \bigg\{ \Big\{ \big\{\{x\} \big\} \Big\} \bigg\} \Bigg\}$ 

{{sensitive}}

{% endraw %}

也可以用自动模式自动调节大小
$$
f(x, y, z) = 3y^2z \left( 3+\frac{7x+5}{1+y^2} \right)
$$

$$
f\left(\left [\frac{1+\left\{x, y\right\}}{\left(\frac{x}{y}+\frac{y}{x}\right)\left(u+1\right)}+a\right]^{3/2}\right)
$$

#### 换行和&、\begin{aligned}  \end{aligned}

其中 `\begin{aligned}` 与 `\end{aligned}` 开辟一个环境，可以换行。
$$
\begin{aligned}a =&\left(1+2+3+ \cdots \right. \\& \cdots+ \left. \infty-2+\infty-1+\infty\right)\end{aligned}
$$
分隔符\middle 的作用，以及\\\可以公式换行
$$
\begin{aligned} P =\left(A = 2|\frac{A^2}{B}> 4\right)  \\  P =\left(A = 2\middle|\frac{A^2}{B}> 4\right) \end{aligned}
$$
#### 分段函数

在单行文本中，不是只能写一行公式，而是整个公式占用一行，这里用到了 cases 环境，把多个情况放在一个公式中，每个情况用\\换行
$$
L(Y, f(X))=\begin{cases}
1,\quad &Y\neq f(X) \\ 
0,\quad &Y = f(X)
\end{cases}
$$

在公式环境下编写公式，公式环境有很多种，这里列举一些常用环境。例如 equation
环境，公式放在这个环境中，自动居中对齐，带有公式编号
$$
\begin{equation}f(x)= 3x^2+6(x-2)-1\end{equation}
$$

$\begin{equation}
f(x)= 3x^{2}+6(x-2)-1 \quad		\tag{1}
\end{equation}$
		
typora 中单个 `$` 包裹即使用 `equation` 环境也做不到居中，typora 中还是得 ctrl+shift+m，行间公式且自动带编号（偏好设置里加上）。

\begin{equation}\begin{aligned}x =&\left(a+b+c \right. \\&\left. +d+e+f \right)\end{aligned}\end{equation}		

两个&标明了换行后对齐的位置

$\begin{equation}\begin{aligned}x=&\left(a+b+c \right. \\&\left. +d+e+f \right)\end{aligned} \quad \tag{2}\end{equation}$   

\left.\begin{aligned}x+y &> 5 \\ x-y &> 11 \end{aligned}\ \right\}\Rightarrow x^2-y^2 > 55

还可以把括号放在左边，只需要换一下“影子括号”位置就可以了。
$$
\left.\begin{aligned}x+y &> 5 \\ x-y &> 11 \end{aligned}\ \right\}\Rightarrow x^2-y^2 > 55
$$
#### 表格、矩阵

在 equation 环境中添加 array 环境，就可以实现数组或者表格的形式，其中每个元素用 & 分隔， \hline 表示横线。公式中如果有中文，就要用\text{}或者\mbox{}装载，否则不能正常输出中文。
$$
\begin{equation}\begin{array}{c|l|c|r}
n & \text{左对齐} & \text{居中对齐} & \text{右对齐} \\
\hline1 & 0.24 & 1 & 125 \\
\hline2 & -1 & 189 & -8 \\
\hline3 & -20 & 2000 & 1+10i
\end{array}\end{equation}
$$
单行文本也可以表示矩阵和公式数组。

$$
\begin{aligned}\left(\begin{array}{ccc|c}
a11 & a12 & a13 & b1 \\
a21 & a22 & a23 & b2 \\
a31 & a32 & a33 & b3 \\
\end{array}\right)\end{aligned}
$$
`\left\{` 表示一个左大括号，它会自动调整大小以适应其后的内容。通常，`\left\{` 配合 `\right\}` 使用，`\right\}` 表示相应的右大括号，以确保左右括号大小一致且适应所包裹内容的大小。\right.表示不显示右边的大括号。\begin{array}和\end{array}表示数组、表格等环境，{ccc|c}表示表格格式，比如有几列等等。
$$
\left\{
\begin{array}{c}
a_1x+b_1y+c_1z = d_1 \\
a_2x+b_2y+c_2z = d_2 \\
a_3x+b_3y+c_3z = d_3
\end{array}
\right.$
$$
<img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F07%2F%E7%9F%A9%E9%98%B5.png" alt="latex公式矩阵表达" style="zoom:60%;" />
$$
\begin{matrix}
a &b &c \\
d &e &f \\
g &h &j
\end{matrix}
$$

$$
\begin{bmatrix}
a &b &c \\
d &e &f \\
g &h &j
\end{bmatrix}
$$

$$
\left(
\begin{matrix}
a &b &c \\
d &e &f \\
g &h &j
\end{matrix}
\right)
$$









































