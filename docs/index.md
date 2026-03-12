---
title: 关于我
hide:
#   - navigation
#   - toc
  - feedback
#   - footer
status: new
comments: true
---





<!-- ## 关于我 -->
<!-- # <span id="jinrishici-sentence">今日诗词</span> -->

<!-- 新的、统一的今日诗词 HTML 结构 -->
<div class="poem-card">
    <div class="poem-seal"></div>
    <div id="jinrishici-container">
        <!-- 今日诗词 SDK 会自动将内容填入这里 -->
    </div>
</div>



<div class="flip-container">
<div class="image-container">
    <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/gzh.jpg" alt="Front Image">
    <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/3f58b6cea54d446e22107fde739e843.jpg" alt="Back Image">
</div>
</div>

<style>

    @import url('https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&display=swap');

    /* 强制重置相册样式 */
    #life-carousel .carousel__cell img {
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        aspect-ratio: 450/280 !important; /* 强制横屏比例 */
    }

/* --- 变量定义，方便修改主题 --- */
    :root {
        --primary-color: #4a6cfd;      /* 主题蓝色 */
        --gradient-start-color: #a5b4fc; /* 渐变起始色 (底部) */
        --title-color: #1f2937;
        --text-color: #6b7280;
        --body-bg-color: #f9fafb;  /* 页面背景色 */
        --card-bg-color: #ffffff;  /* 卡片背景白色 */
        --border-color: #e5e7eb;   /* 边框颜色 */
    }

    /* --- 区域和标题样式 --- */
    .qualification-section {
        padding: 4rem 1rem;
        background-color: var(--body-bg-color);
        text-align: center;
    }
    
    .section__title {
        font-size: 2.25rem;
        font-weight: 700;
        color: var(--title-color);
        margin-bottom: 0.5rem;
    }
    
    .section__subtitle-underline {
        display: block;
        width: 60px;
        height: 4px;
        background-color: var(--primary-color);
        margin: 0 auto 3.5rem auto;
        border-radius: 2px;
    }
    
    /* --- 时间线容器：这是关键！--- */
    .qualification__container {
        max-width: 800px;
        margin: 0 auto;
        position: relative; /* 【最关键的属性】为伪元素提供定位锚点 */
        padding-top: 2rem;  /* 为顶部的箭头留出空间 */
    }
    
    /* --- 生成单根、连续、贯穿全场的垂直线 --- */
    .qualification__container::before {
        content: '';
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        transform: translateX(-50%);
        width: 4px; /* 线的粗细 */
        z-index: 0; /* 确保线在最底层 */
        background: linear-gradient(to top, var(--gradient-start-color), var(--primary-color));
    }
    
    /* --- 网格布局 --- */
    .qualification__data {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        column-gap: 1.5rem;
        position: relative; /* 确保内容在 z-index 堆叠中 */
        z-index: 1;
    }
    
    /* --- 内容卡片样式（包含居中）--- */
    .qualification__content {
        background-color: var(--card-bg-color);
        border: 1px solid var(--border-color);
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        
        /* 【新增】Flexbox 居中样式 */
        min-height: 150px; /* 设定最小高度以实现垂直居中 */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .qualification__content h3, 
    .qualification__content span,
    .qualification__content div {
      text-align: center; /* 确保多行文本也能居中 */
    }


    /* --- 【重要】隐藏掉旧的、分散的线 --- */
    .qualification__line {
        display: none;
    }
    
    /* --- 时间点圆圈样式 --- */
    .qualification__rounder {
        display: inline-block;
        width: 20px;
        height: 20px;
        background-color: var(--primary-color);
        border: 4px solid var(--body-bg-color);
        border-radius: 50%;
    }
    
    /* --- 手绘 SVG 箭头 --- */
    .qualification__container .qualification__data > div:nth-child(2)::before {
        content: '';
        position: absolute;
        top: -30px; 
        left: 50%;
        transform: translateX(-50%);
        width: 30px;
        height: 30px;
        /* background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%234a6cfd' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='18 15 12 9 6 15'%3E%3C/polyline%3E%3C/svg%3E"); */
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath fill='none' stroke='%23000' stroke-linejoin='round' stroke-miterlimit='10' stroke-width='1.5' d='M7.91 20.889c8.302 0 12.845-6.885 12.845-12.845c0-.193 0-.387-.009-.58A9.2 9.2 0 0 0 23 5.121a9.2 9.2 0 0 1-2.597.713a4.54 4.54 0 0 0 1.99-2.5a9 9 0 0 1-2.87 1.091A4.5 4.5 0 0 0 16.23 3a4.52 4.52 0 0 0-4.516 4.516c0 .352.044.696.114 1.03a12.82 12.82 0 0 1-9.305-4.718a4.526 4.526 0 0 0 1.4 6.03a4.6 4.6 0 0 1-2.043-.563v.061a4.524 4.524 0 0 0 3.62 4.428a4.4 4.4 0 0 1-1.189.159q-.435 0-.845-.08a4.51 4.51 0 0 0 4.217 3.135a9.05 9.05 0 0 1-5.608 1.936A9 9 0 0 1 1 18.873a12.84 12.84 0 0 0 6.91 2.016Z'/%3E%3C/svg%3E");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        /* (可选) 添加一个微妙的动画，让它更生动 */
        transition: transform 0.3s ease;
    }
    /* (可选) 添加一个简单的悬停动效，让箭头轻微上浮 */
    .qualification__data:hover > div:nth-child(2)::before {
        transform: translateX(-50%) translateY(-3px);
    }
    
    /* --- 其他文本和图标样式 --- */
    .qualification__title { font-size: 1.125rem; font-weight: 600; color: var(--title-color); margin: 0 0 0.25rem 0; }
    .qualification__subtitle { display: inline-block; font-size: 0.9rem; color: var(--text-color); margin-bottom: 1rem; }
    .qualification__calendar { display: flex; align-items: center; font-size: 0.875rem; color: var(--text-color); }
    .qualification__calendar iconify-icon { font-size: 1.2rem; margin-right: 0.5rem; }
    
    /* --- 响应式设计 --- */
    @media screen and (max-width: 768px) {
        .qualification__data { grid-template-columns: auto 1fr; column-gap: 1rem; }
        .qualification__data > div:first-child:empty { display: none; }
    }







    .flip-container {
        position: relative;
        width: 280px;
        height: 280px;
        margin: 10px auto;
        display: flex;
        align-items: flex-start;
        /* 对齐顶部 */
        justify-content: flex-end;
        /* 将文字放置右上角 */
    }
    .image-container {
        position: relative;
        position: relative;
        width: 290px;
        height: 290px;
    }
    .image-container img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;    /* 图片填满容器 */
        border-radius: 50%;
        border: 4px solid #ffffff; /* 白色边框 */
        box-shadow: 0 8px 24px rgba(14, 30, 37, 0.15); /* 阴影 */
        backface-visibility: hidden; /* 隐藏背面 */
        transition: transform 0.6s ease-in-out; /* 仅对transform过渡 */
    }
    .image-container img:first-child {
        z-index: 1;
        backface-visibility: hidden;
    }
    .image-container img:last-child {
        z-index: 0;
        transform: rotateY(180deg);
        backface-visibility: hidden;
    }
    .image-container:hover img:first-child {
        transform: rotateY(180deg);
        z-index: 2;
    }
    .image-container:hover img:last-child {
        transform: rotateY(0deg);
        z-index: 3;
    }


    .qualification__button {
        font-size: 1.2rem;
        padding: 0.6rem 1rem; /* 可选：增加按钮内边距 */
    }
    
    .qualification__icon {
        font-size: 1.5rem;
        width: 1.8rem;
        height: 1.8rem;
        margin-right: 0.5rem;
        vertical-align: middle;
    }






    /* --- 全新的“山水意境卡片”样式 --- */
    
    /* 1. 【核心】修改卡片主容器，使其成为一个 Flex 容器 */
    .poem-card {
        max-width: 700px;
        margin: 2.5rem auto;
        padding: 2rem; /* 可以适当调整内边距 */
        position: relative;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        background-color: #f9fafb;
        background-image: url('https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2Fssyjt.jpg');
        background-size: cover;
        background-position: center;
        background-blend-mode: luminosity;
    
        /* --- 新增 Flexbox 属性以实现完美居中 --- */
        display: flex;
        align-items: center;    /* 垂直居中 */
        justify-content: center; /* 水平居中 */
        min-height: 200px;       /* 确保卡片有足够的高度来居中，可自行调整 */
    }
    
    /* 悬停效果保持不变 */
    .poem-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
    }
    
    /* 2. 简化诗词容器的样式 */
    #jinrishici-container {
        font-family: 'Zhi Mang Xing', 'Noto Serif SC', serif;
        font-size: 1.6rem;  /*  诗词字体大小 */
        font-weight: normal;
        color: #374151;
        line-height: 2.2;
        text-align: center;
        
        /* 以下属性不再需要，可以删除或注释掉 */
        /* display: inline-block; */
        /* position: relative; */
        /* padding: 0; */
        /* margin: 0 1rem; */
    
        transition: all 0.3s ease;
    }
    
    /* 悬停效果保持不变 */
    .poem-card:hover #jinrishici-container {
        transform: scale(1.03); /* 可以换成轻微放大的效果 */
        color: #111;
        text-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
    }




    /* 6. 装饰性元素：红色印章 */
    .poem-seal {
        position: absolute;
        
        /* 关键修改：将 top 改为 bottom，实现右下角定位 */
        bottom: 1.5rem; /* 从顶部移动到底部 */
        right: 1.5rem;  /* 右侧位置保持不变 */
        
        /* 其他样式保持不变... */
        width: 40px;
        height: 40px;
        background-color: #c93c3c;
        border: 2px solid #a63232;
        border-radius: 4px;
        opacity: 0.85; /* 可以稍微调高一点不透明度 */
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease; /* 为悬停效果添加过渡 */
    }
    
    /* (可选) 为印章添加悬停效果 */
    .poem-seal:hover {
        transform: scale(1.1);
        opacity: 1;
    }
    
    /* 2. 印章文字：统一字体 */
    .poem-seal::after {
        content: '雅'; /* 您可以改成任何想要的字 */
        
        /* 关键修改：使用和诗词一样的字体 */
        font-family: 'Zhi Mang Xing', 'Noto Serif SC', serif;
        
        /* 调整字号以适应书法字体，使其清晰可辨 */
        font-size: 1.2rem; 
    
        /* 保留并优化其他样式 */
        font-weight: 600; /* 对于书法字体，600比700可能更自然 */
        color: white; /* 确保文字是白色的 */
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    /* 7. 响应式设计，在小屏幕上调整内边距 */
    @media (max-width: 768px) {
        .poem-card {
            padding: 2rem 1.5rem;
        }
        #jinrishici-container {
            font-size: 1.1rem;
        }
    }

    .contact-container {
        display: flex;            /* 启用 Flexbox 布局 */
        justify-content: center;  /* 水平居中 */
        align-items: flex-start;  /* 顶部对齐 */
        gap: 25px;                /* 设置项目之间的间距 */
        flex-wrap: wrap;          /* 在小屏幕上允许换行 */
        text-align: center;       /* 内部文字居中 */
    }
    .contact-item {
        width: 200px; /* 控制每个二维码的宽度，可以根据需要调整 */
    }
    .contact-item img {
        width: 100%;              /* 图片宽度占满其容器 */
        height: auto;             /* 高度自动，保持比例 */
        border-radius: 12px;
        border: 3px solid white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* 添加一点阴影让效果更好 */
    }
    .contact-item p {
        margin-top: 10px;
        font-size: 15px;
        color: #333;
        line-height: 1.5;
    }

    /* ============================================= */
    /* ========= 3D 旋转相册样式 (已优化) ========= */
    /* ============================================= */

    .carousel-section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 1rem 1rem;
        background-color: transparent;
        /* overflow: hidden; */
        position: relative; /* 用于全宽出血布局 */
        width: 100%;
    }

    .carousel-title {
        font-size: 2.25rem;
        font-weight: 700;
        color: var(--title-color);
        margin-bottom: 0.5rem;
    }

    .carousel-subtitle-underline {
        display: block;
        width: 60px;
        height: 4px;
        background-color: var(--primary-color);
        margin: 0 auto 3.5rem;
        border-radius: 2px;
    }

    .carousel-container {
        width: 450px;
        max-width: 90vw; /* 在小屏幕上防止溢出 */
        height: 280px;
        position: relative;
        perspective: 1000px;
        margin-bottom: 2.5rem;
        user-select: none;
        -webkit-user-select: none;
        cursor: grab;
    }

    .carousel-container:active {
        cursor: grabbing;
    }

    .carousel {
        width: 100%;
        height: 100%;
        position: absolute;
        transform-style: preserve-3d;
        animation: carousel_rotation 30s infinite linear;
        animation-play-state: running;
        
        /* 【优化1】开启GPU加速，性能提升的关键 */
        will-change: transform;
    }

    .carousel-container:hover .carousel {
        animation-play-state: paused;
    }

    @keyframes carousel_rotation {
        from { transform: translateZ(var(--carousel-radius)) rotateY(0); }
        to   { transform: translateZ(var(--carousel-radius)) rotateY(360deg); }
    }

    .carousel__cell {
        display: block;
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        background: black;
        border: 4px solid white;
        border-radius: 10px;
        overflow: hidden;

        /* 【优化3】稍微简化阴影以降低绘制成本 */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);

        /* 【优化1】为每个面板也开启硬件加速 */
        will-change: transform;
        
        /* 提升渲染性能的技巧 */
        /*backface-visibility: hidden;*/
    }

    .carousel__cell img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        pointer-events: none;
        transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .carousel__cell:hover img {
        transform: scale(1.1);
    }



    /* --- 【全新】美化后的控制按钮样式 --- */
    .carousel-controls {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1.5rem; /* 按钮之间的间距 */
    }

    .carousel-controls button {
        /* 1. 基础样式与尺寸 */
        display: flex;
        justify-content: center;
        align-items: center;
        width: 55px;
        height: 55px;
        border-radius: 50%;
        border: none;
        cursor: pointer;
        
        /* 2. 颜色与渐变 (与您的主题色融合) */
        background: linear-gradient(145deg, hsl(229, 98%, 65%), hsl(229, 98%, 55%)); /* 基于 --primary-color 的渐变 */
        color: white; /* 图标颜色 */

        /* 3. 阴影效果，营造悬浮感 */
        box-shadow: 0 4px 15px rgba(74, 108, 253, 0.4), /* 主题色阴影 */
                    0 2px 5px rgba(0, 0, 0, 0.1);       /* 常规阴影 */

        /* 4. 平滑的过渡动画 */
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }

    /* 5. 悬停时的交互反馈 */
    .carousel-controls button:hover {
        transform: translateY(-4px); /* 按钮轻微上浮 */
        background: linear-gradient(145deg, hsl(229, 98%, 70%), hsl(229, 98%, 60%)); /* 渐变色变亮 */
        box-shadow: 0 8px 25px rgba(74, 108, 253, 0.5),
                    0 4px 10px rgba(0, 0, 0, 0.15);
    }

    /* 6. 点击时的交互反馈 */
    .carousel-controls button:active {
        transform: translateY(-1px) scale(0.98); /* 轻微下沉和缩小，模拟按压 */
        box-shadow: 0 2px 8px rgba(74, 108, 253, 0.4);
        transition-duration: 0.1s; /* 点击反馈要快 */
    }

    /* 7. 使用SVG图标替换文字 (关键！) */
    .carousel-controls button::before {
        content: '';
        display: block;
        width: 24px;
        height: 24px;
        background-color: currentColor; /* 使用按钮的 color (白色) 作为图标颜色 */
        /* 使用 mask-image 技术来创建任意形状的图标 */
        -webkit-mask-size: contain;
        mask-size: contain;
        -webkit-mask-repeat: no-repeat;
        mask-repeat: no-repeat;
        -webkit-mask-position: center;
        mask-position: center;
    }

    /* 为“上一个”按钮设置向左的箭头图标 */
    .carousel-controls .carousel-prev-button::before {
        -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z'/%3E%3C/svg%3E");
        mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z'/%3E%3C/svg%3E");
    }

    /* 为“下一个”按钮设置向右的箭头图标 */
    .carousel-controls .carousel-next-button::before {
        -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M8.59 16.59L10 18l6-6-6-6-1.41 1.41L13.17 12z'/%3E%3C/svg%3E");
        mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M8.59 16.59L10 18l6-6-6-6-1.41 1.41L13.17 12z'/%3E%3C/svg%3E");
    }





    .full-width-bleed {
        width: 100vw;
        left: 50%;
        transform: translateX(-50%);
        padding-left: 1rem;
        padding-right: 1rem;
    }



