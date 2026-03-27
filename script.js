// Navbar shadow on scroll
window.addEventListener("scroll", function () {
  document.querySelector(".header").classList.toggle("scrolled", window.scrollY > 50);
});

// Fade-in animation
const elements = document.querySelectorAll(".card, .service, .step");

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = 1;
      entry.target.style.transform = "translateY(0)";
    }
  });
});

elements.forEach(el => {
  el.style.opacity = 0;
  el.style.transform = "translateY(30px)";
  observer.observe(el);
});
// select state-city

const stateCityMap = {
  "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
  "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
  "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur"],
  "Delhi": ["New Delhi", "Dwarka", "Rohini"],
  "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
  "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
  "Uttar Pradesh": ["Lucknow", "Kanpur", "Noida"],
  "Madhya Pradesh": ["Indore", "Bhopal", "Gwalior"],
  "West Bengal": ["Kolkata", "Howrah", "Durgapur"],
  "Punjab": ["Chandigarh", "Ludhiana", "Amritsar"]
};

const stateSelect = document.getElementById("state");
const citySelect = document.getElementById("city");

stateSelect.addEventListener("change", function () {
  const selectedState = this.value;

  // Clear previous cities
  citySelect.innerHTML = '<option value="">Select City</option>';

  if (selectedState && stateCityMap[selectedState]) {
    stateCityMap[selectedState].forEach(city => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    });
  }
});
// services dropdown
const serviceSelect = document.getElementById("service");

serviceSelect.addEventListener("change", function () {
  const selectedPage = this.value;

  if (selectedPage) {
    window.location.href = selectedPage;
  }
});
function goToService() {
  const selectedPage = document.getElementById("service").value;

  console.log("Selected:", selectedPage); // debug

  if (selectedPage) {
    window.location.href = selectedPage;
  } else {
    alert("Please select a service");
  }
}