﻿---
title: 主页
hide:
#   - navigation
#   - toc
  - feedback
#   - footer
status: new
comments: true
---

<link rel="stylesheet" href="stylesheets/profile-common.css">
<link rel="stylesheet" href="stylesheets/home-page.css">

<!--
文件说明：
本页是博客首页，当前版本不再采用单纯的纵向堆叠，而是改为“主视觉 + 侧栏卡片 + 内容马赛克”的高密度栅格化布局。

本页承担的职责：
1. 用更强的视觉层次建立第一印象；
2. 在首屏内压缩展示身份、方向、代表内容与行动入口；
3. 让第一次进入站点的读者可以快速知道“我是谁、我写什么、应该先点哪里”。
-->

<!-- 首页顶部主舞台：左侧是主视觉与行动入口，右侧收纳诗词和作者切片。 -->
<div class="home-stage">
    <section class="home-hero-board">
        <p class="hero-eyebrow">GZH · Algorithm · 3D Vision · Machine Learning</p>
        <h1 class="hero-title">把算法、三维视觉与长期主义，写成一张可阅读的个人名片</h1>
        <p class="hero-lead">
            这里不是一个“很空的欢迎页”，而是我的博客门面、内容入口和长期作品集首页。
            我希望用更紧凑的结构，把算法基础、科研笔记、点云处理、模型理解和个人研究方向压缩到同一张视觉画布里，
            让你第一次进入这里时，就能快速知道我在关注什么、积累什么、最值得先读什么。
        </p>
        <div class="hero-tags">
            <span class="hero-tag">点云处理</span>
            <span class="hero-tag">三维视觉</span>
            <span class="hero-tag">机器学习</span>
            <span class="hero-tag">算法基础</span>
            <span class="hero-tag">科研笔记</span>
            <span class="hero-tag">长期主义</span>
        </div>
        <div class="hero-actions">
            <a href="about/geren.md" class="md-button md-button--primary">进入作者主页</a>
            <a href="about/files/slam-resume.pdf" target="_blank" class="md-button">下载简历</a>
            <a href="blog/index.md" class="md-button">进入博客总览</a>
        </div>
        <div class="hero-metrics">
            <div class="hero-metric">
                <span class="hero-metric__value">3 条主线</span>
                <span class="hero-metric__label">算法、三维视觉、机器学习三条内容主线并行积累。</span>
            </div>
            <div class="hero-metric">
                <span class="hero-metric__value">研究导向</span>
                <span class="hero-metric__label">偏向点云理解、视觉测量、相机模型与科研型问题拆解。</span>
            </div>
            <div class="hero-metric">
                <span class="hero-metric__value">工程表达</span>
                <span class="hero-metric__label">关注从数学直觉、原理推导到工程实现的完整表达链路。</span>
            </div>
            <div class="hero-metric">
                <span class="hero-metric__value">持续建设中</span>
                <span class="hero-metric__label">把博客继续打磨成个人作品集，而不只是零散记录。</span>
            </div>
        </div>
    </section>

    <aside class="home-side-stack">
        <div class="home-panel home-panel--poem">
            <div class="home-panel__label">今日诗词</div>
            <div class="poem-card home-poem-card">
                <div class="poem-seal"></div>
                <div id="jinrishici-container">正在载入今日诗词...</div>
            </div>
        </div>

        <div class="home-panel home-panel--profile">
            <div class="home-panel__label">作者切片</div>
            <div class="flip-container home-profile-flip">
                <div class="image-container">
                    <img src="assets/profile/avatar-front.jpg" alt="GZH 头像正面" width="290" height="290" decoding="async" fetchpriority="high">
                    <img src="assets/profile/avatar-back.jpg" alt="GZH 头像背面" width="290" height="290" decoding="async" loading="lazy">
                </div>
            </div>
            <div class="home-profile-card">
                <h2 class="home-profile-card__title">龚子航</h2>
                <p class="home-profile-card__desc">
                    数学硕士在读，长期关注三维视觉、点云处理、算法工程与机器学习实践。
                    这个博客既是我的学习记录，也是我正在持续打磨的长期作品集。
                </p>
                <div class="home-profile-pills">
                    <span class="home-profile-pill">PCL</span>
                    <span class="home-profile-pill">Python</span>
                    <span class="home-profile-pill">C++</span>
                    <span class="home-profile-pill">Problem Solving</span>
                </div>
                <a class="home-profile-link" href="about/geren.md">查看完整作者主页</a>
            </div>
        </div>
    </aside>
