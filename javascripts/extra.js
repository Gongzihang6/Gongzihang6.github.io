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






document.addEventListener('DOMContentLoaded', () => {

    /**
     * @function initializeCarousel
     * @description 初始化一个高性能的3D旋转相册组件
     * @param {HTMLElement} carouselSection - 包含相册所有元素的根容器 (.carousel-section)
     */
    function initializeCarousel(carouselSection) {
        // --- DOM元素获取 ---
        const container = carouselSection.querySelector('.carousel-container');
        if (!container) return;

        const carousel = container.querySelector('.carousel');
        const cells = Array.from(container.querySelectorAll('.carousel__cell'));
        const prevButton = carouselSection.querySelector('.carousel-prev-button');
        const nextButton = carouselSection.querySelector('.carousel-next-button');
        
        if (!carousel || cells.length === 0 || !prevButton || !nextButton) {
            console.error("轮播组件初始化失败，在", carouselSection, "中缺少必要的元素。");
            return;
        }

        // --- 核心参数计算 ---
        const cellCount = cells.length;
        const theta = 360 / cellCount;
        const cellWidth = carousel.offsetWidth;
        
        // 使用基于间距的新半径计算公式，解决图片过多时重叠和过小的问题
        const panelGap = 80;
        const circumference = cellCount * (cellWidth + panelGap);
        const radius = Math.round(circumference / (2 * Math.PI));

        // --- 动态布局与样式设置 ---
        carousel.style.setProperty('--carousel-radius', `-${radius}px`);
        cells.forEach((cell, index) => {
            const angle = theta * index;
            cell.style.transform = `rotateY(${angle}deg) translateZ(${radius}px)`;
        });

        // --- 状态管理变量 ---
        let selectedIndex = 0;
        let autoplayTimeout;
        let isDragging = false;
        let startX, startAngle;

        // 【优化2】用于requestAnimationFrame的状态变量
        let latestAngle = 0;
        let animationFrameId = null;

        // --- 核心状态更新与动画函数 ---
        function updateCarouselState() {
            const angle = theta * selectedIndex * -1;
            carousel.style.transition = 'transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            carousel.style.transform = `translateZ(-${radius}px) rotateY(${angle}deg)`;
            carousel.style.animation = 'none'; // 停止CSS动画
            
            clearTimeout(autoplayTimeout);
            autoplayTimeout = setTimeout(() => {
                carousel.style.transition = 'none'; // 为无缝切换到动画做准备
                void carousel.offsetWidth; // 强制重绘
                carousel.style.animation = `carousel_rotation 30s infinite linear`;
                const progress = (angle % 360) / 360;
                carousel.style.animationDelay = `${progress * -30}s`;
                carousel.style.animationPlayState = 'running';
            }, 1000); // 交互后3秒恢复自动旋转
        }
        
        // 【优化2】使用rAF来更新transform，与浏览器渲染同步
        function animateDrag() {
            carousel.style.transform = `translateZ(-${radius}px) rotateY(${latestAngle}deg)`;
            animationFrameId = null; // 动画帧已执行，清空ID
        }

        // --- 事件监听器 ---
        prevButton.addEventListener('click', () => { selectedIndex--; updateCarouselState(); });
        nextButton.addEventListener('click', () => { selectedIndex++; updateCarouselState(); });

        // 拖拽开始 (pointerdown)
        container.addEventListener('pointerdown', e => {
            e.preventDefault();
            isDragging = true;
            container.style.cursor = 'grabbing';
            startX = e.pageX;
            carousel.style.animationPlayState = 'paused';
            clearTimeout(autoplayTimeout);
            
            const computedStyle = window.getComputedStyle(carousel);
            const transformMatrix = new DOMMatrix(computedStyle.transform);
            startAngle = Math.atan2(transformMatrix.m13, transformMatrix.m11) * (180 / Math.PI);
            
            // 捕获指针，解决“粘滞拖动”Bug
            container.setPointerCapture(e.pointerId);
        });
        
        // 拖拽过程 (pointermove)
        container.addEventListener('pointermove', e => {
            if (!isDragging) return;
            const moveX = e.pageX - startX;
            const dragAngle = (moveX / container.offsetWidth) * 180;
            latestAngle = startAngle - dragAngle; // 保持正确的拖动方向
            
            // 【优化2】不直接操作DOM，而是请求下一帧来更新
            if (!animationFrameId) {
                animationFrameId = requestAnimationFrame(animateDrag);
            }
        });

        // 拖拽结束 (pointerup, lostpointercapture)
        function endDrag() {
            if (!isDragging) return;
            isDragging = false;
            container.style.cursor = 'grab';

            // 取消可能正在等待的下一帧动画
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
            }
            
            const computedStyle = window.getComputedStyle(carousel);
            const transformMatrix = new DOMMatrix(computedStyle.transform);
            const currentAngle = Math.atan2(transformMatrix.m13, transformMatrix.m11) * (180 / Math.PI);
            selectedIndex = Math.round(currentAngle / theta);
            updateCarouselState();
        }

        container.addEventListener('pointerup', endDrag);
        container.addEventListener('lostpointercapture', endDrag);
        // 安全网：当窗口失焦时，也结束拖动
        window.addEventListener('blur', endDrag);
    }
    
    // --- 自动初始化页面上所有的轮播组件 ---
    const allCarousels = document.querySelectorAll('.carousel-section');
    allCarousels.forEach(carousel => {
        initializeCarousel(carousel);
    });
});


