// window.MathJax = {
//   tex: {
//     inlineMath: [["\\(", "\\)"]],
//     displayMath: [["\\[", "\\]"]],
//     processEscapes: true,
//     processEnvironments: true
//   },
//   options: {
//     ignoreHtmlClass: ".*|",
//     processHtmlClass: "arithmatex"
//   }
// };


window.MathJax = {
  tex: {
    // 关键1：定义行内和行间公式的界定符
    // MathJax 将在 arithmatex 生成的 span 内部寻找这些界定符
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    // 关键2：加载 ams 宏包以支持 aligned 等环境
    packages: {'[+]': ['ams']}
  },
  // 关键3：告诉 MathJax 只处理 arithmatex 生成的特定 class
  // 这样可以避免它错误地处理页面上其他含 $ 符号的文本
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};


document$.subscribe(() => { 
  MathJax.typesetPromise()
})
