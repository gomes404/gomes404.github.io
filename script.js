document.addEventListener('DOMContentLoaded', function() {
    const skillsReel = document.querySelector('.skills-reel');
    const skillItems = document.querySelectorAll('.skill-item');

    // Clone skill items to create a seamless loop
    skillItems.forEach(item => {
        const clone = item.cloneNode(true);
        skillsReel.appendChild(clone);
    });

    // Function to check if we need to reset the scroll position
    function checkScroll() {
        if (skillsReel.scrollLeft >= skillsReel.scrollWidth / 2) {
            skillsReel.scrollLeft = 0;
        } else if (skillsReel.scrollLeft <= 0) {
            skillsReel.scrollLeft = skillsReel.scrollWidth / 2;
        }
    }

    // Add event listener to continuously check scroll position
    skillsReel.addEventListener('scroll', checkScroll);

    // Start the animation
    function startAnimation() {
        skillsReel.scrollLeft += 1;
        requestAnimationFrame(startAnimation);
    }

    startAnimation();
});