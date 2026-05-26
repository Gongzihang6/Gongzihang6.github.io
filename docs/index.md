---
title: 关于我
hide:
  - navigation
  - toc
  - feedback
status: new
comments: true
---

<style>
  @import url("https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&display=swap");

  :root {
    --home-bg: #f5f7fb;
    --home-card: rgba(255, 255, 255, 0.9);
    --home-border: rgba(199, 210, 224, 0.7);
    --home-shadow: 0 18px 40px rgba(40, 62, 110, 0.08);
    --home-text: #1f2937;
    --home-muted: #667085;
    --home-primary: #4a6cfd;
    --home-primary-soft: #dbe7ff;
    --home-accent: #7dd3a6;
    --home-radius: 28px;
  }

  .md-content__inner > h1:first-of-type {
    display: none;
  }

  .md-main {
    background:
      radial-gradient(circle at top left, rgba(74, 108, 253, 0.08), transparent 26%),
      radial-gradient(circle at top right, rgba(125, 211, 166, 0.12), transparent 24%),
      linear-gradient(180deg, #f8fbff 0%, #f5f7fb 100%);
  }

  .md-grid {
    max-width: 1500px;
  }

  .md-content {
    max-width: 100%;
  }

  .md-content__inner {
    margin: 0;
    padding-top: 1rem;
  }

  @media (min-width: 1220px) {
    .md-sidebar--primary,
    .md-sidebar--secondary {
      display: none;
    }

    .md-main__inner {
      grid-template-columns: 1fr;
    }
  }

  .home-shell {
    padding: 0.6rem 0 2.8rem;
  }

  .home-shell p,
  .home-shell li,
  .home-shell li p {
    text-indent: 0 !important;
  }

  .hero-layout {
    display: grid;
    grid-template-columns: minmax(360px, 0.92fr) minmax(480px, 1.18fr);
    gap: 1.35rem;
    align-items: start;
  }

  .surface-card {
    position: relative;
    overflow: hidden;
    border: 1px solid var(--home-border);
    border-radius: var(--home-radius);
    background: var(--home-card);
    box-shadow: var(--home-shadow);
    backdrop-filter: blur(12px);
  }

  .surface-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
      linear-gradient(140deg, rgba(255, 255, 255, 0.78), rgba(255, 255, 255, 0.5) 36%, rgba(237, 243, 255, 0.35));
    pointer-events: none;
  }

  .profile-panel,
  .github-card,
  .reading-card,
  .contact-board {
    position: relative;
    z-index: 0;
  }

  .profile-panel > *,
  .github-card > *,
  .reading-card > *,
  .contact-board > * {
    position: relative;
    z-index: 1;
  }

  .profile-panel {
    padding: 1.45rem;
  }

  .profile-top {
    display: grid;
    grid-template-columns: 180px 1fr;
    gap: 1.15rem;
    align-items: start;
  }

  .avatar-glow {
    position: relative;
    width: 180px;
    height: 180px;
    margin: 0;
  }

  .avatar-glow::before {
    content: "";
    position: absolute;
    inset: -12px;
    border-radius: 50%;
    background: conic-gradient(from 120deg, rgba(74, 108, 253, 0.12), rgba(125, 211, 166, 0.48), rgba(92, 138, 255, 0.3), rgba(74, 108, 253, 0.12));
    filter: blur(12px);
    opacity: 0.95;
  }

  .flip-container {
    width: 180px;
    height: 180px;
    perspective: 1200px;
  }

  .image-container {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .image-container img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    border: 4px solid rgba(255, 255, 255, 0.96);
    box-shadow: 0 18px 36px rgba(15, 23, 42, 0.14);
    backface-visibility: hidden;
    transition: transform 0.65s ease;
  }

  .image-container img:last-child {
    transform: rotateY(180deg);
  }

  .image-container:hover img:first-child {
    transform: rotateY(180deg);
  }

  .image-container:hover img:last-child {
    transform: rotateY(0deg);
  }

  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.34rem 0.8rem;
    border-radius: 999px;
    background: rgba(74, 108, 253, 0.08);
    color: var(--home-primary);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
  }

  .intro-copy h1 {
    margin: 0.85rem 0 0.45rem;
    font-size: clamp(2rem, 4vw, 2.8rem);
    line-height: 1.05;
    color: var(--home-text);
  }

  .lead {
    margin: 0 0 0.9rem;
    color: var(--home-muted);
    font-size: 1rem;
    line-height: 1.85;
  }

  .tag-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin-bottom: 1rem;
  }

  .tag-cloud span,
  .pill {
    display: inline-flex;
    align-items: center;
    min-height: 34px;
    padding: 0.42rem 0.85rem;
    border-radius: 999px;
    border: 1px solid rgba(74, 108, 253, 0.12);
    background: rgba(255, 255, 255, 0.72);
    color: #41506a;
    font-size: 0.87rem;
  }

  .hero-actions,
  .contact-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
  }

  .home-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    padding: 0.72rem 1.1rem;
    border-radius: 14px;
    border: 1px solid rgba(74, 108, 253, 0.16);
    background: rgba(255, 255, 255, 0.9);
    color: var(--home-text);
    font-weight: 700;
    text-decoration: none;
    transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  }

  .home-btn:hover {
    transform: translateY(-2px);
    border-color: rgba(74, 108, 253, 0.28);
    box-shadow: 0 12px 24px rgba(74, 108, 253, 0.12);
  }

  .home-btn--primary {
    background: linear-gradient(135deg, #4a6cfd 0%, #6e8cff 100%);
    color: #fff;
    box-shadow: 0 12px 26px rgba(74, 108, 253, 0.22);
  }

  .poem-card {
    margin-top: 1.2rem;
    padding: 1rem 1.15rem 1.05rem;
    border-radius: 22px;
    border: 1px solid rgba(74, 108, 253, 0.1);
    background:
      linear-gradient(0deg, rgba(255, 255, 255, 0.82), rgba(255, 255, 255, 0.82)),
      url("https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2Fssyjt.jpg") center/cover no-repeat;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65);
  }

  .poem-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
  }

  .poem-label {
    color: var(--home-primary);
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
  }

  .poem-seal {
    width: 34px;
    height: 34px;
    border-radius: 8px;
    background: #c93c3c;
    box-shadow: 0 8px 18px rgba(201, 60, 60, 0.22);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 auto;
  }

  .poem-seal::after {
    content: "雅";
    color: #fff;
    font-size: 1rem;
    font-family: "Zhi Mang Xing", "Noto Serif SC", serif;
  }

  #jinrishici-container {
    font-family: "Zhi Mang Xing", "Noto Serif SC", serif;
    color: #374151;
    font-size: 1.25rem;
    line-height: 1.75;
  }

  .bio-card {
    margin-top: 1rem;
    padding: 1.05rem 1.1rem;
    border-radius: 22px;
    background: rgba(247, 250, 255, 0.78);
    border: 1px solid rgba(148, 163, 184, 0.14);
  }

  .section-kicker {
    margin-bottom: 0.55rem;
    color: #3f4d66;
    font-size: 0.88rem;
    font-weight: 700;
    letter-spacing: 0.02em;
  }

  .bio-card p {
    margin: 0;
    color: var(--home-muted);
    line-height: 1.9;
  }

  .bio-card p + p {
    margin-top: 0.55rem;
  }

  .contact-pills {
    margin-top: 1rem;
  }

  .contact-pills a {
    text-decoration: none;
  }

  .dashboard-panel {
    display: grid;
    gap: 1.1rem;
  }

  .github-card {
    padding: 1.4rem;
  }

  .card-head {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    align-items: flex-start;
    margin-bottom: 1rem;
  }

  .card-head h2,
  .reading-card h3,
  .contact-board h2 {
    margin: 0;
    color: var(--home-text);
    line-height: 1.2;
  }

  .card-head p,
  .card-subtitle,
  .reading-card p,
  .contact-card p {
    margin: 0.3rem 0 0;
    color: var(--home-muted);
    line-height: 1.75;
  }

  .contrib-legend {
    display: flex;
    align-items: center;
    gap: 0.35rem;
    color: #7b8799;
    font-size: 0.78rem;
    white-space: nowrap;
  }

  .contrib-legend span {
    width: 13px;
    height: 13px;
    border-radius: 4px;
    display: inline-block;
  }

  .contrib-legend span:nth-child(2) { background: #eef7ef; }
  .contrib-legend span:nth-child(3) { background: #d7f0dc; }
  .contrib-legend span:nth-child(4) { background: #b5e4c0; }
  .contrib-legend span:nth-child(5) { background: #82cf95; }
  .contrib-legend span:nth-child(6) { background: #3eaa57; }

  .github-chart {
    display: block;
    width: 100%;
    padding: 0.85rem;
    border-radius: 22px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(243, 247, 252, 0.96));
    border: 1px solid rgba(148, 163, 184, 0.12);
    box-sizing: border-box;
  }

  .github-chart img {
    display: block;
    width: 100%;
    border-radius: 14px;
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.1rem;
  }

  .reading-card {
    padding: 1.25rem 1.2rem 1.15rem;
  }

  .reading-list {
    margin: 0.95rem 0 0;
    padding: 0;
    list-style: none;
  }

  .reading-list li + li {
    margin-top: 0.85rem;
  }

  .reading-list a {
    color: #2f5fb3;
    text-decoration: none;
    line-height: 1.65;
    font-size: 0.97rem;
  }

  .reading-list a:hover {
    color: var(--home-primary);
  }

  .reading-list small {
    display: block;
    margin-top: 0.18rem;
    color: #8591a3;
    font-size: 0.8rem;
  }

  .contact-board {
    margin-top: 1.2rem;
    padding: 1.3rem;
  }

  .contact-grid {
    margin-top: 1rem;
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1rem;
  }

  .contact-card {
    padding: 1rem;
    border-radius: 22px;
    background: rgba(250, 252, 255, 0.86);
    border: 1px solid rgba(148, 163, 184, 0.15);
  }

  .contact-card img {
    display: block;
    width: 100%;
    max-width: 180px;
    margin: 0 auto 0.85rem;
    border-radius: 16px;
    border: 4px solid rgba(255, 255, 255, 0.95);
    box-shadow: 0 10px 22px rgba(15, 23, 42, 0.1);
  }

  .contact-card h3 {
    margin: 0;
    color: var(--home-text);
    font-size: 1rem;
  }

  .contact-card .home-btn {
    margin-top: 0.8rem;
    width: 100%;
  }

  .social-links {
    display: grid;
    gap: 0.7rem;
    margin-top: 0.85rem;
  }

  .social-links a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 40px;
    border-radius: 14px;
    text-decoration: none;
    color: #fff;
    font-weight: 700;
  }

  .social-links a:nth-child(1) { background: linear-gradient(135deg, #111827, #394150); }
  .social-links a:nth-child(2) { background: linear-gradient(135deg, #0088cc, #0069a6); }
  .social-links a:nth-child(3) { background: linear-gradient(135deg, #1d9bf0, #0c7abf); }
  .social-links a:nth-child(4) { background: linear-gradient(135deg, #0a66c2, #084f96); }

  .density-note {
    margin-top: 1rem;
    padding: 0.95rem 1rem;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(74, 108, 253, 0.08), rgba(125, 211, 166, 0.12));
    color: #44536b;
    line-height: 1.8;
  }

  @media (max-width: 1220px) {
    .hero-layout {
      grid-template-columns: 1fr;
    }

    .dashboard-grid,
    .contact-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 860px) {
    .profile-top {
      grid-template-columns: 1fr;
      justify-items: center;
      text-align: center;
    }

    .intro-copy {
      width: 100%;
    }

    .tag-cloud,
    .hero-actions,
    .contact-pills {
      justify-content: center;
    }

    .card-head {
      flex-direction: column;
    }
  }

  @media (max-width: 720px) {
    .home-shell {
      padding-top: 0.25rem;
    }

    .profile-panel,
    .github-card,
    .reading-card,
    .contact-board {
      border-radius: 24px;
    }

    .dashboard-grid,
    .contact-grid {
      grid-template-columns: 1fr;
    }

    .profile-panel,
    .github-card,
    .reading-card,
    .contact-board {
      padding-left: 1rem;
      padding-right: 1rem;
    }

    .avatar-glow,
    .flip-container {
      width: 150px;
      height: 150px;
    }

    .intro-copy h1 {
      font-size: 2rem;
    }

    #jinrishici-container {
      font-size: 1.08rem;
    }
  }
</style>

<div class="home-shell">
  <section class="hero-layout">
    <div class="profile-panel surface-card">
      <div class="profile-top">
        <div class="avatar-glow">
          <div class="flip-container">
            <div class="image-container">
              <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/gzh.jpg" alt="gzh avatar front">
              <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/3f58b6cea54d446e22107fde739e843.jpg" alt="gzh avatar back">
            </div>
          </div>
        </div>

        <div class="intro-copy">
          <span class="eyebrow">GZH · Research / Code / Writing</span>
          <h1>子航 / gzh</h1>
          <p class="lead">
            专注计算机视觉、三维感知与工程实现，持续记录技术学习、科研笔记和折腾过程。
            这个首页现在改成“打开就能读到重点”的结构：先看我是谁，再看我在写什么、做什么。
          </p>

          <div class="tag-cloud">
            <span>计算机视觉</span>
            <span>3D 感知</span>
            <span>科研笔记</span>
            <span>工程复盘</span>
            <span>诗词与阅读</span>
          </div>

          <div class="hero-actions">
            <a class="home-btn home-btn--primary" href="https://github.com/Gongzihang6" target="_blank" rel="noopener">访问 GitHub</a>
            <a class="home-btn" href="about/files/slam-resume.pdf" target="_blank" rel="noopener">下载简历</a>
          </div>
        </div>
      </div>

      <div class="poem-card">
        <div class="poem-meta">
          <span class="poem-label">DAILY POEM</span>
          <span class="poem-seal"></span>
        </div>
        <div id="jinrishici-container">正在载入今日诗词...</div>
      </div>

      <div class="bio-card">
        <div class="section-kicker">个人简介</div>
        <p>偶发强迫症，长期热衷于技术、数学与把东西真正做出来这件事。偏爱能反复打磨的工作，也愿意把学习过程整理成别人能直接使用的文字。</p>
        <p>这里会持续沉淀视觉感知、算法理解、工具实践，以及一些不那么功利但能长期滋养人的内容。</p>
      </div>

      <div class="contact-pills">
        <a class="pill" href="mailto:zihanggong24@gmail.com">Email</a>
        <a class="pill" href="https://t.me/gongzihang" target="_blank" rel="noopener">Telegram</a>
        <a class="pill" href="https://twitter.com/ZihangGong28792_" target="_blank" rel="noopener">Twitter</a>
        <a class="pill" href="https://www.linkedin.com/in/%E5%AD%90%E8%88%AA-%E9%BE%9A-74a0a1372/" target="_blank" rel="noopener">LinkedIn</a>
      </div>
    </div>

    <div class="dashboard-panel">
      <div class="github-card surface-card">
        <div class="card-head">
          <div>
            <h2>GitHub 贡献图</h2>
            <p>用贡献热力图把最近一年的活跃度直接放到首屏，信息量比单独的个人介绍更高。</p>
          </div>
          <div class="contrib-legend">
            <em>少</em>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <em>多</em>
          </div>
        </div>

        <a class="github-chart" href="https://github.com/Gongzihang6" target="_blank" rel="noopener">
          <img src="https://ghchart.rshah.org/4a6cfd/Gongzihang6" alt="GitHub contribution chart for Gongzihang6">
        </a>

        <div class="density-note">
          打开首页先看到身份、方向、活跃度和推荐内容，比原来“头像 + 大块留白 + 长滚动”更像一个真正的个人门户。
        </div>
      </div>

      <div class="dashboard-grid">
        <div class="reading-card surface-card">
          <h3>推荐文章</h3>
          <p>优先放适合第一次访问时快速理解你能力边界与输出风格的内容。</p>
          <ul class="reading-list">
            <li>
              <a href="./blog/随笔/科研/摄像机成像模型/">摄像机成像模型</a>
              <small>科研基础与视觉几何入门</small>
            </li>
            <li>
              <a href="./blog/随笔/科研/求解两个坐标系的相对旋转和平移矩阵/">两个坐标系的相对旋转和平移矩阵</a>
              <small>偏工程与数学推导</small>
            </li>
            <li>
              <a href="./blog/随笔/Transformer/">Transformer</a>
              <small>模型结构理解与整理</small>
            </li>
            <li>
              <a href="./blog/随笔/Py-Markdown/">Py-Markdown</a>
              <small>写作与博客工具链实践</small>
            </li>
            <li>
              <a href="./blog/随笔/mermaid绘图语法总结/">Mermaid 绘图语法总结</a>
              <small>高实用性的知识整理</small>
            </li>
          </ul>
        </div>

        <div class="reading-card surface-card">
          <h3>继续阅读</h3>
          <p>把不同方向的代表性内容并排放出来，避免首页只停留在“自我介绍”。</p>
          <ul class="reading-list">
            <li>
              <a href="./blog/MachineLearning/经典卷积神经网络/">经典卷积神经网络</a>
              <small>深度学习基础梳理</small>
            </li>
            <li>
              <a href="./blog/MachineLearning/理解YOLO网络结构/">理解 YOLO 网络结构</a>
              <small>目标检测方向笔记</small>
            </li>
            <li>
              <a href="./blog/MachineLearning/支持向量机SVM/">支持向量机 SVM</a>
              <small>传统机器学习方法</small>
            </li>
            <li>
              <a href="./blog/随笔/latex入门学习/">LaTeX 入门学习</a>
              <small>科研写作与排版</small>
            </li>
            <li>
              <a href="./blog/随笔/Matlab基础速成/">Matlab 基础速成</a>
              <small>工具型教程内容</small>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="contact-board surface-card">
    <h2>联系我</h2>
    <p class="card-subtitle">保留联系入口，但改成更紧凑的面板。需要交流技术、项目合作或学习问题，都可以直接联系。</p>

    <div class="contact-grid">
      <div class="contact-card">
        <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/%E6%88%91%E7%9A%84%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="WeChat QR code">
        <h3>微信</h3>
        <p>扫码即可添加，适合日常交流。</p>
      </div>

      <div class="contact-card">
        <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2FQQ%E4%BA%8C%E7%BB%B4%E7%A0%81.jpg" alt="QQ QR code">
        <h3>QQ</h3>
        <p>如果你更习惯 QQ，也可以直接扫码。</p>
      </div>

      <div class="contact-card">
        <h3>Email</h3>
        <p>适合正式沟通、项目合作和较长的问题描述。</p>
        <a class="home-btn home-btn--primary" href="mailto:zihanggong24@gmail.com?subject=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%9D%A5%E8%87%AA%E4%BD%A0%E7%9A%84%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99" rel="noopener">发送邮件</a>
        <p style="margin-top:0.8rem;"><code style="user-select:all;">zihanggong24@gmail.com</code></p>
      </div>

      <div class="contact-card">
        <h3>社交账号</h3>
        <p>更适合看动态、项目和持续输出。</p>
        <div class="social-links">
          <a href="https://github.com/Gongzihang6" target="_blank" rel="noopener">GitHub</a>
          <a href="https://t.me/gongzihang" target="_blank" rel="noopener">Telegram</a>
          <a href="https://twitter.com/ZihangGong28792_" target="_blank" rel="noopener">Twitter</a>
          <a href="https://www.linkedin.com/in/%E5%AD%90%E8%88%AA-%E9%BE%9A-74a0a1372/" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>
    </div>
  </section>
</div>

<script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
<script>
  jinrishici.load(function(result) {
    var container = document.getElementById("jinrishici-container");
    if (container && result && result.data) {
      container.textContent = result.data.content;
    }
  });
</script>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    var myConfetti = confetti.create(null, {
      resize: true,
      useWorker: true
    });

    myConfetti({
      particleCount: 200,
      spread: 160,
      origin: { y: 0.5 },
      startVelocity: 40,
      gravity: 0.8,
      ticks: 350,
      colors: ["#4a6cfd", "#a5b4fc", "#ffc700", "#ff5e7e", "#88ff5a"]
    });
  });
</script>
