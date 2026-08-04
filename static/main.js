window.addEventListener('scroll', () => {
  // 1. How far the user has scrolled from the top
  const scrollTop = window.scrollY || document.documentElement.scrollTop;

  // 2. Total height of the entire document
  const totalHeight = document.documentElement.scrollHeight;

  // 3. Height of the visible screen (viewport)
  const viewportHeight = document.documentElement.clientHeight;

  // 4. Maximum distance the user can actually scroll
  const scrollableDistance = totalHeight - viewportHeight;

  // 5. Calculate percentage (prevent division by zero if page is not scrollable)
  const scrollProgress = scrollableDistance > 0
    ? (scrollTop / scrollableDistance) * 100
    : 0;

  // Example: Update a progress bar width if you have one
  // document.getElementById('progress-bar').style.width = `${scrollProgress}%`;
  document.querySelector(".sidebar").style.transform = `translateY(${scrollProgress}%)`
});

/*const cards = document.querySelectorAll(".project-card");

let maxHeight = 0;

cards.forEach(card => {
    maxHeight = Math.max(maxHeight, card.offsetHeight);
});

cards.forEach(card => {
    card.style.minHeight = `${maxHeight}px`;
});*/