</style>







<br>
<center><font size=6rem color= #757575>
      永远保持谦逊  
<br>

			--gzh </font></center>  

---

<center>
<a href="../龚子航_SLAM算法工程师_简历.pdf" target="_blank" class="md-button">下载简历</a>
</center>  

## 个人简介

<!-- <p style="text-align: center; font-size: 25px; margin: 0px;"><strong>𝘿𝙤𝙣'𝙩 𝙘𝙖𝙧𝙚 𝙖𝙗𝙤𝙪𝙩 𝙬𝙤𝙧𝙡𝙙𝙡𝙮 𝙚𝙮𝙚𝙨 𝙩𝙤 𝙥𝙪𝙧𝙨𝙪𝙚 𝙮𝙤𝙪𝙧 𝙤𝙬𝙣 𝙡𝙞𝙜𝙝𝙩</strong></p> -->

!!! pied-piper1 "About me"
    - [x] Hey, I'm [gzh](https://github.com/Gongzihang6){target=“_blank”}~
        - [x] 偶发的强迫症 
        - [x] 热爱(xiā)折腾技术/数学
        - [x] 读书明志;诗词爱好者;擅长羽毛球
        - [x] 清醒知趣，明得失，知进退 

<div class="carousel-section full-width-bleed" id="life-carousel">
    <h2 class="carousel-title">我的生活</h2>
    <span class="carousel-subtitle-underline"></span>
    <div class="carousel-container">
        <div class="carousel">
            <!-- 替换成您的生活照片 -->
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20250510_170835.jpg" alt="社团活动" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20230915_174751.jpg" alt="旅行风景" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20250417_085601.jpg" alt="团队合影" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2Fwx_camera_1748174958408.jpg" alt="羽毛球" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240809_190138.jpg" alt="个人摄影" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20250320_004737.jpg" alt="志愿者活动" draggable="false"></figure>     
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240808_190022.jpg" alt="8" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240730_192249.jpg" alt="9" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240729_185903.jpg" alt="10" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240320_111630.jpg" alt="11" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240204_124404.jpg" alt="12" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240204_120923.jpg" alt="13" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240204_081247.jpg" alt="14" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240320_111718.jpg" alt="15" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20250119_183726.jpg" alt="16" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20241224_172745.jpg" alt="17" draggable="false"></figure>
            <figure class="carousel__cell"><img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FIMG_20240726_190230.jpg" alt="18" draggable="false"></figure>
        </div>
    </div>
    <div class="carousel-controls">
        <button class="carousel-prev-button">‹</button>
        <button class="carousel-next-button">›</button>
    </div>
