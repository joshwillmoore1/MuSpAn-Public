// carousel_autoplay.js
// Auto-start all carousels on the page with a 3 second interval (3000 ms).
// Adjust interval value as needed.
document.addEventListener('DOMContentLoaded', function () {
    // selector used by sphinx-carousel for the outer element is usually ".carousel"
    var carousels = document.querySelectorAll('.carousel');
    carousels.forEach(function (el) {
      // If bootstrap is available, get or create a Carousel instance with options
      if (window.bootstrap && window.bootstrap.Carousel) {
        // options: interval in ms; pause controls whether to pause on hover
        window.bootstrap.Carousel.getOrCreateInstance(el, {
          interval: 5000,
          pause: 'hover',   // or false to never pause
          ride: 'carousel'  // ensures it starts automatically
        });
      }
    });
  });
  