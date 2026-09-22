document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('navToggle');
    const drawer = document.getElementById('mobileDrawer');
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;
    const toggleLabel = themeToggle.querySelector('.toggle-label');

    toggle.addEventListener('click', () => {
        drawer.classList.toggle('open');
        toggle.classList.toggle('active');
    });

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        html.setAttribute('data-theme', savedTheme);
        toggleLabel.textContent = savedTheme === 'dark' ? 'Dark' : 'Light';
        themeToggle.classList.toggle('dark', savedTheme === 'dark');
    }

    themeToggle.addEventListener('click', () => {
        const current = html.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        toggleLabel.textContent = next === 'dark' ? 'Dark' : 'Light';
        themeToggle.classList.toggle('dark', next === 'dark');
    });

    gsap.from('.page-content', {
        opacity: 0,
        y: 15,
        duration: 0.5,
        ease: 'power2.out'
    });
});