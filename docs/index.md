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

<!-- 首页保留诗词卡片与头像翻转，用于建立第一印象与页面辨识度。 -->
<div class="poem-card">
    <div class="poem-seal"></div>
    <div id="jinrishici-container">正在载入今日诗词...</div>
</div>

<div class="flip-container">
    <div class="image-container">
        <img src="assets/profile/avatar-front.jpg" alt="GZH 头像正面" width="290" height="290" decoding="async" fetchpriority="high">
        <img src="assets/profile/avatar-back.jpg" alt="GZH 头像背面" width="290" height="290" decoding="async" loading="lazy">
    </div>
</div>

<!-- 首页入口区：快速建立身份定位与行动路径。 -->
<div class="home-hero">
    <p class="hero-eyebrow">GZH · Algorithm · 3D Vision · Machine Learning</p>
    <h2 class="hero-title">把数学直觉、工程实现与长期主义写进博客</h2>
    <p class="hero-lead">
        这里是我的博客主页，重点记录算法、三维视觉、点云处理、机器学习和科研实践中的学习、思考与整理。
        首页负责带你快速看到我最值得读的内容；完整个人经历、履历、态度和联系方式，则统一放在作者个人简介页展示。
    </p>
    <div class="hero-tags">
        <span class="hero-tag">点云处理</span>
        <span class="hero-tag">三维视觉</span>
        <span class="hero-tag">机器学习</span>
        <span class="hero-tag">算法基础</span>
        <span class="hero-tag">长期主义</span>
    </div>
    <div class="hero-actions">
        <a href="about/geren.md" class="md-button md-button--primary">进入个人简介</a>
        <a href="about/files/slam-resume.pdf" target="_blank" class="md-button">下载简历</a>
        <a href="blog/index.md" class="md-button">进入博客总览</a>
    </div>
</div>

## 精选内容

<p class="home-section-intro">
从最能代表当前博客质量和方向的内容开始读，会比从目录里盲翻更高效。
这一组入口优先覆盖算法、科研和机器学习三个方向，适合第一次来到这里的读者快速建立印象。
</p>

<div class="home-grid">
    <a class="home-card" href="blog/随笔/科研/点云关键点预测.md">
        <span class="home-card__meta">Research / 3D Vision</span>
        <h3 class="home-card__title">点云关键点预测</h3>
        <p class="home-card__desc">围绕点云关键点预测问题展开，能够直接体现我对三维视觉、数据表达与科研型内容的持续关注。</p>
        <span class="home-card__cta">继续阅读</span>
    </a>
    <a class="home-card" href="blog/随笔/科研/PCL库总结.md">
        <span class="home-card__meta">Point Cloud / PCL</span>
        <h3 class="home-card__title">PCL 库总结</h3>
        <p class="home-card__desc">从工程视角整理 PCL 常用能力，适合快速了解我在点云处理和三维数据工具链上的知识积累。</p>
        <span class="home-card__cta">继续阅读</span>
    </a>
    <a class="home-card" href="blog/MachineLearning/理解YOLO网络结构.md">
        <span class="home-card__meta">Machine Learning</span>
        <h3 class="home-card__title">理解 YOLO 网络结构</h3>
        <p class="home-card__desc">聚焦目标检测网络的结构理解与拆解，能够体现我对深度学习内容的学习路径和知识表达方式。</p>
        <span class="home-card__cta">继续阅读</span>
    </a>
    <a class="home-card" href="blog/Computer%20Science/LeetCode热题100/回文链表.md">
        <span class="home-card__meta">Algorithm / LeetCode</span>
        <h3 class="home-card__title">回文链表</h3>
        <p class="home-card__desc">从题解型内容切入算法基础，适合快速了解我在数据结构、题解整理和知识复盘方面的输出风格。</p>
        <span class="home-card__cta">继续阅读</span>
    </a>
</div>

## 代表专题

<p class="home-section-intro">
如果你更希望按主题浏览，而不是逐篇挑选，可以直接从下面三个代表专题进入。
每个专题都对应了我当前博客里最稳定、最有延续性的内容方向。
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

## 继续了解我

<p class="home-section-intro">
首页只负责带你快速进入内容，不再重复展示履历、联系方式和完整个人介绍。
如果你想进一步了解我，可以从下面三个入口继续深入。
</p>

<div class="quick-grid">
    <a class="quick-card" href="about/geren.md">
        <h3>作者个人简介</h3>
        <p>查看更完整的个人介绍、履历时间线、人生态度与后续联系入口。</p>
    </a>
    <a class="quick-card" href="about/files/slam-resume.pdf" target="_blank">
        <h3>下载简历</h3>
        <p>如果你更关注经历概览、研究方向和技能信息，可以直接阅读 PDF 简历版本。</p>
    </a>
    <a class="quick-card" href="blog/index.md">
        <h3>博客总览</h3>
        <p>从博客目录继续展开，按你的兴趣进入 Computer Science、MachineLearning 或随笔栏目。</p>
    </a>
</div>

<script src="javascripts/poem-loader.js"></script>