</div>

<!-- 精选阅读四宫格：优先给第一次访问的读者一个最短阅读路径。 -->
<section class="home-section">
    <div class="home-section-head">
        <p class="home-section-kicker">Featured Reading</p>
        <h2 class="home-section-title">第一次来到这里，建议先从这四块开始</h2>
        <p class="home-section-intro">
            这组入口尽量覆盖我当前最能代表博客质量和方向的内容。
            它不是简单的“文章列表”，而是我希望外部读者最快感知我研究兴趣、知识结构和表达方式的一组样本。
        </p>
    </div>

    <div class="home-feature-grid">
        <a class="home-card home-card--research" href="blog/随笔/科研/点云关键点预测.md">
            <span class="home-card__meta">Research / 3D Vision</span>
            <h3 class="home-card__title">点云关键点预测</h3>
            <p class="home-card__desc">
                这是当前最能体现我对三维视觉、点云表达和研究型问题持续关注的一篇内容，适合作为理解我专业方向的第一站。
            </p>
            <span class="home-card__cta">继续阅读</span>
        </a>
        <a class="home-card home-card--engineering" href="blog/随笔/科研/PCL库总结.md">
            <span class="home-card__meta">Point Cloud / Engineering</span>
            <h3 class="home-card__title">PCL 库总结</h3>
            <p class="home-card__desc">
                偏工程实践与工具链整理的一篇代表文章，适合快速了解我在点云处理、库使用和知识沉淀上的风格。
            </p>
            <span class="home-card__cta">继续阅读</span>
        </a>
        <a class="home-card home-card--model" href="blog/MachineLearning/理解YOLO网络结构.md">
            <span class="home-card__meta">Machine Learning</span>
            <h3 class="home-card__title">理解 YOLO 网络结构</h3>
            <p class="home-card__desc">
                如果你更关心我如何拆解复杂模型、讲清楚结构逻辑，这篇文章会比一句“我会深度学习”更有说服力。
            </p>
            <span class="home-card__cta">继续阅读</span>
        </a>
        <a class="home-card home-card--algorithm" href="blog/Computer%20Science/LeetCode热题100/回文链表.md">
            <span class="home-card__meta">Algorithm / LeetCode</span>
            <h3 class="home-card__title">回文链表</h3>
            <p class="home-card__desc">
                这类题解型内容更适合观察我的基础能力、思路拆解方式和“把知识写得可复用”的表达习惯。
            </p>
            <span class="home-card__cta">继续阅读</span>
        </a>
    </div>
</section>

