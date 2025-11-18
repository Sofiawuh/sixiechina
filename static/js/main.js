document.addEventListener('DOMContentLoaded', function() {
    // 导航栏滚动效果
    const header = document.querySelector('.header');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('shrink');
        } else {
            header.classList.remove('shrink');
        }
    });

    // 轮播图功能
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;
    let interval;

    // 切换到指定幻灯片
    function goToSlide(index) {
        if (index < 0) index = slides.length - 1;
        if (index >= slides.length) index = 0;

        slider.style.transform = `translateX(-${index * 100}%)`;

        // 更新活动状态
        slides.forEach(slide => slide.classList.remove('active'));
        slides[index].classList.add('active');

        dots.forEach(dot => dot.classList.remove('active'));
        dots[index].classList.add('active');

        currentIndex = index;
    }

    // 自动轮播
    function startAutoSlide() {
        interval = setInterval(() => {
            goToSlide(currentIndex + 1);
        }, 5000); // 5秒切换一次
    }

    // 小点点击事件
    dots.forEach(dot => {
        dot.addEventListener('click', function() {
            const slideIndex = parseInt(this.getAttribute('data-slide'));
            goToSlide(slideIndex);
            resetAutoSlide();
        });

        // 鼠标悬停事件
        dot.addEventListener('mouseenter', function() {
            const slideIndex = parseInt(this.getAttribute('data-slide'));
            goToSlide(slideIndex);
            resetAutoSlide();
        });
    });

    // 重置自动轮播
    function resetAutoSlide() {
        clearInterval(interval);
        startAutoSlide();
    }

    // 初始化
    startAutoSlide();

    // 响应式菜单
    const menuToggle = document.createElement('div');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '☰';
    document.querySelector('.header-in').appendChild(menuToggle);

    menuToggle.addEventListener('click', function() {
        const nav = document.querySelector('.mheader-nav');
        nav.style.display = nav.style.display === 'block' ? 'none' : 'block';
    });

    function adjustMenu() {
        const nav = document.querySelector('.mheader-nav');
        if (window.innerWidth > 768) {
            nav.style.display = 'block';
        } else {
            nav.style.display = 'none';
        }
    }

    window.addEventListener('resize', adjustMenu);
    adjustMenu();
});
