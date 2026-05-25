/*
 * 文件说明：
 * 本文件用于为首页与作者页的诗词卡片异步加载“今日诗词”内容。
 *
 * 实现思路：
 * 1. 页面先渲染本地结构与占位文本，不阻塞首屏；
 * 2. 浏览器空闲时再异步加载第三方 SDK；
 * 3. SDK 加载成功后替换容器中的占位文本；
 * 4. 如果第三方脚本加载失败，则保留占位文本，不影响页面主体阅读。
 *
 * 优化收益：
 * 1. 减少外部脚本对首屏渲染的影响；
 * 2. 让首页和作者页共享同一套诗词加载逻辑；
 * 3. 便于后续继续把外部依赖做统一收口。
 */

(function () {
  var container = document.getElementById("jinrishici-container");
  if (!container) {
    return;
  }

  if (!container.textContent || !container.textContent.trim()) {
    container.textContent = "正在载入今日诗词...";
  }

  function applyPoem() {
    if (!window.jinrishici || typeof window.jinrishici.load !== "function") {
      return;
    }

    window.jinrishici.load(function (result) {
      if (result && result.data && result.data.content) {
        container.textContent = result.data.content;
      }
    });
  }

  function loadSdk() {
    if (window.jinrishici) {
      applyPoem();
      return;
    }

    var script = document.createElement("script");
    script.src = "https://sdk.jinrishici.com/v2/browser/jinrishici.js";
    script.async = true;
    script.onload = applyPoem;
    document.body.appendChild(script);
  }

  if ("requestIdleCallback" in window) {
    window.requestIdleCallback(loadSdk, { timeout: 1500 });
  } else {
    window.setTimeout(loadSdk, 400);
  }
})();
