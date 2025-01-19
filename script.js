document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll('.slide');
    const prevButton = document.querySelector('.left-arrow');
    const nextButton = document.querySelector('.right-arrow');
    let currentSlideIndex = 1; // Starts from the second slide (index 1)

    function updateSlides() {
        slides.forEach((slide, index) => {
            slide.classList.remove('current-slide', 'prev-slide', 'next-slide');
            slide.style.transition = 'opacity 1s ease-in-out'; // Ensures smooth fade transition
            if (index === currentSlideIndex) {
                slide.classList.add('current-slide');
                slide.style.opacity = 1;
            } else if (index === (currentSlideIndex - 1 + slides.length) % slides.length) {
                slide.classList.add('prev-slide');
                slide.style.opacity = 0;
            } else {
                slide.classList.add('next-slide');
                slide.style.opacity = 0;
            }
        });
    }

    // Set initial state of the slideshow
    updateSlides();

    prevButton.addEventListener('click', function () {
        currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        updateSlides();
    });

    nextButton.addEventListener('click', function () {
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        updateSlides();
    });
});