</div>


<script>
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
</script>

















<!-- <div class="card2 file-block" markdown="1">
<div class="file-icon"><img src="https://pic4.zhimg.com/80/v2-98f918276ecbc6d549fa6a5d1238e713_1440w.webp" style="height: 3em;"></div>
<div class="file-body">
<div class="file-title">个人简历</div>
<div class="file-meta">2025-02-14</div>
</div>
<a class="down-button" target="_blank" href="../个人简历.pdf" markdown="1">:fontawesome-solid-download: 下载</a>
</div> -->

<hr />
<h2 id="_3">我的履历<a class="headerlink" href="#_3" title="Permanent link">&para;</a></h2>

<p><link rel="stylesheet" href="../sty/portfolio.css"></p>

<!-- 增大字号 -->
<div class="qualification__tabs">
    <div class="qualification__button qualification__active" data-target='#education'>
        <iconify-icon icon="fluent:hat-graduation-12-regular" class="qualification__icon"></iconify-icon>
        来时路
    </div>
</div>
<!-- 放置在您页面的主体部分 -->
<section class="qualification-section">
    <h2 class="section__title">教育背景</h2>
    <span class="section__subtitle-underline"></span>

    <div class="qualification__container">
        
        <!-- 未来规划 (最顶端) -->
        <div class="qualification__data">
            <div></div> 
            <div>
                <span class="qualification__rounder"></span>
                <span class="qualification__line"></span> <!-- 这个会被CSS隐藏 -->
            </div>
            <div class="qualification__content">
                <h3 class="qualification__title">未完待续</h3>
                <span class="qualification__subtitle">于道各努力，千里自同风</span>
                <div class="qualification__calendar">
                    <iconify-icon icon="tabler:calendar-time"></iconify-icon>
                    <span>未来</span>
                </div>
            </div>
        </div>
    
        <!-- 硕士 (中间) -->
        <div class="qualification__data">
            <div class="qualification__content">
                <h3 class="qualification__title">HZAU (华中农业大学)</h3>
                <span class="qualification__subtitle">数学硕士</span>
                <div class="qualification__calendar">
                    <iconify-icon icon="tabler:calendar"></iconify-icon>
                    <span>2024 - 2027 (规划)</span>
                </div>
            </div>
            <div>
                <span class="qualification__rounder"></span>
                <span class="qualification__line"></span> <!-- 这个会被CSS隐藏 -->
            </div>
        </div>
    
        <!-- 学士 (中间) -->
        <div class="qualification__data">
            <div></div>
            <div>
                <span class="qualification__rounder"></span>
                <span class="qualification__line"></span> <!-- 这个会被CSS隐藏 -->
            </div>
            <div class="qualification__content">
                <h3 class="qualification__title">HZAU (华中农业大学)</h3>
                <span class="qualification__subtitle">设施农业科学与工程学士</span>
                <div class="qualification__calendar">
                    <iconify-icon icon="tabler:calendar"></iconify-icon>
                    <span>2020 - 2024</span>
                </div>
            </div>
        </div>
        
        <!-- 高中 (最底端) -->
        <div class="qualification__data">
            <div class="qualification__content">
                <h3 class="qualification__title">汉川一中</h3>
                <span class="qualification__subtitle">平凡普通的三年</span>
                <div class="qualification__calendar">
                    <iconify-icon icon="tabler:calendar"></iconify-icon>
                    <span>2017 - 2020</span>
                </div>
            </div>
            <div>
                <span class="qualification__rounder"></span>
            </div>
        </div>
    
    </div>
