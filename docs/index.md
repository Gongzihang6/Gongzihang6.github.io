---
title: gzh
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
    --home-page-width: min(85vw, 1380px);
    --home-text: #1f2937;
    --home-muted: #667085;
    --home-primary: #4a6cfd;
    --home-primary-deep: #2f5fb3;
    --home-line: rgba(193, 207, 229, 0.78);
    --home-card: rgba(255, 255, 255, 0.92);
    --home-shadow: 0 18px 40px rgba(44, 72, 126, 0.08);
    --home-shadow-hover: 0 26px 50px rgba(44, 72, 126, 0.14);
    --home-radius: 28px;
    --glow-a: rgba(74, 108, 253, 0.4);
    --glow-b: rgba(107, 182, 255, 0.4);
    --glow-c: rgba(125, 211, 166, 0.45);
  }

  .md-main {
    background:
      radial-gradient(circle at top left, rgba(74, 108, 253, 0.08), transparent 24%),
      radial-gradient(circle at top right, rgba(125, 211, 166, 0.12), transparent 22%),
      linear-gradient(180deg, #f8fbff 0%, #f4f7fb 100%);
  }

  .md-grid {
    max-width: var(--home-page-width);
  }

  .md-content {
    max-width: 100%;
  }

  .md-content__inner {
    margin: 0;
    padding-top: 0.15rem;
  }

  .md-content__inner > h1:first-of-type {
    display: none;
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
    width: 100%;
    padding: 0.15rem 0 2rem;
    animation: home-fade-in 0.8s ease both;
  }

  .home-shell p,
  .home-shell li,
  .home-shell li p {
    text-indent: 0 !important;
  }

  .surface-card {
    position: relative;
    overflow: hidden;
    border-radius: var(--home-radius);
    border: 1px solid var(--home-line);
    background:
      linear-gradient(150deg, rgba(255, 255, 255, 0.96), rgba(251, 253, 255, 0.88) 42%, rgba(243, 248, 255, 0.9));
    box-shadow: var(--home-shadow);
    backdrop-filter: blur(16px);
    transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  }

  .surface-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
      radial-gradient(circle at top right, rgba(74, 108, 253, 0.08), transparent 24%),
      radial-gradient(circle at bottom left, rgba(125, 211, 166, 0.08), transparent 24%);
    pointer-events: none;
  }

  .surface-card:hover {
    transform: translateY(-4px);
    border-color: rgba(142, 169, 214, 0.95);
    box-shadow: var(--home-shadow-hover);
  }

  .surface-card > * {
    position: relative;
    z-index: 1;
  }

  .hero-layout {
    display: grid;
    grid-template-columns: minmax(360px, 0.92fr) minmax(440px, 1.08fr);
    gap: 1.1rem;
    align-items: start;
  }

  .profile-panel {
    padding: 1.1rem 1.15rem 1.2rem;
  }

  .profile-stack {
    display: grid;
    justify-items: start;
    gap: 0.95rem;
  }

  .top-row {
    display: grid;
    grid-template-columns: 172px minmax(0, 1fr);
    gap: 1rem;
    align-items: center;
    width: 100%;
  }

  .avatar-glow {
    position: relative;
    width: 172px;
    height: 172px;
    margin: 0 auto;
    animation: float-avatar 5.8s ease-in-out infinite;
  }

  .avatar-glow::before,
  .avatar-glow::after {
    content: "";
    position: absolute;
    inset: -14px;
    border-radius: 50%;
    filter: blur(15px);
    opacity: 0.82;
    animation: glow-shift 7.5s linear infinite;
  }

  .avatar-glow::before {
    background: conic-gradient(from 0deg, var(--glow-a), var(--glow-b), var(--glow-c), rgba(255, 191, 113, 0.34), var(--glow-a));
  }

  .avatar-glow::after {
    inset: -8px;
    opacity: 0.55;
    filter: blur(22px);
    animation-duration: 10.5s;
    animation-direction: reverse;
    background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.55), transparent 36%),
      conic-gradient(from 180deg, rgba(125, 211, 166, 0.3), rgba(74, 108, 253, 0.3), rgba(255, 170, 142, 0.22), rgba(125, 211, 166, 0.3));
  }

  .flip-container {
    width: 172px;
    height: 172px;
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
    border: 4px solid rgba(255, 255, 255, 0.98);
    box-shadow: 0 18px 36px rgba(15, 23, 42, 0.14);
    backface-visibility: hidden;
    transition: transform 0.7s ease;
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

  .intro-copy {
    width: 100%;
  }

  .eyebrow {
    display: inline-flex;
    align-items: center;
    min-height: 30px;
    padding: 0.3rem 0.78rem;
    border-radius: 999px;
    background: rgba(74, 108, 253, 0.08);
    color: var(--home-primary);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.05em;
  }

  .intro-copy h1 {
    margin: 0.15rem 0 0.35rem;
    color: var(--home-text);
    font-size: clamp(2.3rem, 5vw, 3.3rem);
    line-height: 1.04;
  }

  .lead {
    margin: 0;
    max-width: 36rem;
    color: #5f718f;
    font-size: 1.02rem;
    line-height: 1.9;
  }

  .tag-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin-top: 0.15rem;
  }

  .tag-cloud span {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 38px;
    padding: 0.52rem 0.98rem;
    border-radius: 999px;
    border: 1px solid rgba(170, 190, 220, 0.85);
    color: #334155;
    font-size: 0.9rem;
    background: linear-gradient(135deg, rgba(239, 245, 255, 0.92), rgba(247, 251, 255, 0.96));
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease, color 0.25s ease;
  }

  .tag-cloud span:nth-child(1) { background: linear-gradient(135deg, #eef4ff, #f5f9ff); }
  .tag-cloud span:nth-child(2) { background: linear-gradient(135deg, #eef8f6, #f6fcfb); }
  .tag-cloud span:nth-child(3) { background: linear-gradient(135deg, #f6f3ff, #fbf9ff); }
  .tag-cloud span:nth-child(4) { background: linear-gradient(135deg, #fff5ec, #fffaf5); }
  .tag-cloud span:nth-child(5) { background: linear-gradient(135deg, #f7f5ef, #fcfbf7); }

  .tag-cloud span:hover {
    transform: translateY(-3px);
    color: var(--home-primary-deep);
    border-color: rgba(116, 153, 231, 0.95);
    box-shadow: 0 14px 28px rgba(74, 108, 253, 0.1);
  }

  .hero-actions,
  .contact-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .contact-pills {
    display: none;
  }

  .hero-actions {
    margin-top: 0.05rem;
  }

  .contact-pills {
    display: none;
  }

  .home-btn,
  .pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    padding: 0.72rem 1.12rem;
    border-radius: 14px;
    border: 1px solid rgba(156, 177, 218, 0.8);
    background: rgba(255, 255, 255, 0.88);
    color: var(--home-text);
    font-weight: 700;
    text-decoration: none;
    transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  }

  .home-btn:hover,
  .pill:hover {
    transform: translateY(-2px);
    border-color: rgba(91, 131, 217, 0.95);
    box-shadow: 0 14px 26px rgba(74, 108, 253, 0.12);
  }

  .home-btn--primary {
    background: linear-gradient(135deg, #4a6cfd 0%, #6f93ff 100%);
    color: #fff;
    box-shadow: 0 12px 26px rgba(74, 108, 253, 0.22);
  }

  .poem-card {
    width: 100%;
    padding: 1.12rem 1.15rem 0.98rem;
    border-radius: 24px;
    border: 1px solid rgba(199, 209, 228, 0.85);
    background:
      linear-gradient(0deg, rgba(255, 255, 255, 0.34), rgba(255, 255, 255, 0.22)),
      url("https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/medias%2F2025%2F06%2Fssyjt.jpg") center/cover no-repeat;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8);
  }

  .poem-meta {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 0.2rem;
  }

  .poem-seal {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, #de4b4b, #b72929);
    box-shadow: 0 10px 20px rgba(201, 60, 60, 0.22);
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }

  .poem-seal::after {
    content: "雅";
    color: #fff;
    font-size: 1rem;
    font-family: "Zhi Mang Xing", "Noto Serif SC", serif;
  }

  #jinrishici-container {
    font-family: "Zhi Mang Xing", "Noto Serif SC", serif;
    color: #283449;
    font-size: 1.45rem;
    line-height: 1.85;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.78);
  }

  .bio-card {
    width: 100%;
    padding: 1rem 1.05rem;
    border-radius: 22px;
    border: 1px solid rgba(206, 214, 229, 0.78);
    background: rgba(247, 250, 255, 0.74);
  }

  .section-kicker {
    margin-bottom: 0.45rem;
    color: #3f4d66;
    font-size: 0.88rem;
    font-weight: 700;
    letter-spacing: 0.02em;
  }

  .bio-card p {
    margin: 0;
    color: #5f718f;
    line-height: 1.9;
  }

  .bio-card p + p {
    margin-top: 0.5rem;
  }

  .dashboard-panel {
    display: grid;
    gap: 1rem;
  }

  .github-card {
    padding: 1.15rem 1.2rem 1.05rem;
  }

  .card-head {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    align-items: flex-start;
    margin-bottom: 0.85rem;
  }

  .card-head h2,
  .reading-card h3,
  .contact-board h2 {
    margin: 0;
    color: var(--home-text);
    line-height: 1.2;
  }

  .github-title {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 0.7rem;
  }

  .github-title strong {
    font-size: clamp(2rem, 3.2vw, 2.4rem);
    font-weight: 700;
    letter-spacing: -0.02em;
  }

  .github-summary {
    color: #7d889a;
    font-size: 0.98rem;
  }

  .github-summary b {
    color: #62bf7a;
    font-weight: 800;
  }

  .contrib-legend {
    display: flex;
    align-items: center;
    gap: 0.38rem;
    color: #7b8799;
    font-size: 0.82rem;
    white-space: nowrap;
  }

  .contrib-legend span {
    width: 14px;
    height: 14px;
    border-radius: 4px;
    display: inline-block;
  }

  .contrib-legend span:nth-child(2) { background: #eef7ef; }
  .contrib-legend span:nth-child(3) { background: #dff1e3; }
  .contrib-legend span:nth-child(4) { background: #c6e8ce; }
  .contrib-legend span:nth-child(5) { background: #8ed39d; }
  .contrib-legend span:nth-child(6) { background: #4fb866; }

  .github-chart-wrap {
    position: relative;
    padding: 0.9rem 0.9rem 0.72rem;
    border-radius: 24px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.94), rgba(242, 247, 252, 0.95));
    border: 1px solid rgba(201, 211, 227, 0.85);
    overflow: hidden;
  }

  .github-chart {
    width: 100%;
    min-height: 190px;
    overflow: hidden;
  }

  .github-calendar-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 0.4rem;
  }

  .github-calendar {
    display: grid;
    grid-template-columns: 28px 1fr;
    gap: 8px;
    align-items: start;
  }

  .github-months {
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: 1fr;
    color: #8a94a6;
    font-size: 0.76rem;
  }

  .github-weekdays {
    display: grid;
    grid-template-rows: repeat(7, 14px);
    gap: 4px;
    color: #8a94a6;
    font-size: 0.72rem;
    text-align: right;
    padding-top: 18px;
  }

  .github-grid {
    display: grid;
    grid-template-columns: repeat(53, 12px);
    grid-template-rows: repeat(7, 12px);
    gap: 3px;
    overflow-x: hidden;
    padding: 2px 2px 2px 0;
    align-content: start;
    justify-content: start;
  }

  .contrib-cell {
    width: 12px;
    height: 12px;
    border-radius: 4px;
    background: #eef7ef;
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.95);
    transition: transform 0.16s ease, box-shadow 0.16s ease, outline-color 0.16s ease;
  }

  .contrib-cell.is-zero { background: #eef7ef; }
  .contrib-cell.is-l1 { background: #dff1e3; }
  .contrib-cell.is-l2 { background: #c6e8ce; }
  .contrib-cell.is-l3 { background: #8ed39d; }
  .contrib-cell.is-l4 { background: #4fb866; }

  .contrib-cell:hover {
    transform: scale(1.15);
    box-shadow: 0 0 0 2px rgba(74, 108, 253, 0.22);
    outline: 1px solid rgba(74, 108, 253, 0.2);
    z-index: 2;
  }

  .month-row {
    width: 100%;
    height: auto;
  }

  .github-tooltip {
    position: absolute;
    z-index: 10;
    min-width: 168px;
    max-width: 240px;
    padding: 0.7rem 0.9rem;
    border-radius: 14px;
    background: rgba(30, 31, 35, 0.92);
    color: #fff;
    font-size: 0.92rem;
    line-height: 1.45;
    pointer-events: none;
    opacity: 0;
    transform: translate(-50%, calc(-100% - 14px)) scale(0.96);
    transform-origin: bottom center;
    transition: opacity 0.18s ease, transform 0.18s ease;
    box-shadow: 0 18px 36px rgba(15, 23, 42, 0.24);
  }

  .github-tooltip::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: -7px;
    width: 14px;
    height: 14px;
    background: rgba(30, 31, 35, 0.92);
    transform: translateX(-50%) rotate(45deg);
  }

  .github-tooltip.is-visible {
    opacity: 1;
    transform: translate(-50%, calc(-100% - 18px)) scale(1);
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    align-items: stretch;
  }

  .reading-card {
    display: flex;
    flex-direction: column;
    min-height: 100%;
    padding: 1.15rem 1.15rem 1rem;
  }

  .reading-card::after {
    content: "";
    position: absolute;
    inset: auto 1.15rem 0.9rem 1.15rem;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(112, 146, 219, 0.3), transparent);
    pointer-events: none;
  }

  .reading-card h3 {
    font-size: 1.42rem;
  }

  .reading-list {
    margin: 0.75rem 0 0;
    padding: 0;
    list-style: none;
  }

  .reading-list li {
    position: relative;
    padding: 0.9rem 0 0.9rem 0.82rem;
    border-bottom: 1px dashed rgba(186, 199, 221, 0.6);
    transition: transform 0.25s ease, padding-left 0.25s ease;
  }

  .reading-list li:last-child {
    border-bottom: 0;
    padding-bottom: 0.3rem;
  }

  .reading-list li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 1.45rem;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4a6cfd, #78b1ff);
    box-shadow: 0 0 0 6px rgba(74, 108, 253, 0.08);
  }

  .reading-list li:hover {
    transform: translateX(6px);
    padding-left: 0.96rem;
  }

  .reading-list a {
    color: var(--home-primary-deep);
    text-decoration: none;
    line-height: 1.6;
    font-size: 1.02rem;
    transition: color 0.25s ease;
  }

  .reading-list a:hover {
    color: var(--home-primary);
  }

  .reading-list small {
    display: block;
    margin-top: 0.2rem;
    color: #93a0b2;
    font-size: 0.83rem;
  }

  .contact-board {
    margin-top: 1rem;
    padding: 1.25rem 1.25rem 1.3rem;
  }

  .contact-board .card-subtitle {
    margin: 0.28rem 0 0;
    color: #5f718f;
    line-height: 1.75;
  }

  .contact-grid {
    margin-top: 1rem;
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1rem;
  }

  .contact-card {
    display: flex;
    flex-direction: column;
    min-height: 100%;
    padding: 1.08rem;
    border-radius: 24px;
    border: 1px solid rgba(201, 211, 227, 0.85);
    background: linear-gradient(180deg, rgba(252, 253, 255, 0.95), rgba(244, 248, 255, 0.92));
    transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
  }

  .contact-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 22px 36px rgba(53, 81, 138, 0.1);
    border-color: rgba(141, 168, 214, 0.95);
  }

  .contact-card img {
    display: block;
    width: 100%;
    max-width: 190px;
    margin: 0 auto 0.95rem;
    border-radius: 16px;
    border: 4px solid rgba(255, 255, 255, 0.98);
    box-shadow: 0 12px 24px rgba(15, 23, 42, 0.1);
  }

  .contact-card h3 {
    margin: 0;
    color: var(--home-text);
    font-size: 1.08rem;
  }

  .contact-card p {
    margin: 0.6rem 0 0;
    color: #5f718f;
    line-height: 1.8;
  }

  .contact-card .home-btn {
    width: 100%;
    margin-top: 1rem;
  }

  .mail-code {
    margin-top: 1rem;
    padding: 0.8rem 0.9rem;
    border-radius: 14px;
    border: 1px solid rgba(187, 201, 227, 0.9);
    background: linear-gradient(135deg, #f6f9ff, #fcfdff);
    color: #334155;
    font-family: var(--md-code-font, monospace);
    font-size: 0.95rem;
    font-weight: 700;
    user-select: all;
    word-break: break-all;
  }

  .social-links {
    display: grid;
    gap: 0.82rem;
    margin-top: 1rem;
  }

  .social-links a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 46px;
    border-radius: 16px;
    text-decoration: none;
    color: #fff;
    font-weight: 700;
    box-shadow: 0 10px 18px rgba(47, 95, 179, 0.15);
    transition: transform 0.22s ease, filter 0.22s ease, box-shadow 0.22s ease;
  }

  .social-links a:hover {
    transform: translateY(-2px);
    filter: saturate(1.06);
    box-shadow: 0 16px 24px rgba(47, 95, 179, 0.2);
  }

  .social-links a:nth-child(1) { background: linear-gradient(135deg, #1f2937, #374151); }
  .social-links a:nth-child(2) { background: linear-gradient(135deg, #1784c2, #0f74ab); }
  .social-links a:nth-child(3) { background: linear-gradient(135deg, #2d9be5, #177dc5); }
  .social-links a:nth-child(4) { background: linear-gradient(135deg, #1d67bd, #15549c); }

  @keyframes home-fade-in {
    from {
      opacity: 0;
      transform: translateY(12px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes glow-shift {
    0% {
      transform: rotate(0deg) scale(1);
      filter: blur(15px) hue-rotate(0deg);
    }
    50% {
      transform: rotate(180deg) scale(1.06);
      filter: blur(18px) hue-rotate(35deg);
    }
    100% {
      transform: rotate(360deg) scale(1);
      filter: blur(15px) hue-rotate(0deg);
    }
  }

  @keyframes float-avatar {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-4px); }
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
    .card-head {
      flex-direction: column;
    }

    .tag-cloud,
    .hero-actions,
    .contact-pills {
      justify-content: center;
    }

    .profile-stack {
      justify-items: center;
      text-align: center;
    }

    .top-row {
      grid-template-columns: 1fr;
      justify-items: center;
      text-align: center;
    }

    .intro-copy,
    .bio-card {
      text-align: left;
    }
  }

  @media (max-width: 720px) {
    :root {
      --home-page-width: min(94vw, 1380px);
    }

    .home-shell {
      padding-top: 0;
    }

    .profile-panel,
    .github-card,
    .reading-card,
    .contact-board {
      padding-left: 1rem;
      padding-right: 1rem;
      border-radius: 24px;
    }

    .dashboard-grid,
    .contact-grid {
      grid-template-columns: 1fr;
    }

    .avatar-glow,
    .flip-container {
      width: 150px;
      height: 150px;
    }

    .intro-copy h1 {
      font-size: 2.2rem;
    }

    #jinrishici-container {
      font-size: 1.16rem;
    }
  }
</style>

<div class="home-shell">
  <section class="hero-layout">
    <div class="profile-panel surface-card">
      <div class="profile-stack">
        <div class="top-row">
          <div class="avatar-glow">
            <div class="flip-container">
              <div class="image-container">
                <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/gzh.jpg" alt="gzh avatar front">
                <img src="https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/3f58b6cea54d446e22107fde739e843.jpg" alt="gzh avatar back">
              </div>
            </div>
          </div>

          <div class="poem-card">
            <div class="poem-meta">
              <span class="poem-seal"></span>
            </div>
            <div id="jinrishici-container">正在载入今日诗词...</div>
          </div>
        </div>

        <div class="intro-copy">
          <span class="eyebrow">GZH · Research / Code / Writing</span>
          <h1>gzh</h1>
          <p class="lead">
            专注计算机视觉、三维感知与工程实现，持续记录技术学习、科研笔记和折腾过程。
          </p>
        </div>

        <div class="tag-cloud">
          <span>SLAM</span>
          <span>3D 视觉</span>
          <span>自动驾驶</span>
          <span>工程复盘</span>
          <span>诗词与阅读</span>
        </div>

        <div class="hero-actions">
          <a class="home-btn home-btn--primary" href="https://github.com/Gongzihang6" target="_blank" rel="noopener">访问 GitHub</a>
          <a class="home-btn" href="about/files/slam-resume.pdf" target="_blank" rel="noopener">下载简历</a>
        </div>

        <div class="bio-card">
          <div class="section-kicker">个人简介</div>
          <p>偶发强迫症，长期热衷于技术、数学与把东西真正做出来这件事。偏爱能反复打磨的工作，也愿意把学习过程整理成别人能直接使用的文字。</p>
          <p>这里会持续沉淀视觉感知、算法理解、工具实践，以及一些不那么功利但能长期滋养人的内容。</p>
        </div>
      </div>
    </div>

    <div class="dashboard-panel">
      <div class="github-card surface-card">
        <div class="card-head">
          <div class="github-title">
            <strong>GitHub</strong>
            <span class="github-summary"><span id="github-summary-text">gzh 过去一年</span> <b id="github-total-count">--</b> 次贡献</span>
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

        <div class="github-chart-wrap">
          <div class="github-chart" id="github-chart" aria-label="GitHub contribution chart"></div>
          <div class="github-tooltip" id="github-tooltip"></div>
        </div>
      </div>

      <div class="dashboard-grid">
        <div class="reading-card surface-card">
          <h3>推荐文章</h3>
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
    <p class="card-subtitle">需要交流技术、项目合作或学习问题，都可以直接联系。</p>

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
        <div class="mail-code">zihanggong24@gmail.com</div>
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

<script>
  document.addEventListener("DOMContentLoaded", function() {
    var chartContainer = document.getElementById("github-chart");
    var tooltip = document.getElementById("github-tooltip");
    var totalNode = document.getElementById("github-total-count");
    var username = "Gongzihang6";

    function formatDate(dateText) {
      var date = new Date(dateText + "T00:00:00");
      if (Number.isNaN(date.getTime())) {
        return dateText;
      }
      return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日";
    }

    function levelClass(count) {
      if (!count) return "is-zero";
      if (count <= 2) return "is-l1";
      if (count <= 5) return "is-l2";
      if (count <= 9) return "is-l3";
      return "is-l4";
    }

    function renderError() {
      chartContainer.innerHTML = '<p style="margin:0;color:#5f718f;">贡献图暂时加载失败，请稍后刷新重试。</p>';
      if (totalNode) {
        totalNode.textContent = "--";
      }
    }

    function bindTooltip(nodes) {
      nodes.forEach(function(cell) {
        function showTooltip() {
          var date = cell.getAttribute("data-date");
          var countText = cell.getAttribute("data-count") || "0";
          tooltip.textContent = formatDate(date) + "：" + countText + " 次贡献";
          tooltip.classList.add("is-visible");

          var wrapRect = chartContainer.parentElement.getBoundingClientRect();
          var rect = cell.getBoundingClientRect();
          tooltip.style.left = rect.left - wrapRect.left + rect.width / 2 + "px";
          tooltip.style.top = rect.top - wrapRect.top + "px";
        }

        function hideTooltip() {
          tooltip.classList.remove("is-visible");
        }

        cell.addEventListener("mouseenter", showTooltip);
        cell.addEventListener("mousemove", showTooltip);
        cell.addEventListener("mouseleave", hideTooltip);
      });
    }

    function renderCalendar(contributions) {
      if (!Array.isArray(contributions) || !contributions.length) {
        renderError();
        return;
      }

      var sorted = contributions.slice().sort(function(a, b) {
        return a.date.localeCompare(b.date);
      });

      var firstDate = new Date(sorted[0].date + "T00:00:00");
      var startDate = new Date(firstDate);
      startDate.setDate(firstDate.getDate() - firstDate.getDay());

      var dataMap = new Map();
      var total = 0;
      sorted.forEach(function(item) {
        dataMap.set(item.date, item);
        total += Number(item.count || 0);
      });

      var monthLabels = [];
      var cells = [];
      var current = new Date(startDate);
      var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

      for (var week = 0; week < 53; week++) {
        if (week === 0 || current.getDate() <= 7) {
          monthLabels.push("<span>" + monthNames[current.getMonth()] + "</span>");
        } else {
          monthLabels.push("<span></span>");
        }

        for (var day = 0; day < 7; day++) {
          var dateText = current.toISOString().slice(0, 10);
          var entry = dataMap.get(dateText);
          var count = entry ? Number(entry.count || 0) : 0;
          cells.push('<button class="contrib-cell ' + levelClass(count) + '" data-date="' + dateText + '" data-count="' + count + '" aria-label="' + formatDate(dateText) + " " + count + ' 次贡献"></button>');
          current.setDate(current.getDate() + 1);
        }
      }

      var weekdays = ["", "Mon", "", "Wed", "", "Fri", ""].map(function(day) {
        return "<span>" + day + "</span>";
      }).join("");

      chartContainer.innerHTML =
        '<div class="github-calendar-head"><div class="github-months">' + monthLabels.join("") + '</div></div>' +
        '<div class="github-calendar"><div class="github-weekdays">' + weekdays + '</div><div class="github-grid">' + cells.join("") + "</div></div>";

      if (totalNode) {
        totalNode.textContent = String(total);
      }

      bindTooltip(chartContainer.querySelectorAll(".contrib-cell"));
    }

    fetch("https://github-contributions-api.jogruber.de/v4/" + username + "?y=last")
      .then(function(res) {
        if (!res.ok) throw new Error("request failed");
        return res.json();
      })
      .then(function(data) {
        if (!data || !Array.isArray(data.contributions)) {
          throw new Error("bad payload");
        }
        renderCalendar(data.contributions);
      })
      .catch(function() {
        renderError();
      });
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
