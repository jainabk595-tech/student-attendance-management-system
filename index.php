<?php include 'includes/header.php'; ?>
<?php include 'includes/db.php'; ?>

<!-- HERO -->
<section class="hero fade-in">
    <div class="hero-left">
        <h1>Book Professional Mehendi Artists Near You</h1>
        <p>Explore trending designs & book instantly</p>

        <div class="hero-buttons">
            <button class="btn">Book Now</button>
            <button class="btn-outline">Explore Designs</button>
        </div>

        <div class="search-bar">

    <!-- STATE -->
    <select id="state" onchange="loadCities()">
        <option value="">Select State</option>
        <option>Maharashtra</option>
        <option>Gujarat</option>
        <option>Rajasthan</option>
        <option>Delhi</option>
    </select>

    <!-- CITY -->
    <select id="city">
        <option>Select City</option>
    </select>

    <!-- DATE -->
    <input type="date">

    <!-- SERVICE -->
    <select>
        <option>Service Type</option>
        <option>Bridal Mehendi</option>
        <option>Party Mehendi</option>
        <option>Engagement</option>
    </select>

    <!-- SEARCH BUTTON -->
    <button>🔍</button>

</div>
    </div>
</section>

<!-- TRENDING -->
<section class="section fade-in">
    <h2>Trending Now</h2>

    <div class="cards">

    <?php
    $result = mysqli_query($conn, "SELECT * FROM artists");
    while($row = mysqli_fetch_assoc($result)) {
    ?>

    <div class="card">
        <img src="/mehendi_booking/<?php echo $row['image']; ?>">
        <div class="card-body">
            <h3><?php echo $row['name']; ?></h3>
            <p>₹<?php echo $row['price']; ?></p>
        </div>
    </div>

    <?php } ?>

    </div>
</section>

<!-- SERVICES -->
<section class="section light fade-in">
    <h2>Services</h2>

    <div class="services">
        <div class="service">Bridal Mehendi</div>
        <div class="service">Party Mehendi</div>
        <div class="service">Engagement</div>
        <div class="service">Festival</div>
    </div>
</section>

<!-- HOW IT WORKS -->
<section class="section fade-in">
    <h2>How It Works</h2>

    <div class="steps">
        <div>Choose Design</div>
        <div>Select Artist</div>
        <div>Book Appointment</div>
    </div>
</section>

<!-- CTA -->
<section class="cta fade-in">
    <h2>Make Your Special Day Even More Beautiful</h2>
    <button class="btn">Get Started</button>
</section>

<?php include 'includes/footer.php'; ?>