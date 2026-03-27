const track = document.querySelector(".carousel-track");
const next = document.querySelector(".next");
const prev = document.querySelector(".prev");

let index = 0;

next.addEventListener("click", () => {
  index += 1;
  track.style.transform = `translateX(-${index * 280}px)`;
});

prev.addEventListener("click", () => {
  if (index > 0) index--;
  track.style.transform = `translateX(-${index * 280}px)`;
});