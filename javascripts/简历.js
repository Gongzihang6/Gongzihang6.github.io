// 页面加载完成后执行
document.addEventListener("DOMContentLoaded", function() {
    // 获取所有简历部分
    const sections = document.querySelectorAll('.resume-section');
    
    // 监听滚动事件
    window.addEventListener('scroll', function() {
        // 遍历每个简历部分
        sections.forEach(section => {
            // 获取元素位置
            const sectionTop = section.getBoundingClientRect().top;
            // 获取窗口高度
            const windowHeight = window.innerHeight;
            
            // 如果元素在窗口可视范围内，则添加可见类
            if (sectionTop < windowHeight * 0.85) {
                section.classList.add('visible');
            }
        });
    });
    
    // 初始检查
    sections.forEach(section => {
        if (section.getBoundingClientRect().top < window.innerHeight) {
            section.classList.add('visible');
        }
    });
    
    // 为项目标题添加点击展开/折叠功能
    const projectTitles = document.querySelectorAll('.project-title');
    projectTitles.forEach(title => {
        title.addEventListener('click', function() {
            const content = this.nextElementSibling;
            if (content.style.display === 'none') {
                content.style.display = 'block';
                this.style.cursor = 'default';
            } else {
                content.style.display = 'none';
                this.style.cursor = 'pointer';
            }
        });
    });
    
    // 为教育背景添加鼠标悬停效果
    const educationSection = document.querySelector('.section-title:contains("教育背景")');
    if (educationSection) {
        educationSection.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#2980b9';
            this.style.transition = 'background-color 0.3s ease';
        });
        
        educationSection.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '#3498db';
        });
    }
});