</section>




## 人生态度

<p style="text-align: center; font-size: 25px; margin: 0px;">
    <strong>
    "𝘿𝙤𝙣'𝙩 𝙘𝙖𝙧𝙚 𝙖𝙗𝙤𝙪𝙩 𝙬𝙤𝙧𝙡𝙙𝙡𝙮 𝙚𝙮𝙚𝙨 𝙩𝙤 𝙥𝙪𝙧𝙨𝙪𝙚 𝙮𝙤𝙪𝙧 𝙤𝙬𝙣 𝙡𝙞𝙜𝙝𝙩"
    </strong>
    <br>
    <strong>
    “珍惜你的不良嗜好，因为那可能是你热爱生活的主要原因。”
    </strong>
</p>

<!-- <img class="img1" src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/IMG_20250626_101151.webp"> -->
![IMG_20250626_101151](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/IMG_20250626_101151.webp)


<!-- <head>
  <style>
    @media (min-width: 768px) {
      .mobile-only {
        display: none;
      }
    }
  </style>
</head>
<body>
  <a href="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/%E6%88%91%E7%9A%84%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" target="_blank" class="mobile-only">

   <center>
    <img class="img1" src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/%E6%88%91%E7%9A%84%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" style="width: 450px; height: auto;">
      <div style="color:orange; 
      color: #999;
      padding: 2px;">我的Wechat</div>
    </center>  

  </a>  

  <a href="https://t.me/gongzihang" target="_blank" class="mobile-only">
   <center>
    <img class="img1" src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/tg.jpg" style="width: 450px; height: auto;">
      <div style="color:orange; 
      color: #999;
      padding: 2px;">我的TG</div>
    </center>  


  </a>
