const elements = document.querySelectorAll('.fade-in');

window.addEventListener('scroll', () => {
    elements.forEach(el => {
        const position = el.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            el.classList.add('show');
        }
    });
});
function loadCities() {
    const state = document.getElementById("state").value;
    const cityDropdown = document.getElementById("city");

    let cities = [];

    if (state === "Maharashtra") {
        cities = ["Mumbai", "Pune", "Nagpur", "Nashik"];
    } 
    else if (state === "Gujarat") {
        cities = ["Ahmedabad", "Surat", "Vadodara"];
    }
    else if (state === "Rajasthan") {
        cities = ["Jaipur", "Udaipur", "Jodhpur"];
    }

    cityDropdown.innerHTML = "<option>Select City</option>";

    cities.forEach(city => {
        let option = document.createElement("option");
        option.value = city;
        option.text = city;
        cityDropdown.appendChild(option);
    });
}