<!-- 内容地图：使用更高密度的马赛克布局，压缩展示阅读路线、当前建设方向和专题矩阵。 -->
<section class="home-section">
    <div class="home-section-head">
        <p class="home-section-kicker">Content Atlas</p>
        <h2 class="home-section-title">如果不想一篇篇翻，可以直接按地图进入</h2>
        <p class="home-section-intro">
            这一块负责把首页从“门面图”真正升级成“内容导航台”。
            你可以按主题、按阅读目标、按想了解我的角度，从不同入口快速进入同一个博客体系。
        </p>
    </div>

    <div class="home-map-grid">
        <div class="home-map-card home-map-card--wide">
            <span class="home-map-card__meta">阅读路线</span>
            <h3 class="home-map-card__title">第一次访问，建议沿着这条路径看</h3>
            <p class="home-map-card__desc">
                如果你是第一次来到这里，不建议直接扎进左侧目录深翻。
                更高效的方式，是先挑与你最相关的方向，再顺着该方向的代表文章与专题入口继续往里走。
            </p>
            <div class="home-route-grid">
                <a class="home-route-tile" href="blog/随笔/科研/点云关键点预测.md">
                    <strong>科研与三维视觉</strong>
                    <span>先看点云关键点预测，再延伸到相机模型、体尺测量和多相机采集。</span>
                </a>
                <a class="home-route-tile" href="blog/随笔/科研/PCL库总结.md">
                    <strong>工程与工具链</strong>
                    <span>从 PCL 库总结切入，更快看到我在工程实践和知识整理上的积累。</span>
                </a>
                <a class="home-route-tile" href="blog/MachineLearning/理解YOLO网络结构.md">
                    <strong>模型理解与算法</strong>
                    <span>先看 YOLO 网络结构，再延伸到 2D 图像深度学习和算法题解体系。</span>
                </a>
            </div>
        </div>

        <div class="home-map-card home-map-card--tall">
            <span class="home-map-card__meta">持续建设中</span>
            <h3 class="home-map-card__title">我现在重点在长期建设什么</h3>
            <p class="home-map-card__desc">
                与其说我在“写博客”，不如说我在持续建设几类能代表自己能力边界与兴趣方向的内容资产。
            </p>
            <div class="home-stack-list">
                <div class="home-stack-item">
                    <strong>算法与题解专题</strong>
                    <p>把刷题从一次性输出，转成可复盘、可迁移的方法型积累。</p>
                </div>
                <div class="home-stack-item">
                    <strong>科研与三维视觉笔记</strong>
                    <p>围绕点云理解、视觉测量、相机模型与真实问题表达持续沉淀。</p>
                </div>
                <div class="home-stack-item">
                    <strong>个人作品集表达</strong>
                    <p>持续优化这个站点本身，让它越来越像真正可对外展示的个人主页。</p>
                </div>
            </div>
        </div>

        <div class="home-map-card home-map-card--full">
            <span class="home-map-card__meta">专题矩阵</span>
            <h3 class="home-map-card__title">三个最稳定、最有延续性的代表专题</h3>
            <p class="home-map-card__desc">
                如果你更喜欢按主题浏览，而不是看单篇入口，可以直接从下面三个专题继续深入。
            </p>
            <div class="topic-grid">
                <div class="topic-card">
                    <span class="home-card__meta">专题一</span>
                    <h3 class="topic-card__title">算法与题解整理</h3>
                    <p class="topic-card__desc">以 LeetCode 热题、数据结构基础和算法思维整理为主，适合快速刷到短平快但有复盘价值的内容。</p>
                    <div class="topic-links">
                        <a href="blog/Computer%20Science/LeetCode热题100/回文链表.md">回文链表</a>
                        <a href="blog/Computer%20Science/LeetCode热题100/找到字符串中所有字母异位词.md">找到字符串中所有字母异位词</a>
                    </div>
                </div>
                <div class="topic-card">
                    <span class="home-card__meta">专题二</span>
                    <h3 class="topic-card__title">科研与三维视觉</h3>
                    <p class="topic-card__desc">围绕点云、关键点预测、PCL 工具链与研究型问题展开，是当前最能体现专业方向的一组内容。</p>
                    <div class="topic-links">
                        <a href="blog/随笔/科研/点云关键点预测.md">点云关键点预测</a>
                        <a href="blog/随笔/科研/体尺测量方案.md">体尺测量方案</a>
                    </div>
                </div>
                <div class="topic-card">
                    <span class="home-card__meta">专题三</span>
                    <h3 class="topic-card__title">机器学习与模型理解</h3>
                    <p class="topic-card__desc">聚焦模型结构、图像任务与深度学习基础理解，适合想看我如何把复杂模型讲清楚的读者。</p>
                    <div class="topic-links">
                        <a href="blog/MachineLearning/理解YOLO网络结构.md">理解 YOLO 网络结构</a>
                        <a href="blog/MachineLearning/2D图像深度学习.md">2D 图像深度学习</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 继续深入：保留最直接的三个行动入口，承接作者页、简历和博客总览。 -->
<section class="home-section">
    <div class="home-section-head">
        <p class="home-section-kicker">Next Step</p>
        <h2 class="home-section-title">想继续了解我，可以从这三条路往下走</h2>
        <p class="home-section-intro">
            首页负责吸引、筛选和导向，不再重复塞满履历与联系方式。
            如果你已经对这个博客有兴趣，下面三个入口足够承接大部分下一步动作。
        </p>
    </div>

    <div class="quick-grid">
        <a class="quick-card" href="about/geren.md">
            <h3>作者个人简介</h3>
            <p>查看更完整的个人介绍、研究方向、履历路径、人生态度与长期建设中的内容资产。</p>
        </a>
        <a class="quick-card" href="about/files/slam-resume.pdf" target="_blank">
            <h3>下载简历</h3>
            <p>如果你更希望快速浏览经历概览、方向边界和技能信息，可以直接进入 PDF 简历版本。</p>
        </a>
        <a class="quick-card" href="blog/index.md">
            <h3>博客总览</h3>
            <p>从博客目录继续展开，按你的兴趣进入 Computer Science、MachineLearning 或随笔栏目。</p>
        </a>
    </div>
</section>

<script src="javascripts/poem-loader.js"></script>
