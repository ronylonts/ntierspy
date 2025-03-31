document.addEventListener('DOMContentLoaded', function() {
    // Animation des éléments
    const featureBoxes = document.querySelectorAll('.feature-box');
    
    featureBoxes.forEach(box => {
        box.addEventListener('mouseenter', () => {
            box.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
        });
        
        box.addEventListener('mouseleave', () => {
            box.style.boxShadow = 'none';
        });
    });
});