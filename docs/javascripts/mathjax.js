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
    // 确保 aligned 等环境可用
    packages: {'[+]': ['ams']},
    // 定义行内和块级公式的分隔符
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    // 如果需要，可以保留
    processEscapes: true,
    processEnvironments: true
  }
};

document$.subscribe(() => { 
  MathJax.typesetPromise()
})
