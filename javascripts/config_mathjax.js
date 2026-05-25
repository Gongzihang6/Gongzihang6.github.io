/*
 * 文件说明：
 * 本文件负责站点中 MathJax 的配置与按需加载控制。
 *
 * 实现目标：
 * 1. 保留现有公式渲染能力，兼容 `pymdownx.arithmatex` 输出结构；
 * 2. 不再在所有页面全量加载 MathJax，而是仅在检测到公式节点时再动态注入；
 * 3. 降低无公式页面的脚本请求数量与解析开销，提升全站平均加载速度。
 *
 * 实现方式：
 * 1. 先在全局挂载 `window.MathJax` 配置；
 * 2. 在文档解析完成后检测页面中是否存在 `.arithmatex` 公式容器；
 * 3. 若存在公式，再异步加载 MathJax 主脚本；
 * 4. 若页面没有公式，则直接跳过，不产生额外远程请求。
 */

window.MathJax = {
  tex: {
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: { "[+]": ["tagformat", "mathtools", "mhchem"] }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  loader: {
    load: ["[tex]/tagformat", "[tex]/mathtools", "[tex]/mhchem"]
  }
};

(function () {
  /**
   * 判断当前页面是否真的包含公式节点。
   * Material + arithmatex 渲染后会输出带有 `arithmatex` 类名的容器，
   * 这里直接以该类名作为是否需要 MathJax 的判定依据。
   */
  function hasMathContent() {
    return Boolean(document.querySelector(".arithmatex"));
  }

  /**
   * 动态注入 MathJax 脚本。
   * 使用数据属性防止重复注入，避免与后续页面脚本扩展发生冲突。
   */
  function loadMathJax() {
    if (document.querySelector('script[data-mathjax-loader="true"]')) {
      return;
    }

    var script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js";
    script.async = true;
    script.setAttribute("data-mathjax-loader", "true");
    document.head.appendChild(script);
  }

  function bootstrapMathJax() {
    if (!hasMathContent()) {
      return;
    }
    loadMathJax();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootstrapMathJax, { once: true });
  } else {
    bootstrapMathJax();
  }
})();