</body>

<style>
@media (max-width: 768px) { /* 移动端隐藏 */
  .desktop-only {
    display: none !important;
  }
}
</style>

<div class="grid desktop-only" style="display: grid;grid-template-columns: 35% 65%" markdown>
<div class="grid cards" markdown>

-   <center>![WeChat](https://picx.zhimg.com/80/v2-21045fd6f42e98fb136c6d7d0958f2f1_1440w.webp#only-light){ .lg .middle style="width: 50px; height: 50px;"} ![WeChat](https://img.icons8.com/?size=100&id=19977&format=png&color=000000#only-dark){ .lg .middle style="width: 50px; height: 50px;"}</center>

    ---
    
    <center><font  color= #757575 size=6>WeChat</font>  
    <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/%E6%88%91%E7%9A%84%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" style="width: auto; height: auto;">
    <font color= #999 >扫一扫上面的二维码图案<br>
    加我为朋友</font></center>

</div>

<div class="grid cards" style="display: grid; grid-template-columns: 1fr;" markdown>



-   <center>![](https://pic4.zhimg.com/v2-e996df5a7696237b6f924ace7044cd97_1440w.jpg#only-light){ .lg .middle style="width: 50px; height: 50px;"}![](https://img.icons8.com/?size=100&id=3AYCSzCO85Qw&format=png&color=000000#only-dark){ .lg .middle style="width: 50px; height: 50px;"} </center>

    ---

    <center><font  color= #757575 size=6>Email</font>
[发送电子邮件 :fontawesome-solid-paper-plane:](mailto:<zihanggong24@gmail.com>){.md-button}</center>

<div class="grid cards" style="display:grid; grid-template-columns: 49% 49% !important;" markdown>


-   <center>![](https://pica.zhimg.com/v2-61b4731957dba61e9960436dbd06306a_1440w.jpg#only-light){ .lg .middle style="width: 50px; height: 50px;" } ![WeChat](https://img.icons8.com/?size=100&id=63306&format=png&color=000000#only-dark){ .lg .middle style="width: 50px; height: 50px;"}</center>

    ---

    <center><font  color= #757575 size=6>Telegram</font>
    [Let's Chat :fontawesome-brands-telegram:](https://t.me/gongzihang){.md-button} </center>

-   <center>![](https://pic3.zhimg.com/80/v2-aa11d437a377f1a0deac132eb800b306_1440w.webp#only-light){ .lg .middle style="width: 50px; height: 50px;"} ![WeChat](https://img.icons8.com/?size=100&id=13963&format=png&color=000000#only-dark){ .lg .middle style="width: 50px; height: 50px;"}</center>

    ---
    
    <center><font  color= #757575 size=6>Twitter</font>  
    [@Wcowin :material-twitter:](https://twitter.com/ZihangGong28792){.md-button}</center>

</div>
</div>
</div> -->


## 联系我

=== "💬 联系方式 Contact"
    <div class="contact-container">
      <div class="contact-item">
        <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/%E6%88%91%E7%9A%84%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="微信二维码">
        <p>
          <b>💬 微信</b><br>
          扫码加我为朋友
        </p>
      </div>
      <div class="contact-item">
        <!-- 在这里替换成你的QQ二维码图片地址 -->
        <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FQQ%E4%BA%8C%E7%BB%B4%E7%A0%81.jpg" alt="QQ二维码">
        <p>
          <b>🐧 QQ</b><br>
          扫码加我为好友
        </p>
      </div>
    </div>

=== "📧 邮箱"
    <div style="text-align: center; padding: 20px 0px;">
        <div style="font-size: 16px; color: #757575; margin-bottom: 25px;">
            您可以直接复制我的邮箱地址：<br>
            <code style="background-color: #f0f0f0; padding: 4px 8px; border-radius: 6px; font-size: 17px; color: var(--primary-color, #4a6cfd); user-select: all;">zihanggong24@gmail.com</code>
        </div>
        <a href="mailto:zihanggong24@gmail.com?subject=你好，来自你的个人网站" class="md-button md-button--primary" style="font-size: 16px; padding: 12px 30px; border-radius: 25px;">
            :fontawesome-solid-paper-plane:   或点击此处快速发送
        </a>
        <div style="margin-top: 30px;">
            <div style="font-size: 16px; color: #999; margin-top: 5px;">
                💡 24小时内回复，请耐心等待
            </div>
        </div>
    </div>

=== "🌐 社交"
    <div class="contact-tab-container">
        <div class="contact-tab-content" style="text-align: center; padding: 0px 0;">
            <div style="margin-bottom: 25px;">
                <p style="font-size: 16px; color: var(--md-default-fg-color--light); margin-bottom: 20px;">
                    关注我的社交媒体，获取最新动态
                </p>
            </div>
            <!-- 修改按钮布局 - 移动端也保持左右排列 -->
            <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 25px; min-height: 50px; align-items: center;">
                <a href="https://t.me/gongzihang" class="md-button md-button--primary"
                   style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 16px; border-radius: 25px; background: linear-gradient(135deg, #0088cc, #0066aa); color: white; text-decoration: none; font-size: 14px; min-width: 120px; justify-content: center;" target="_blank">
                    :fontawesome-brands-telegram: Telegram
                </a>
                <a href="https://twitter.com/ZihangGong28792_" class="md-button md-button--primary"
                   style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 16px; border-radius: 25px; background: linear-gradient(135deg, #1da1f2, #0d8bd9); color: white; text-decoration: none; font-size: 14px; min-width: 120px; justify-content: center;" target="_blank">
                    :fontawesome-brands-twitter: Twitter
                </a>
            </div>
            <div style="max-width: 500px; margin: 0 auto;">
                <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/tg.jpg" 
                     style="width: 100%; height: auto; border-radius: 10px;">
            </div>
        </div>
    </div>

=== "📍 其他"
    <div style="text-align: center; padding: 0px 0px;">
    <div style="margin-bottom: 30px;">
        <p style="font-size: 15px; color: var(--md-default-fg-color--light);">
        通过下列平台了解我的更多工作和项目经历
        </p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; max-width: 700px; margin: 0 auto;">
        <!-- GitHub -->
        <div style="padding: 20px; border-radius: 16px; background: var(--md-code-bg-color); border: 1px solid var(--md-default-fg-color--lightest); box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: transform 0.3s, box-shadow 0.3s;"
            onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 10px 20px rgba(0,0,0,0.08)'"
            onmouseout="this.style.transform='none'; this.style.boxShadow='0 4px 10px rgba(0,0,0,0.05)'">
        <div style="font-size: 26px; margin-bottom: 12px;">🌟</div>
        <h4 style="margin: 0 0 10px 0; color: var(--md-primary-fg-color); font-size: 17px;">GitHub</h4>
        <a href="https://github.com/Gongzihang6" class="md-button" style="font-size: 14px;" target="_blank">
            :fontawesome-brands-github: 查看 GitHub
        </a>
        </div>
        <!-- LinkedIn -->
        <div style="padding: 20px; border-radius: 16px; background: var(--md-code-bg-color); border: 1px solid var(--md-default-fg-color--lightest); box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: transform 0.3s, box-shadow 0.3s;"
            onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 10px 20px rgba(0,0,0,0.08)'"
            onmouseout="this.style.transform='none'; this.style.boxShadow='0 4px 10px rgba(0,0,0,0.05)'">
        <div style="font-size: 26px; margin-bottom: 12px;">💼</div>
        <h4 style="margin: 0 0 10px 0; color: var(--md-primary-fg-color); font-size: 17px;">LinkedIn</h4>
        <a href="https://www.linkedin.com/in/%E5%AD%90%E8%88%AA-%E9%BE%9A-74a0a1372/" class="md-button" style="font-size: 14px;" target="_blank">
            :fontawesome-brands-linkedin: 查看档案
        </a>
        </div>
    </div>
    <!-- 底部强调卡片 -->
    <div style="margin-top: 40px; padding: 20px; border-radius: 12px; background: linear-gradient(135deg, var(--md-primary-fg-color--light), var(--md-primary-fg-color)); color: white; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
        <p style="margin: 0; font-size: 16px; font-weight: 600;">
        随时欢迎联系我合作或交流！
        </p>
        <p style="margin: 10px 0 0 0; font-size: 14px; opacity: 0.9;">
        无论是技术探讨、学习交流还是职业机会，我都乐意听见你的声音 😄
        </p>
    </div>
    </div>



<script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>

<!-- 放在 .poem-card 的后面 -->
<script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
<script type="text/javascript">
jinrishici.load(function(result) {
    // 这个函数会在成功获取诗词后执行
    var container = document.getElementById("jinrishici-container");
    if (container) {
        // 我们手动将诗词内容填充到指定的 div 中
        container.innerHTML = result.data.content;
    }
});
</script>


<!-- 1. 引入 canvas-confetti 库，我们使用 CDN 保证速度和方便 -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

<!-- 2. 添加触发碎纸屑特效的脚本 -->
<script>
document.addEventListener('DOMContentLoaded', () => {

    // 创建一个 confetti 实例
    const myConfetti = confetti.create(null, {
        resize: true,
        useWorker: true
    });

    // 触发礼花效果
    myConfetti({
        particleCount: 200,     // 粒子数量
        spread: 160,            // 喷射范围 (角度)
        origin: { y: 0.5 },     // 从页面中部喷出
        startVelocity: 40,      // 初始速度
        gravity: 0.8,           // 重力
        ticks: 350,             // 持续时间

        // 我根据您博客的主题色为您挑选了一组和谐的颜色
        colors: ['#4a6cfd', '#a5b4fc', '#ffc700', '#ff5e7e', '#88ff5a'] 
    });
});
</script>




