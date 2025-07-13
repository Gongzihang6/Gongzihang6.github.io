// Wrap every letter in a span
var textWrapper = document.querySelector('.ml3');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml3 .letter',
    opacity: [0,1],
    easing: "easeInOutQuad",
    duration: 2250,
    delay: (el, i) => 150 * (i+1)
  }).add({
    targets: '.ml3',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });


//全屏视频
// var video = document.getElementById("video1");
// var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

// if (isMobile) {
//   video.style.display = "none";
//   video.muted = true;
// } else {
//   video.volume = 0.5; // 或者根据需要设置适当的音量值，例如 0.5 表示 50% 的音量
// }

// 优化
// const container = document.querySelector('.container');
// const boxes = document.querySelectorAll('p');

// // Read a layout property
// const newWidth = container.offsetWidth;

// for (var i = 0; i < boxes.length; i++) {    
//     // Then invalidate layouts with writes.
//     boxes[i].style.width = newWidth + 'px';
// }
// const width = box.offsetWidth;
// box.classList.add('big');

// // When the user clicks on a link/button:
// async function navigateToSettingsPage() {
//   // Capture and visually freeze the current state.
//   await document.documentTransition.prepare({
//     rootTransition: 'cover-up',
//     sharedElements: [element1, element2, element3],
//   });
//   // This is a function within the web app:
//   updateDOMForSettingsPage();
//   // Start the transition.
//   await document.documentTransition.start({
//     sharedElements: [element1, element4, element5],
//   });
//   // Transition complete!
// }
// 优化end








// docs/javascripts/extra.js

/**
 * 自动为代码块添加折叠功能
 *
 * 策略：
 * 1. 仅为超过 N 行的代码块添加折叠功能，避免为短代码添加不必要的按钮。
 * 2. 默认状态为折叠。
 * 3. 创建一个美观的、可点击的按钮来控制折叠/展开。
 */
document.addEventListener("DOMContentLoaded", () => {
  const FOLD_THRESHOLD_LINES = 15; // 设置一个阈值，超过15行的代码块才会被折叠

  // 获取所有由Material主题渲染的代码块容器
  const codeBlocks = document.querySelectorAll("div.highlight");

  codeBlocks.forEach(block => {
    // 计算代码行数（通过计算 pre > code 内部的换行符）
    const codeElement = block.querySelector("pre > code");
    if (!codeElement) return;
    
    // getComputedStyle 可以在隐藏元素上获取样式，但我们用行数更可靠
    const lines = codeElement.innerHTML.split('\n').length;

    // 如果代码行数小于阈值，则不处理
    if (lines <= FOLD_THRESHOLD_LINES) {
      return;
    }

    // 默认设置为折叠状态
    block.classList.add("code-collapsed");

    // 创建折叠/展开按钮
    const button = document.createElement("button");
    button.classList.add("code-fold-button");
    button.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="icon-expand">
        <path d="M10 4H4c-1.11 0-2 .89-2 2v6h2V6h6V4m10 16h-6v2h6c1.11 0 2-.89 2-2v-6h-2v6M4 20v-6H2v6c0 1.11.89 2 2 2h6v-2H4m10-10V4h-6v2h6v6h2Z"></path>
      </svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="icon-collapse">
        <path d="M14 20h6c1.11 0 2-.89 2-2v-6h-2v6h-6v2M4 8V2h6v2H4v6H2V2c0-1.11.89-2 2-2h6v2H4m16 0V2h-6v2h6v6h2V2c0-1.11-.89-2-2-2Z"></path>
      </svg>
      <span class="button-text">展开代码</span>
    `;

    // 将按钮添加到代码块容器的起始位置
    block.prepend(button);

    // 添加点击事件监听器
    button.addEventListener("click", () => {
      const isCollapsed = block.classList.contains("code-collapsed");
      block.classList.toggle("code-collapsed");
      button.querySelector('.button-text').textContent = isCollapsed ? "折叠代码" : "展开代码";
    });
  });
});


