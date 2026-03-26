<?php
$conn = mysqli_connect("localhost", "root", "", "mehendi_booking");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>