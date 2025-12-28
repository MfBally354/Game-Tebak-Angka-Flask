// Animasi sederhana untuk form input
document.addEventListener('DOMContentLoaded', function() {
    const input = document.querySelector('input[type="number"]');
    
    if (input) {
        input.addEventListener('focus', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        input.addEventListener('blur', function() {
            this.style.transform = 'scale(1)';
        });
    }
    
    // Animasi untuk cards
    const cards = document.querySelectorAll('.mode-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 150);
    });
});
